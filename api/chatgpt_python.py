import os
from openai import OpenAI # type: ignore

# Crear cliente usando la nueva API de OpenAI
client = OpenAI(api_key="API_KEY_HERE")

while True:
    prompt = input("\nIntroduce una pregunta: ")
    
    if prompt.lower() == "exit":
        break
    
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048
    )
    
    print(chat_completion.choices[0].message.content)
