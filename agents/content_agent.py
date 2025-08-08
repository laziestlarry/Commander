import openai, os
class ContentAgent:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
    def generate_description(self, topic):
        prompt = f"Write a high-converting, SEO-rich product description for: {topic}"
        r = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role":"user", "content": prompt}]
        )
        return r['choices'][0]['message']['content']
