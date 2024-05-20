#use gpt-3.5 turbo api for data format
from dotenv import load_dotenv
import os
from openai import OpenAI

# APIKEY
OpenAI_API_KEY = os.environ.get('OpenAI_API_KEY')
client = OpenAI(api_key=OpenAI_API_KEY)

#TEST
def testAPI():
    MODEL = "gpt-3.5-turbo"
    USER_INPUT_MSG = "안녕"
    response = client.chat.completions.create(model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": USER_INPUT_MSG}, 
        {"role": "assistant", "content": "Who's there?"},
    ],
    temperature=0)

    return response.choices[0].message.content

def main():
    print(testAPI())
if __name__ == "__main__":
    main()
