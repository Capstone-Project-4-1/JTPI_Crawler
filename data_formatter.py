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

def checkPass(sclipt):  # 수정 필요
    USER_INPUT_MSG = sclipt
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": [{"type": "text", "text": "너는 사용자가 입력한 정보가 교통패스 정보인지 파악해 대답은 True / False 로만해줘"}]},
            {"role": "user", "content": [{"type": "text", "text": "도쿄 시간표"}]},
            {"role": "assistant", "content": [{"type": "text", "text": "False"}]},
            {"role": "user", "content": [{"type": "text", "text": "도쿄 원데이 패스"}]},
            {"role": "assistant", "content": [{"type": "text", "text": "True"}]},
            {"role": "user", "content": [{"type": "text", "text": "미나미패스"}]},
            {"role": "assistant", "content": [{"type": "text", "text": "True"}]},
            {"role": "user", "content": [{"type": "text", "text": "신주쿠 패스"}]},
            {"role": "assistant", "content": [{"type": "text", "text": "True"}]},
            {"role": "user", "content": [{"type": "text", "text": "KANSAI RAILWAY PASS"}]},
            {"role": "assistant", "content": [{"type": "text", "text": "True"}]},
            {"role": "user", "content": USER_INPUT_MSG}
        ],
        temperature=1,
        max_tokens=34,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content == "True"  # return 값을 bool 타입으로 수정 필요



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
