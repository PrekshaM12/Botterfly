# Integrating the OpenAI Moderation Endpoint

1. Call `POST /v1/moderations` with the candidate reply.  
2. Block or rewrite if any flag probability > 0.2.  
3. Log the category for analytics.  
4. Re-prompt using safer wording (temperature 0).
