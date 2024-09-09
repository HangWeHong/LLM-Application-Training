import openai;
openai.api_key="xxx"

completion=openai.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":"Give me 3 fruits name"}])
print(completion.choices[0].message.content)