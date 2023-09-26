import openai

def generate(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000
        )
    
    return response["choices"][0]["text"]