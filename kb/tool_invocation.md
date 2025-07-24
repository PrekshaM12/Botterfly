# Structured JSON for Function Calls

Define a **JSON schema**:

```json
{
  "name": "search_kb",
  "parameters": {
    "type": "object",
    "properties": {
      "query": { "type": "string" }
    },
    "required": ["query"]
  }
}
```

In your prompt: “When relevant, return *only* JSON matching the schema.”
