import ollama
import json

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_sentiment",
            "description": "Analyzes sentiment of text",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    }
]

def get_sentiment(text):
    return {"sentiment": "positive", "confidence": 0.95}

messages = [{"role": "user", "content": "What is the sentiment of: I love this!"}]

response = ollama.chat(
    model="llama3.1",
    messages=messages,
    tools=tools
)

message = response["message"]

if message.get("tool_calls"):
    tool_call = message["tool_calls"][0]
    args = tool_call["function"]["arguments"]
    result = get_sentiment(args["text"])

    messages.append(message)
    messages.append({
        "role": "tool",
        "content": json.dumps(result)
    })

    final = ollama.chat(model="llama3.1", messages=messages)
    print(final["message"]["content"])
else:
    print(message["content"])