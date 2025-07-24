# Exposing Rationales Safely

* Ask LLM for `{"answer": "...", "reasoning": "..."}`.  
* Return `answer` to user, store `reasoning` in audit log.  
* Mask secrets in reasoning before logging.
