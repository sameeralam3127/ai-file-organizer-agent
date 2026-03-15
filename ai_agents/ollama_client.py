import ollama

MODEL = "llama3.1:latest"


def ask_llm(messages):

    response = ollama.chat(
        model=MODEL,
        messages=messages,
        format="json"
    )

    return response["message"]["content"].strip()