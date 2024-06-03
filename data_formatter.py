#use gpt-3.5 turbo api for data format
from openai import OpenAI


class Formatter :
    def __init__(self,api_key):
        self.client = OpenAI(api_key=api_key)
        
    #TEST Connect API
    def testAPI(self):
        MODEL = "gpt-3.5-turbo"
        USER_INPUT_MSG = "안녕"
        response = self.client.chat.completions.create(model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": USER_INPUT_MSG}, 
            {"role": "assistant", "content": "Who's there?"},
        ],
        temperature=0)
        return response.choices[0].message.content
    
    def checkPass(self,sclipt): 
        USER_INPUT_MSG = sclipt
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You need to determine if the user's input contains terms related to travel passes for tourists such as 'day pass', 'ride pass', 'ticket', 'one-day pass', 'three-day pass', 'five-day pass', 'tourist', 'visitor', 'sightseeing', etc. If it contains terms related to local residents or senior citizens such as 'senior pass', 'resident pass', etc., respond with 'False'. If it contains any tourist pass terms, respond with 'True'. Otherwise, respond with 'False'."},
                {"role": "user", "content": USER_INPUT_MSG}
            ],
            temperature=0,
            max_tokens=3,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content == "True"  # return 값을 bool 타입

    def formateDate(self,sclipt): #수정 필요
        MODEL = "gpt-3.5-turbo"
        USER_INPUT_MSG = sclipt
        response = self.client.chat.completions.create(model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}, 
            {"role": "user", "content": USER_INPUT_MSG}, 
            {"role": "assistant", "content": "Who's there?"}, 
        ],
        temperature=0)
        return response.choices[0].message.content #return 값을 리스트형식으로 반환 예정


    def dataFormatter(self,sclipt): #필요없을듯 삭제 예정 
        if(self.checkPass(sclipt)==True):
            return self.formateDate(sclipt)
        else:
            return 0
        