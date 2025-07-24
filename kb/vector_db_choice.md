# Vector Store Choice for Small Corpora

For < 2 k documents:

| Option    | Setup | Cost | Notes |
| --------- | ----- | ---- | ----- |
| Chroma    | 1-line `pip install chromadb` | Free | Perfect for laptop / serverless. |
| FAISS     | C++ / Rust bindings | Free | Fast, but no persistence. |
| Pinecone  | Easy | $0.10/GB-mo | Overkill until > 50 k docs. |

**Recommendation:** Start with **Chroma**, migrate later if QPS > 50.
