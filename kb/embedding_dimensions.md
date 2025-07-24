# Why 1 536-dimension Embeddings?

* Captures nuanced semantics; ablation shows sharp drop below 512 dims.  
* **Down-project** safely with PCA / SVD to 256 dims for *approximate* search (top-k recall ↓ 3 %).  
* Keep originals for rerank if precision matters.
