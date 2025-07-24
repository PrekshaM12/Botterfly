# 🦋 Botterfly

**Botterfly is a fully-local AI help-desk assistant** that turns any folder of Markdown FAQs into instant answers.  
No cloud calls, no API keys required—everything runs on-device using open-source models.

|                           | |
|---------------------------|----------------------------------------------------------------|
| **Tech stack**           | MiniLM sentence-transformer · ChromaDB · Llama 2-7B (Ollama) · LangChain Core |
| **Runs on**              | macOS / Linux laptop with ≥ 8 GB RAM (Apple Silicon or x86)     |
| **Latency**              | ~400–800 ms end-to-end on an M-series Mac                       |
| **Cost**                 | **\$0** (all models are free & local)                          |

---

## ✨ Features

* **Offline RAG** – embeds your Markdown docs with MiniLM (Hugging Face) and stores vectors in Chroma.
* **Confidence gate** – skips replies when similarity distance > 1.3 to avoid hallucinations.
* **Concise answers** – prompt limits to ≤ 45 words, perfect for chat or desktop pop-ups.
* **Swappable LLM** – default is `llama2:7b`; drop in `mistral:7b` or `llama2:13b` by editing one line.
* **100 % open source** – no telemetry, no hidden keys.

---

## 🚀 Quick start

```bash
# 1  Clone repo & enter
git clone https://github.com/your-user/botterfly.git
cd botterfly

# 2  Create Python venv
python3 -m venv .venv
source .venv/bin/activate

# 3  Install deps
pip install -r requirements.txt   # langchain-core, langchain-huggingface, chromadb, sentence-transformers

# 4  Install Ollama & pull the LLM
brew install ollama               # or download the .dmg from ollama.ai
ollama pull llama2:7b

# 5  Embed your knowledge base
python scripts/embed_kb.py        # reads every *.md in kb/ and builds chroma_store/

# 6  Chat in Terminal
python scripts/process_ticket.py
