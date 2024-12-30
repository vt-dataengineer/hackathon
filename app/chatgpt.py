import openai

# Set the API key and organization
openai.api_key = "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"
openai.organization = "org-KdIz0b3zsaisTYS7AXQjFI8v"

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    """
    Communicates with the OpenAI GPT model to generate responses.

    :param prompt: Input prompt for ChatGPT.
    :param model: ChatGPT model to use.
    :return: ChatGPT's response as a string.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        raise RuntimeError(f"ChatGPT API Error: {e}")
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    try:
        response = chat_with_gpt(user_prompt)
        print("\nChatGPT Response:")
        print(response)
    except Exception as e:
        print(f"Error: {e}")
