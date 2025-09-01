from openai import OpenAI

client = OpenAI(
    base_url="https://platform.covenantlabs.ai/api/v1/",
    api_key="698e640d9cb90ac1aaf198a561e8724c51e72c3666eb1196e0ac37e61e17f031"
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