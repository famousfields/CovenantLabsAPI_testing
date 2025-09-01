from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("COVENANT_API_KEY")

client = OpenAI(
    base_url="https://platform.covenantlabs.ai/api/v1/",
    api_key=api_key
)

def useAPI():
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-1B-Instruct",
        messages = [
        {
            "role": "system",
            "content": (
                "You are an AI that extracts structured data from user messages. "
                "Your output must always be in JSON format with the fields: "
                "`greeting`, `mood`, and `name` (if any). "
                "If a field isn't present, set it to null."
            ),
        },
        {
            "role": "user",
            "content": "Hello, how are you? My name is Sarah and I'm Happy.",
        },
    ]
        
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    response = useAPI()

    print("response was:", response)