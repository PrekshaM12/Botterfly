# Choosing the right OpenAI model for summarisation

**Recommendation:** Use **GPT-4o-mini** for production summaries of long legal briefs.

| Model          | Tokens/sec† | Quality (human eval) | Cost / 1k tokens |
| -------------- | ---------- | -------------------- | ---------------- |
| GPT-3.5-turbo  | ~80        | Good                 | $0.50 input / $1.50 output |
| GPT-4o-mini    | ~45        | *Very good*          | $1.00 / $2.00 |
| GPT-4-turbo    | ~15        | Excellent            | $5.00 / $15.00 |

†Measured in our staging env, context ≈ 8 k tokens.

**Why GPT-4o-mini?**

* Handles 128 k-token contexts—perfect for 10-page (≈ 7 k tokens) docs.  
* Hallucination rate ↓ 40 % vs GPT-3.5 (internal eval).  
* 3× cheaper than GPT-4-turbo, still within SLA latency.

**Implementation tips**

1. **Chunk** the brief → overlap 20 %.  
2. **System prompt:** “You are a legal analyst who writes 200-word concise summaries…”  
3. **Post-process:** run through the moderation endpoint.
