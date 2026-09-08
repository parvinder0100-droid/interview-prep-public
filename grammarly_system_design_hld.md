# Grammarly High-Level Design (HLD) & System Architecture

## 1. System Overview & Problem Statement
Grammarly is a real-time AI writing assistant providing grammatical error correction (GEC), spell checking, tone detection, clarity suggestions, and generative rewrites across multiple client platforms (browsers, desktop OS hooks, mobile keyboards, and web editors).

---

## 2. Requirements & Scale Estimations

### 2.1 Functional Requirements
1. **Real-time Spell & Grammar Checking**: Low-latency underline annotations as the user types.
2. **Context-Aware Style & Tone Analysis**: Formality, clarity, conciseness, and tone scoring.
3. **Generative Sentence Rewriting**: LLM-assisted rephrasing with tone adjustment.
4. **Plagiarism Detection**: Semantic text similarity against billions of web documents.
5. **Personal & Enterprise Customization**: Custom dictionaries, brand tone guidelines, sensitive data masking.
6. **Multi-Platform Support**: Browser extensions, native desktop apps, mobile keyboards, Word/GDocs add-ins.

### 2.2 Non-Functional Requirements
1. **Ultra-Low Latency**:
   - Fast spell / basic typo check: **< 15ms**
   - Deep NLP / GEC inference: **< 80ms - 150ms**
   - Total roundtrip to user: **< 200ms**
2. **High Throughput & Availability**:
   - 100M+ Daily Active Users (DAU)
   - Peak throughput: **150,000+ QPS**
   - 99.99% system availability
3. **Data Privacy & Security**:
   - Zero Data Retention (ZDR) mode for enterprise customers.
   - PII / HIPAA compliant data scrubbing before persistence.
   - In-transit (TLS 1.3) and at-rest (AES-256 KMS) encryption.

---

## 3. High-Level Architecture (Excalidraw Map)

The architecture is organized into **6 core tiers** as represented in [`grammarly_hld.excalidraw`](file:///~/InterviewPrep/grammarly_hld.excalidraw):

```
+-------------------------------------------------------------------------------------------------------+
|                                    1. CLIENT ECOSYSTEM                                                |
| [Browser Extension] [Desktop Native Hook] [Mobile Keyboard] [Web Editor] [MS Word / GDocs Plugin]     |
| (Debouncing 300ms • Sentence Segmentation • Myers Text Diffing • Local Bloom Filter • Token Tracking) |
+---------------------------------------------------+---------------------------------------------------+
                                                    |
                                                    | (WSS Live Diffs / HTTPS Batch)
                                                    v
+-------------------------------------------------------------------------------------------------------+
|                                  2. INGRESS & EDGE LAYER                                              |
| [Cloudflare CDN/DDoS] ---> [Sticky WebSocket Gateways] / [API Gateway Envoy]                          |
|                            [Auth & JWT Service]        [Rate Limiter - Redis Token Bucket]            |
+---------------------------------------------------+---------------------------------------------------+
                                                    |
                                                    v
+-------------------------------------------------------------------------------------------------------+
|                               3. CORE PROCESSING PIPELINE                                             |
| [Document & Session Manager] (Buffer sync, Cursor offsets, Active document state)                     |
|         |                                              |                                              |
|         +---> [Fast Path: Linter (<10ms)]              +---> [Deep NLP / GEC Orchestrator]            |
|               (SymSpell, Trie, Bloom Filters, Dict)          (Multi-model context coordinator)        |
|                                                              |                                        |
|         +----------------------------------------------------+-------------------------+              |
|         | [Tone & Clarity]   | [Plagiarism Service]   | [GenAI Rewrites]  | [Custom Style Guides]     |
+---------+--------------------+------------------------+-------------------+---------------------------+
          |                                                                 |
          v                                                                 v
+------------------------------------+             +----------------------------------------------------+
|    4. ML INFERENCE PLATFORM        |             |         5. STORAGE & CACHING TIER                  |
| [Triton Inference Server (GPU)]    |             | [Redis Cluster] -> Active Sessions & L1 Suggestion |
| [GEC Transformer (T5/BART Seq2Seq)]| <---------> | [PostgreSQL]    -> User profiles, teams, metadata  |
| [Tone / Style Classifiers (RoBERTa)]|             | [Vector DB]     -> Milvus/Pinecone 100M+ docs     |
| [Quantization: FP16/INT8, TensorRT]|             | [S3 Blob Store] -> Doc versions, Model Weights     |
+------------------------------------+             +----------------------------------------------------+
          |                                                                 |
          +---------------------------------+-------------------------------+
                                            |
                                            v (Telemetry: Accept / Reject / Dismiss)
+-------------------------------------------------------------------------------------------------------+
|                       6. ASYNCHRONOUS FEEDBACK & ACTIVE LEARNING LOOP                                 |
| [Apache Kafka Event Stream] ---> [Flink Stream Analytics] ---> [Active Learning Curation]             |
|                                                                          |                            |
| [Canary GPU Deploy to Triton] <---------------- [MLflow Model Registry & A/B Eval Pipeline] <--------+
+-------------------------------------------------------------------------------------------------------+
```

---

## 4. Deep-Dive: Key Architectural Subsystems

### 4.1 Client-Side Optimization (Debouncing & Diffing)
Sending every keystroke to backend servers would saturate network bandwidth and overwhelm GPU clusters:
- **300ms Idle Debounce**: Requests are only dispatched when user pauses or hits sentence terminators (`.`, `!`, `?`, `\n`).
- **Myers Text Diffing**: Client computes delta patches (`{offset: 142, deleted: "teh", inserted: "the"}`) rather than sending the entire document.
- **Client-Side Bloom Filter**: Instantly intercepts 10,000+ common typos locally before touching the network.

### 4.2 Two-Tier Hybrid Inspection Engine
1. **Tier 1: Fast Rule-Based Linter (< 10ms)**
   - Uses **SymSpell** (Symmetric Delete algorithm) + **Trie / Inverted Index** for instant spell check.
   - Deterministic regex and AST grammar rules for obvious agreement mistakes (e.g. *"an apple"* vs *"a apple"*).
2. **Tier 2: Deep Neural GEC Inference (< 80ms)**
   - Fine-tuned Seq2Seq transformer (e.g., T5 / BART / custom encoder-decoder).
   - Context window of $\pm 3$ sentences around the cursor.
   - Dynamic batching on **NVIDIA Triton Inference Servers** with **TensorRT-LLM** optimization.

### 4.3 Data Storage & Caching Matrix
| Component | Technology | Primary Purpose | Latency Target |
| :--- | :--- | :--- | :--- |
| **Session Cache** | Redis Cluster | Active WebSocket connection state, sentence hash cache | $< 1\text{ ms}$ |
| **Relational DB** | PostgreSQL / CockroachDB | User accounts, team subscriptions, custom style rules | $< 10\text{ ms}$ |
| **Vector DB** | Milvus / Pinecone | Plagiarism similarity search against 100M+ web embeddings | $< 40\text{ ms}$ |
| **Event Bus** | Apache Kafka | Telemetry streams, accept/reject feedback events | $< 5\text{ ms}$ ingest |
| **Object Store** | AWS S3 / GCS | Long-term document storage, model weights, checkpoints | N/A (Async) |

### 4.4 Continuous Active Learning & Feedback Loop
- When a user **accepts** or **rejects** a suggestion, the event is streamed to **Kafka**.
- **Hard Negative Mining**: Rejected suggestions with high confidence flag edge cases for linguist annotation.
- Models are retrained, benchmarked on offline datasets, and deployed via **Shadow Traffic & 1% Canary** before full rollout.

---

## 5. How to Open the Excalidraw Diagram
1. Open [excalidraw.com](https://excalidraw.com) in your browser.
2. Click the hamburger menu on the top-left $\rightarrow$ **Open...**
3. Select [`~/InterviewPrep/grammarly_hld.excalidraw`](file:///~/InterviewPrep/grammarly_hld.excalidraw) (or drag-and-drop the file directly onto the canvas).
