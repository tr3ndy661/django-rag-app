from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key='lm-studio'
)


def ask_llm(question):
    completion = client.chat.completions.create(
    model="qwen2.5-coder-1.5b-instruct",
    messages=[
        {"role": "user", "content": question}
    ],
    temperature=0.7,
    )

    return completion.choices[0].message.content


