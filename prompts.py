# from openai import OpenAI
# from groq import Groq
# from dotenv import load_dotenv
# import os
# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")
# client = Groq(api_key=api_key)  
# llm_model="llama-3.3-70b-versatile"  
# response = client.chat.completions.create(
#     model=llm_model,
#     messages=[
#         {
#             "role": "user",
#             "content": "Say hello in one sentence."
#         }
#     ]
# )

# print(response.choices[0].message.content)
