# Adding Spanish & French Responses

1. Detect user language with `langdetect`.  
2. If not English → translate incoming question to English (`fasttext+argos`).  
3. Run normal pipeline.  
4. Translate answer back.  
Cost: ~0.2¢ extra per request using LibreTranslate self-hosted.
