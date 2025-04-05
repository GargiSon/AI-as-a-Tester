from groq import Groq

client = Groq(api_key = "Groq Pass key")
completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[
        {
            "role": "system",
            "content": "Assume you are a industry leading AI trainer. You are also leading AI startups around the world. You are an Indian origin currently giving AI trainings in well known institutes of northern india. You use funny elements during the session."
        },
        {
            "role": "user",
            "content": "Can you explain core concepts of Agnetic AI"
        }
    ],
    temperature=0.7,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

response = completion.choices[0].message
print(response)

    
completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[
        {
            "role": "system",
            "content": """Assume you are AI judge, you need to validate the response based on following prompt.
            
            Give me answer Yes or No in json format."""
        },
        {
            "role": "user",
            "content": """<prompt>Assume you are a industry leading AI trainer. You are also leading AI startups around the world. You are an Indian origin currently giving AI trainings in well known institutes of northern india. You use funny elements during the session.</prompt>
            <response>{response}</response>"""
        }
    ],
    temperature=0.2, #temperature should be low because it is judge have to consider all possibilities
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)


response2 = completion.choices[0].message
print(response2)
