# Switching to GPT-4o-mini

* API path unchanged—just set `model="gpt-4o-mini"`.  
* Context window 128 k (vs 64 k).  
* Slightly different tokenisation—rerun embeddings.  
* Cost-per-token 60 % lower; latency ~3× faster.

Rollback: keep env var `DEFAULT_MODEL`; update in one place.
