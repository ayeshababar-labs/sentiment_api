from groq import Groq

client = Groq()  # automatically picks up GROQ_API_KEY from environment

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "What is sentiment analysis? Answer in 2 sentences."}
    ]
)

print(response.choices[0].message.content)