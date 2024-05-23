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

def checkPass(sclipt):
    USER_INPUT_MSG = sclipt
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 사용자가 입력한 정보에 '패스', '이용권' 등의 단어가 포함되었는지 파악해 대답은 True / False 로만해줘"},
            {"role": "user", "content": USER_INPUT_MSG}
        ],
        temperature=0,
        max_tokens=3,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content == "True"  # return 값을 bool 타입




def formateDate(sclipt): #수정 필요
    MODEL = "gpt-3.5-turbo"
    USER_INPUT_MSG = sclipt
    response = client.chat.completions.create(model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, 
        {"role": "user", "content": USER_INPUT_MSG}, 
        {"role": "assistant", "content": "Who's there?"}, 
    ],
    temperature=0)
    return response.choices[0].message.content #return 값을 리스트형식으로 반환 예정


def dataFormatter(sclipt):
    if(checkPass(sclipt)==True):
        return formateDate(sclipt)
    else:
        return 0




def main():
    print(checkPass("책가방"))
    
if __name__ == "__main__":
    main()
