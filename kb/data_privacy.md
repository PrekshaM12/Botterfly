# Sending PII through the OpenAI API

* **Allowed:** transient PII if you have the **Enterprise Privacy commitment**.  
* **Not allowed:** highly-sensitive data (SSNs, health records) unless redacted.  
* **Steps:**  
  1. Sign the DPA in Admin → Security Center.  
  2. Enable *Zero-Retention* toggle.  
  3. Tokenise or hash fields where possible.
