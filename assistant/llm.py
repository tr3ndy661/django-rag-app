from openai import OpenAI
import json


client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key='lm-studio'
)


def ask_llm(question, context):
    completion = client.chat.completions.create(
    model="qwen2.5-coder-1.5b-instruct",
    messages=[
            {"role": "user", "content": f"Using the following information: {context}\n\nAnswer this question: {question}"}
    ],
    temperature=0.7,
    tools = [
        {
            "type": "function",
            "function": {
                "name": "check_order_status",
                "description": "checks the order status and details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "order number"
                        }
                    },
                    "required": ["order_id"]
                }
            }
        }
    ]
    )

    message = completion.choices[0].message.content

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        order_id = args['order_id']
        result = check_order_status(order_id)
        return result
    else :
        return message.content


