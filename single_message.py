import openai

API_KEY = open("API_KEY", "r").read()

openai.api_key = API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that translates English to French."},
        {"role": "user", "content": "How do I say hello in French?"},
        {"role": "assistant", "content": "Hello in French is Bonjour."},
        {"role": "user", "content": "How do I say I love artificial intelligence in French?"}
    ]
)

print(response)