from groq import Groq
import json

client = Groq()

# Define a fake tool
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_sentiment",
            "description": "Analyzes the sentiment of a given text",
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

# Fake tool implementation
def get_sentiment(text):
    return {"sentiment": "positive", "confidence": 0.95}  # hardcoded for now

# Agent loop
messages = [{"role": "user", "content": "What is the sentiment of: I love this!"}]

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

# Check if model wants to call a tool
if message.tool_calls:
    tool_call = message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    
    # Call the actual function
    result = get_sentiment(args["text"])
    
    # Send result back to model
    messages.append(message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result)
    })
    
    # Get final response
    final = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages
    )
    print(final.choices[0].message.content)
else:
    # Model answered directly without calling a tool
    print(message.content)