#!/usr/bin/env python3
import json
import uuid
import random

def gen_id():
    return str(uuid.uuid4())[:8]

def create_rect(x, y, w, h, bg_color="#ffffff", stroke_color="#1e1e1e", stroke_width=2, stroke_style="solid", roughness=0, roundness=3, opacity=100, fill_style="solid"):
    return {
        "id": gen_id(),
        "type": "rectangle",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": stroke_color,
        "backgroundColor": bg_color,
        "fillStyle": fill_style,
        "strokeWidth": stroke_width,
        "strokeStyle": stroke_style,
        "roughness": roughness,
        "opacity": opacity,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": roundness} if roundness else None,
        "seed": random.randint(1, 1000000),
        "version": 1,
        "versionNonce": random.randint(1, 1000000),
        "isDeleted": False,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False
    }

def create_text(x, y, text, font_size=14, font_family=1, text_align="center", stroke_color="#1e1e1e", opacity=100):
    lines = text.split("\n")
    line_height = 1.3
    approx_w = max([len(line) for line in lines]) * (font_size * 0.58)
    approx_h = len(lines) * (font_size * line_height)
    
    return {
        "id": gen_id(),
        "type": "text",
        "x": x,
        "y": y,
        "width": max(approx_w, 20),
        "height": max(approx_h, 20),
        "angle": 0,
        "strokeColor": stroke_color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": opacity,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "seed": random.randint(1, 1000000),
        "version": 1,
        "versionNonce": random.randint(1, 1000000),
        "isDeleted": False,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
        "text": text,
        "fontSize": font_size,
        "fontFamily": font_family,
        "textAlign": text_align,
        "verticalAlign": "top",
        "baseline": font_size,
        "containerId": None,
        "originalText": text,
        "lineHeight": line_height
    }

def create_card(x, y, w, h, title, lines_list, bg_color="#ffffff", stroke_color="#1971c2", title_color="#1864ab", badge=None):
    elements = []
    # Main container
    box = create_rect(x, y, w, h, bg_color=bg_color, stroke_color=stroke_color, stroke_width=2, roundness=3)
    elements.append(box)
    
    # Title
    t_elem = create_text(x + 16, y + 14, title, font_size=15, stroke_color=title_color, text_align="left")
    elements.append(t_elem)
    
    # Optional Badge (e.g. latency, technology)
    if badge:
        bw = len(badge) * 7 + 14
        badge_box = create_rect(x + w - bw - 12, y + 12, bw, 20, bg_color=stroke_color, stroke_color=stroke_color, stroke_width=1, roundness=2)
        badge_txt = create_text(x + w - bw - 8, y + 15, badge, font_size=10, stroke_color="#ffffff", text_align="left")
        elements.extend([badge_box, badge_txt])
        
    # Content lines
    body_text = "\n".join(lines_list)
    b_elem = create_text(x + 16, y + 42, body_text, font_size=12, stroke_color="#495057", text_align="left")
    elements.append(b_elem)
    
    return elements

def create_arrow(start_pt, end_pt, stroke_color="#495057", stroke_width=2, stroke_style="solid", label=None, label_above=True):
    elements = []
    dx = end_pt[0] - start_pt[0]
    dy = end_pt[1] - start_pt[1]
    
    arrow_elem = {
        "id": gen_id(),
        "type": "arrow",
        "x": start_pt[0],
        "y": start_pt[1],
        "width": abs(dx),
        "height": abs(dy),
        "angle": 0,
        "strokeColor": stroke_color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": stroke_width,
        "strokeStyle": stroke_style,
        "roughness": 0,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 2},
        "seed": random.randint(1, 1000000),
        "version": 1,
        "versionNonce": random.randint(1, 1000000),
        "isDeleted": False,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
        "points": [[0, 0], [dx, dy]],
        "lastCommittedPoint": None,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": "arrow"
    }
    elements.append(arrow_elem)
    
    if label:
        mid_x = start_pt[0] + dx / 2
        mid_y = start_pt[1] + dy / 2 + (-22 if label_above else 8)
        lw = len(label) * 7 + 16
        # Background pill for label to prevent overlap
        lbl_bg = create_rect(mid_x - lw/2, mid_y, lw, 20, bg_color="#ffffff", stroke_color="#ced4da", stroke_width=1, roundness=2)
        lbl_txt = create_text(mid_x - lw/2 + 8, mid_y + 3, label, font_size=11, stroke_color=stroke_color, text_align="left")
        elements.extend([lbl_bg, lbl_txt])
        
    return elements

def create_multi_point_arrow(points, stroke_color="#495057", stroke_width=2, stroke_style="solid", label=None, label_pos=None):
    elements = []
    base_x, base_y = points[0]
    rel_points = [[p[0] - base_x, p[1] - base_y] for p in points]
    
    min_x = min(p[0] for p in rel_points)
    max_x = max(p[0] for p in rel_points)
    min_y = min(p[1] for p in rel_points)
    max_y = max(p[1] for p in rel_points)
    
    arrow_elem = {
        "id": gen_id(),
        "type": "arrow",
        "x": base_x,
        "y": base_y,
        "width": max_x - min_x,
        "height": max_y - min_y,
        "angle": 0,
        "strokeColor": stroke_color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": stroke_width,
        "strokeStyle": stroke_style,
        "roughness": 0,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 2},
        "seed": random.randint(1, 1000000),
        "version": 1,
        "versionNonce": random.randint(1, 1000000),
        "isDeleted": False,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
        "points": rel_points,
        "lastCommittedPoint": None,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": "arrow"
    }
    elements.append(arrow_elem)
    
    if label and label_pos:
        lx, ly = label_pos
        lw = len(label) * 7 + 16
        lbl_bg = create_rect(lx - lw/2, ly, lw, 20, bg_color="#ffffff", stroke_color="#ced4da", stroke_width=1, roundness=2)
        lbl_txt = create_text(lx - lw/2 + 8, ly + 3, label, font_size=11, stroke_color=stroke_color, text_align="left")
        elements.extend([lbl_bg, lbl_txt])
        
    return elements

def build_clean_diagram():
    elements = []
    
    # ----------------------------------------------------
    # HEADER BANNER (Top)
    # ----------------------------------------------------
    elements.append(create_rect(50, 40, 1820, 90, bg_color="#1864ab", stroke_color="#1864ab", roundness=3))
    elements.append(create_text(80, 56, "Grammarly System Architecture — High-Level Design (HLD)", font_size=22, stroke_color="#ffffff", text_align="left"))
    elements.append(create_text(80, 88, "Real-Time AI Writing Assistant • Sub-80ms Multi-Tier GEC Inference • Debounced Stream Sync • Active Learning", font_size=13, stroke_color="#d0ebff", text_align="left"))

    # ----------------------------------------------------
    # 5 MAIN HORIZONTAL ZONES (Columns)
    # ----------------------------------------------------
    # Col 1: Clients (x: 50, w: 280)
    # Col 2: Gateway & Edge (x: 390, w: 290)
    # Col 3: Processing & NLP (x: 740, w: 340)
    # Col 4: ML Inference (x: 1140, w: 320)
    # Col 5: Storage & Cache (x: 1520, w: 350)
    
    # ZONE 1: CLIENTS
    elements.append(create_rect(50, 160, 290, 680, bg_color="#f8f9fa", stroke_color="#1971c2", stroke_style="dashed", stroke_width=2, roundness=3))
    elements.append(create_rect(65, 175, 160, 26, bg_color="#1971c2", stroke_color="#1971c2", roundness=2))
    elements.append(create_text(75, 180, "1. Client Ecosystem", font_size=13, stroke_color="#ffffff", text_align="left"))
    
    elements.extend(create_card(70, 220, 250, 90, "Browser Extension", ["• Chrome, Safari, Edge", "• DOM mutation & cursor tracking", "• 300ms debounce buffer"], bg_color="#ffffff", stroke_color="#1971c2", title_color="#1864ab"))
    elements.extend(create_card(70, 330, 250, 90, "Desktop & Mobile OS", ["• macOS / Windows native hooks", "• iOS / Android virtual keyboard", "• Low-latency mobile predictions"], bg_color="#ffffff", stroke_color="#1971c2", title_color="#1864ab"))
    elements.extend(create_card(70, 440, 250, 90, "Rich Web & Office Plugins", ["• Grammarly Web Editor", "• MS Word, Outlook, Google Docs", "• Chunked document syncing"], bg_color="#ffffff", stroke_color="#1971c2", title_color="#1864ab"))
    
    # Client Smart features box
    elements.extend(create_card(70, 560, 250, 250, "Client-Side Intelligence", [
        "• 300ms Idle Debouncing",
        "• Sentence Boundary Detection",
        "• Myers Text Diffing (Delta Patches)",
        "• Local Bloom Filter (Common Typos)",
        "• Token & Cursor Offset Mapping",
        "• Local Cache for Frequent Queries"
    ], bg_color="#e7f5ff", stroke_color="#1971c2", title_color="#1864ab"))

    # ZONE 2: INGRESS & GATEWAY
    elements.append(create_rect(380, 160, 300, 680, bg_color="#f8f9fa", stroke_color="#7048e8", stroke_style="dashed", stroke_width=2, roundness=3))
    elements.append(create_rect(395, 175, 180, 26, bg_color="#7048e8", stroke_color="#7048e8", roundness=2))
    elements.append(create_text(405, 180, "2. Ingress & Edge Layer", font_size=13, stroke_color="#ffffff", text_align="left"))
    
    elements.extend(create_card(400, 220, 260, 95, "Cloudflare Edge & WAF", ["• Anycast DNS & TLS 1.3 Termination", "• DDoS Shield & Bot Mitigation", "• Edge Static Asset Caching"], bg_color="#ffffff", stroke_color="#7048e8", title_color="#5f3dc4", badge="Global Edge"))
    elements.extend(create_card(400, 335, 260, 115, "WebSocket Gateway", ["• Stateful, persistent connections", "• User-session sticky routing", "• Real-time keystroke diff streaming", "• Sub-20ms bidirectional stream"], bg_color="#ffffff", stroke_color="#7048e8", title_color="#5f3dc4", badge="Stateful WS"))
    elements.extend(create_card(400, 470, 260, 105, "API Gateway (Envoy/Kong)", ["• REST & gRPC endpoints", "• Large batch document analysis", "• User settings & workspace APIs"], bg_color="#ffffff", stroke_color="#7048e8", title_color="#5f3dc4", badge="REST/gRPC"))
    elements.extend(create_card(400, 595, 260, 105, "Auth & Rate Limiting", ["• OAuth2 & JWT Verification", "• Subscription tier check (Free/Pro)", "• Redis Token Bucket Rate Limiter"], bg_color="#ffffff", stroke_color="#7048e8", title_color="#5f3dc4"))
    elements.extend(create_card(400, 720, 260, 95, "Ingress Load Balancer", ["• L4/L7 NLB with health checks", "• Connection draining & auto-failover", "• Zero-downtime rolling deploys"], bg_color="#f3f0ff", stroke_color="#7048e8", title_color="#5f3dc4"))

    # ZONE 3: CORE PROCESSING PIPELINE
    elements.append(create_rect(720, 160, 360, 680, bg_color="#f8f9fa", stroke_color="#0ca678", stroke_style="dashed", stroke_width=2, roundness=3))
    elements.append(create_rect(735, 175, 210, 26, bg_color="#0ca678", stroke_color="#0ca678", roundness=2))
    elements.append(create_text(745, 180, "3. Core Processing Pipeline", font_size=13, stroke_color="#ffffff", text_align="left"))
    
    elements.extend(create_card(740, 220, 320, 95, "Session & Buffer Manager", ["• Text diff patch reconciliation", "• Document cursor & span offset math", "• Per-user active document lock"], bg_color="#ffffff", stroke_color="#0ca678", title_color="#099268", badge="State Sync"))
    elements.extend(create_card(740, 335, 320, 110, "Fast Path: Spell Linter", ["• SymSpell / Trie Dictionary (<10ms)", "• Fast regex & deterministic rules", "• Instant typo & capitalization checks", "• Local word frequency ranking"], bg_color="#ffffff", stroke_color="#0ca678", title_color="#099268", badge="< 10ms"))
    elements.extend(create_card(740, 465, 320, 125, "Deep GEC Orchestrator", ["• Multi-model inference coordinator", "• Context window extraction (±3 sentences)", "• Suggestion deduplication & ranking", "• Confidence threshold filtering"], bg_color="#ffffff", stroke_color="#0ca678", title_color="#099268", badge="Async Core"))
    elements.extend(create_card(740, 610, 320, 100, "Tone, Style & Clarity Engine", ["• Formality & confidence scoring", "• Conciseness & passive-voice rewrite", "• Vocabulary enhancement suggestions"], bg_color="#ffffff", stroke_color="#0ca678", title_color="#099268"))
    elements.extend(create_card(740, 730, 320, 90, "Custom Rules & Vocab Service", ["• Enterprise brand style guidelines", "• Custom personal/org dictionary", "• PII & sensitive data masking"], bg_color="#e6fcf5", stroke_color="#0ca678", title_color="#099268"))

    # ZONE 4: ML INFERENCE PLATFORM
    elements.append(create_rect(1120, 160, 340, 680, bg_color="#f8f9fa", stroke_color="#f76707", stroke_style="dashed", stroke_width=2, roundness=3))
    elements.append(create_rect(1135, 175, 210, 26, bg_color="#f76707", stroke_color="#f76707", roundness=2))
    elements.append(create_text(1145, 180, "4. ML Inference Platform", font_size=13, stroke_color="#ffffff", text_align="left"))
    
    elements.extend(create_card(1140, 220, 300, 100, "Triton Model Serving Cluster", ["• Dynamic Batching (5-10ms window)", "• TensorRT-LLM GPU acceleration", "• Auto-scaling GPU pods (K8s / HPA)"], bg_color="#ffffff", stroke_color="#f76707", title_color="#d9480f", badge="GPU Cluster"))
    elements.extend(create_card(1140, 340, 300, 105, "GEC Neural Transformer", ["• Seq2Seq Grammar Model (T5/BART)", "• Token edit & span replacement", "• Grammatical Error Correction (<60ms)"], bg_color="#ffffff", stroke_color="#f76707", title_color="#d9480f", badge="Seq2Seq"))
    elements.extend(create_card(1140, 465, 300, 95, "Tone / Clarity Classifiers", ["• Multi-Head RoBERTa / DeBERTa", "• Readability & emotion rating", "• Sentence complexity analysis"], bg_color="#ffffff", stroke_color="#f76707", title_color="#d9480f"))
    elements.extend(create_card(1140, 580, 300, 105, "Generative LLM Rewriter", ["• Full-sentence contextual rewrites", "• Tone shifting (Formal / Casual / Short)", "• Guardrail filtering & prompt safety"], bg_color="#ffffff", stroke_color="#f76707", title_color="#d9480f", badge="GenAI"))
    elements.extend(create_card(1140, 705, 300, 115, "Model Optimization Layer", ["• FP16 / INT8 Model Quantization", "• Sentence KV-Cache for active docs", "• Failover to fast rule-based linter"], bg_color="#fff4e6", stroke_color="#f76707", title_color="#d9480f"))

    # ZONE 5: STORAGE & CACHING
    elements.append(create_rect(1500, 160, 370, 680, bg_color="#f8f9fa", stroke_color="#1098ad", stroke_style="dashed", stroke_width=2, roundness=3))
    elements.append(create_rect(1515, 175, 200, 26, bg_color="#1098ad", stroke_color="#1098ad", roundness=2))
    elements.append(create_text(1525, 180, "5. Storage & Caching Layer", font_size=13, stroke_color="#ffffff", text_align="left"))
    
    elements.extend(create_card(1520, 220, 330, 105, "Redis Cluster (Cache Tier)", ["• Active WebSocket session registry", "• Fast sentence hash cache (L1 cache)", "• User token buckets & hot dictionary", "• Sub-millisecond read latency"], bg_color="#ffffff", stroke_color="#1098ad", title_color="#0b7285", badge="< 1ms Cache"))
    elements.extend(create_card(1520, 345, 330, 105, "PostgreSQL / CockroachDB", ["• User profiles, teams & subscriptions", "• Custom enterprise style guides", "• Organization vocabulary & rule sets", "• ACID transactional metadata"], bg_color="#ffffff", stroke_color="#1098ad", title_color="#0b7285", badge="Primary DB"))
    elements.extend(create_card(1520, 470, 330, 105, "Vector DB (Milvus / Pinecone)", ["• 100M+ web document embeddings", "• HNSW indexed passage vectors", "• Real-time semantic similarity search", "• Sub-40ms plagiarism matching"], bg_color="#ffffff", stroke_color="#1098ad", title_color="#0b7285", badge="Vector Search"))
    elements.extend(create_card(1520, 595, 330, 95, "S3 Blob Storage", ["• Long-term document version history", "• Export snapshots (PDF, Docx)", "• ML model checkpoints & weights"], bg_color="#ffffff", stroke_color="#1098ad", title_color="#0b7285"))
    elements.extend(create_card(1520, 710, 330, 110, "Privacy & Data Governance", ["• Zero Data Retention (ZDR) mode", "• AES-256 KMS Envelope Encryption", "• PII scrubbing before persistence", "• SOC2 Type II & GDPR compliant"], bg_color="#e3fafc", stroke_color="#1098ad", title_color="#0b7285"))

    # ----------------------------------------------------
    # ZONE 6: ASYNC FEEDBACK LOOP (Bottom Banner)
    # ----------------------------------------------------
    elements.append(create_rect(50, 870, 1820, 230, bg_color="#f8f9fa", stroke_color="#d6336c", stroke_style="dashed", stroke_width=2, roundness=3))
    elements.append(create_rect(65, 885, 320, 26, bg_color="#d6336c", stroke_color="#d6336c", roundness=2))
    elements.append(create_text(75, 890, "6. Asynchronous Feedback & Active Learning Loop", font_size=13, stroke_color="#ffffff", text_align="left"))

    elements.extend(create_card(70, 930, 400, 140, "Apache Kafka / Event Bus", [
        "Event Topics Ingested:",
        "• Suggestion Shown to User",
        "• Suggestion Accepted / Rejected / Ignored",
        "• User Manual Override Edit",
        "• Inference Latency & Error Telemetry"
    ], bg_color="#ffffff", stroke_color="#d6336c", title_color="#a61e4d", badge="Event Stream"))

    elements.extend(create_card(510, 930, 400, 140, "Analytics & Metric Tracking", [
        "Apache Flink / Spark Streaming:",
        "• Real-time model precision/recall calculation",
        "• High false-positive rate anomaly alerts",
        "• Rule acceptance metrics by category",
        "• Aggregated dashboard data in ClickHouse"
    ], bg_color="#ffffff", stroke_color="#d6336c", title_color="#a61e4d", badge="Stream Analytics"))

    elements.extend(create_card(950, 930, 420, 140, "Active Learning & Curation", [
        "Continuous Model Improvement:",
        "• Hard Negative Mining on rejected edits",
        "• Synthetic typo & error generation pipeline",
        "• Human-in-the-loop linguist review queue",
        "• Automated benchmark dataset curation"
    ], bg_color="#ffffff", stroke_color="#d6336c", title_color="#a61e4d", badge="Data Curation"))

    elements.extend(create_card(1410, 930, 440, 140, "Model Registry & Deployment", [
        "MLflow & Canary Release Pipeline:",
        "• Automated offline GEC benchmark scoring",
        "• Shadow traffic replay against existing models",
        "• 1% Canary live deployment with A/B testing",
        "• Automated zero-downtime GPU rollouts"
    ], bg_color="#ffffff", stroke_color="#d6336c", title_color="#a61e4d", badge="CI/CD Deploy"))

    # ----------------------------------------------------
    # CLEAN, NON-COLLIDING ARROWS
    # ----------------------------------------------------
    # 1. Clients -> Edge (Straight horizontal)
    elements.extend(create_arrow([320, 260], [400, 260], stroke_color="#1971c2", label="HTTPS / WSS", label_above=True))
    elements.extend(create_arrow([320, 380], [400, 380], stroke_color="#7048e8", label="Live Typed Diffs", label_above=True))
    elements.extend(create_arrow([320, 500], [400, 500], stroke_color="#1971c2", label="Doc Sync", label_above=True))

    # 2. Edge -> Processing Pipeline (Straight horizontal)
    elements.extend(create_arrow([660, 260], [740, 260], stroke_color="#7048e8", label="Session Route", label_above=True))
    elements.extend(create_arrow([660, 380], [740, 380], stroke_color="#7048e8", label="Diff Stream", label_above=True))
    elements.extend(create_arrow([660, 510], [740, 510], stroke_color="#7048e8", label="REST Batch", label_above=True))

    # 3. Processing Pipeline -> ML Platform (Straight horizontal)
    elements.extend(create_arrow([1060, 260], [1140, 260], stroke_color="#0ca678", label="gRPC Infer", label_above=True))
    elements.extend(create_arrow([1060, 380], [1140, 380], stroke_color="#0ca678", label="Spell / Rules", label_above=True))
    elements.extend(create_arrow([1060, 510], [1140, 510], stroke_color="#0ca678", label="GEC Deep Infer", label_above=True))
    elements.extend(create_arrow([1060, 650], [1140, 650], stroke_color="#0ca678", label="Tone / LLM", label_above=True))

    # 4. Processing / ML -> Storage (Straight horizontal)
    elements.extend(create_arrow([1440, 260], [1520, 260], stroke_color="#f76707", label="Session Cache", label_above=True))
    elements.extend(create_arrow([1440, 380], [1520, 380], stroke_color="#f76707", label="User Dict / Rules", label_above=True))
    elements.extend(create_arrow([1440, 510], [1520, 510], stroke_color="#f76707", label="Vector Plagiarism", label_above=True))
    elements.extend(create_arrow([1440, 650], [1520, 650], stroke_color="#f76707", label="Doc Versioning", label_above=True))

    # 5. Return suggestions back to Clients (Clean dashed return arrow between Zone 3 and Zone 2)
    elements.extend(create_arrow([740, 420], [660, 420], stroke_color="#0ca678", stroke_style="dashed", label="Suggestions Push", label_above=False))
    elements.extend(create_arrow([400, 420], [320, 420], stroke_color="#7048e8", stroke_style="dashed", label="Underline Annotations", label_above=False))

    # 6. Bottom Flow: User Feedback -> Kafka -> Analytics -> Active Learning -> Model Registry
    elements.extend(create_arrow([200, 810], [200, 930], stroke_color="#d6336c", stroke_style="dashed", label="Accept / Reject Telemetry", label_above=False))
    elements.extend(create_arrow([470, 1000], [510, 1000], stroke_color="#d6336c", label="Stream Aggregation", label_above=True))
    elements.extend(create_arrow([910, 1000], [950, 1000], stroke_color="#d6336c", label="Hard Negatives", label_above=True))
    elements.extend(create_arrow([1370, 1000], [1410, 1000], stroke_color="#d6336c", label="Trained Weights", label_above=True))

    # 7. Model Registry Deploy to Triton (Clean routed multi-point arrow up along the outside right)
    elements.extend(create_multi_point_arrow([
        [1630, 930],
        [1630, 860],
        [1450, 860],
        [1290, 860],
        [1290, 820]
    ], stroke_color="#d6336c", stroke_style="dashed", label="Canary GPU Deploy", label_pos=[1460, 845]))

    # Excalidraw JSON structure
    return {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "viewBackgroundColor": "#f8f9fa",
            "gridSize": None,
            "theme": "light"
        },
        "files": {}
    }

def main():
    excalidraw_data = build_clean_diagram()
    output_path = "~/InterviewPrep/grammarly_hld.excalidraw"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(excalidraw_data, f, indent=2)
    print(f"Generated clean Grammarly HLD diagram with {len(excalidraw_data['elements'])} elements.")

if __name__ == "__main__":
    main()
