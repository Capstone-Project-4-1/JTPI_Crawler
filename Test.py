import data_formatter as df
from dotenv import load_dotenv
import os

# APIKEY
OpenAI_API_KEY = os.environ.get('OpenAI_API_KEY')



def main():

    formatter = df.Formatter(OpenAI_API_KEY)
    print(formatter.testAPI())
    
if __name__ == "__main__":
    main()
