#!/usr/bin/env python3
import json

with open("~/InterviewPrep/grammarly_hld.excalidraw", "r", encoding="utf-8") as f:
    diagram_json = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Grammarly HLD - Interactive Excalidraw Diagram</title>
  <style>
    html, body, #root {{
      width: 100%;
      height: 100%;
      margin: 0;
      padding: 0;
      overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}
    .top-bar {{
      position: fixed;
      top: 12px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 100;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border: 1px solid #ced4da;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      border-radius: 24px;
      padding: 6px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 13px;
      color: #343a40;
    }}
    .top-bar strong {{
      color: #1864ab;
    }}
    .top-bar button {{
      background: #1864ab;
      color: #fff;
      border: none;
      padding: 5px 12px;
      border-radius: 14px;
      cursor: pointer;
      font-size: 12px;
      font-weight: 500;
    }}
    .top-bar button:hover {{
      background: #1971c2;
    }}
  </style>
  <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@excalidraw/excalidraw/dist/excalidraw.production.min.js"></script>
</head>
<body>
  <div class="top-bar">
    <span>💡 <strong>Grammarly HLD</strong> • Interactive Excalidraw Canvas</span>
    <button onclick="copyJson()">📋 Copy JSON for Excalidraw.com</button>
    <a href="https://excalidraw.com" target="_blank" style="color: #1864ab; text-decoration: none; font-weight: 500;">Open excalidraw.com ↗</a>
  </div>
  <div id="root"></div>

  <script>
    const diagramData = {diagram_json};

    function copyJson() {{
      navigator.clipboard.writeText(JSON.stringify(diagramData, null, 2)).then(() => {{
        alert("Copied diagram JSON to clipboard! On excalidraw.com, press Cmd+V / Ctrl+V to paste.");
      }}).catch(() => {{
        alert("Please copy from the .excalidraw file.");
      }});
    }}

    const App = () => {{
      return React.createElement(
        "div",
        {{ style: {{ width: "100vw", height: "100vh" }} }},
        React.createElement(ExcalidrawLib.Excalidraw, {{
          initialData: {{
            elements: diagramData.elements,
            appState: {{
              ...diagramData.appState,
              viewBackgroundColor: "#f8f9fa",
              theme: "light"
            }},
            scrollToContent: true
          }},
          UIOptions: {{
            canvasActions: {{
              loadScene: true,
              export: {{ saveFileToDisk: true }},
              saveAsImage: true
            }}
          }}
        }})
      );
    }};

    const root = ReactDOM.createRoot(document.getElementById("root"));
    root.render(React.createElement(App));
  </script>
</body>
</html>
"""

with open("~/InterviewPrep/viewer.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated viewer.html successfully.")
