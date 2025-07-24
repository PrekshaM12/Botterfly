# Troubleshooting Sudden Latency Increases

Common causes:

1. **Model upgrade** behind the scenes → new weights.  
2. Region saturation—move to **east-us-2** or **eu-west-3**.  
3. Large prompt length (check logs).  
4. Network issues; test with `mtr` to api.openai.com.

Mitigation: enable **timeout retry** and regional fail-over.
