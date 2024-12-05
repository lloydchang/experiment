import os
from litellm import completion

# [OPTIONAL] set env var,  replace with your actual key
# os.environ["HUGGINGFACE_API_KEY"] = "your_huggingface_api_key"

messages = [{ "content": "There's a llama in my garden 😱 What should I do?","role": "user"}]

response = completion(
    # model="huggingface/meta-llama/Meta-Llama-3.1-8B-Instruct",
    model="huggingface/Qwen/Qwen2.5-Coder-32B-Instruct",
    messages=[{ "content": "which model are you?","role": "user"}],
    stream=True
)

full_response = ""
try:
    for chunk in response:
        # Access the 'choices' and then the 'delta' to get the text
        if chunk['choices'][0]['delta'].get('content'): # Check if content exists
            text_chunk = chunk['choices'][0]['delta']['content']
            full_response += text_chunk
            print(text_chunk, end="", flush=True)

    print("\n\nFull Response:\n", full_response)
except (KeyError, IndexError) as e:
    print(f"Error processing response: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
