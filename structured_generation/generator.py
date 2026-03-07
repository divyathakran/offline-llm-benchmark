import ollama


def generate_structured(model, prompt, temperature=0):

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": temperature}
    )

    return response["message"]["content"]