import requests

class DeepSeekLLM:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.deepseek.com/v1/chat/completions"

    def ask_question(self, question):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": question}]
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}, {response.text}"

# Example usage
if __name__ == "__main__":
    api_key = "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"
    llm = DeepSeekLLM(api_key)
    question = "What is the capital of France?"
    answer = llm.ask_question(question)
    print(answer)

  


