import requests
import json
import ollama

def get_sentiment(text):
    response = requests.post(
        "http://localhost:5001/predict",
        json={"text": text}
    )
    return response.json()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_sentiment",
            "description": "Analyzes the sentiment of text using an ML model",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to analyze"
                    }
                },
                "required": ["text"]
            }
        }
    }
]

messages = [{"role": "user", "content": "Is this review good or bad?: The battery died after 2 hours"}]

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
    print(f"Tool result from Flask: {result}")

    messages.append(message)
    messages.append({
        "role": "tool",
        "content": json.dumps(result)
    })

    final = ollama.chat(model="llama3.1", messages=messages)
    print(f"Agent response: {final['message']['content']}")
else:
    print(message["content"])