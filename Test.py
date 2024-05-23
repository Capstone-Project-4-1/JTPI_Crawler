from dotenv import load_dotenv
import os
import data_formatter as df
import crawler as cr


# APIKEY
OpenAI_API_KEY = os.environ.get('OpenAI_API_KEY')

# test data_formatter
def test_formatter():
    formatter = df.Formatter(OpenAI_API_KEY)
    print(formatter.testAPI())
    
def test_crawler():
    start_url = "https://www.miyakoh.co.jp/rosen/ticket/1day.html" 
    crawler = cr.Crawler()
    url_content = crawler.crawl_website(start_url,1).copy()
    for url,content in url_content.items():
        print(url+" : "+content)
        
    
def test_integrate():
    formatter = df.Formatter(OpenAI_API_KEY)
    print(formatter.testAPI())
    start_url = "https://www.miyakoh.co.jp/rosen/ticket/1day.html" 
    crawler = cr.Crawler()
    url_content = crawler.crawl_website(start_url,1).copy()
    for url,content in url_content.items():
        print(url+" : ",formatter.checkPass(content))
        


def main():
    test_integrate()

if __name__ == "__main__":
    main()
