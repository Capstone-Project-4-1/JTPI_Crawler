from dotenv import load_dotenv
import os
import data_formatter as df
import crawler as cr
import logging

logging.basicConfig(filename='JTPI_Error.log', filemode='a', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# APIKEY
OpenAI_API_KEY = os.environ.get('OpenAI_API_KEY')

# test data_formatter.py
def test_formatter():
    formatter = df.Formatter(OpenAI_API_KEY)
    print(formatter.testAPI())
    
# test crawler.py    
def test_crawler():
    site_url =[]
    start_url = "https://www.miyakoh.co.jp/rosen/ticket/index.html" 
    crawler = cr.Crawler()
    url_content = crawler.crawl_website(start_url,1).copy()
    for url,content in url_content.items():
        print(url+" : "+content)
        site_url.append(url)
    
    for fetched_url in site_url:
        print(fetched_url+" : "+crawler.parse_html_ALL(fetched_url))
    
        

        
# test integration data_formatter & crawler
def test_integrate():
    site_url=[]
    formatter = df.Formatter(OpenAI_API_KEY)
    print(formatter.testAPI())
    start_url = "https://www.miyakoh.co.jp/rosen/ticket/index.html" 
    crawler = cr.Crawler()
    url_content = crawler.crawl_website(start_url,1).copy()
    for url,content in url_content.items():
        check_pass = formatter.checkPass(content)
        print(url+" : ",check_pass) #True인 경우 다 긁어와서 포맷형식에 맞추는 방법으로 실행 
        if check_pass:
            site_url.append(url)
    for fetched_url in site_url:
        print(fetched_url+" : "+crawler.parse_html_ALL(fetched_url))
    
    
    
        

def main():
    test_integrate()
    #test_crawler()
if __name__ == "__main__":
    main()
