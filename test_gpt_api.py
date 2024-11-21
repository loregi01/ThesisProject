from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    api_key = OPENAI_API_KEY,
)

query = "Who is the father of Luigi?"

completion = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Translate this natural language query in Prolog: {query}"},
    ]
)

print(completion.choices[0].message.content.strip())


