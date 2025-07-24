# Handling OpenAI 429 Rate-Limit Errors

* **Short-term:** exponential back-off (start 200 ms, cap 20 s).  
* **Batch requests** with parallel=true.  
* **Reserve capacity:** request quota increase via dashboard → “Usage” → “Request Increase”.  
* **Long-term:** front a lightweight cache (status, embeddings, retrieval answers).
