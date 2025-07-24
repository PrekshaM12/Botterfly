# Reducing hallucinations in conversational agents

1. **Ground every answer** with Retrieval-Augmented Generation (RAG).  
2. **Explicitly instruct:** “If you are unsure, say ‘I don’t know’.”  
3. Use **temperature ≤ 0.3** for factual responses.  
4. Log queries with hallucination tags; retrain retrieval index weekly.  
5. Consider **tool calls**—let the model fetch facts instead of guessing.
