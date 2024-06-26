import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

logging.basicConfig(filename='JTPI_Error.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Crawler:
    def __init__(self) -> None:
        pass

    @staticmethod
    def fetch_page(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"Failed to fetch {url}: {e}")
            return None
   
    @staticmethod
    def parse_links(html, base_url):
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for link in soup.find_all('a', href=True):
            full_url = urljoin(base_url, link['href'])
            parsed_url = urlparse(full_url)
            clean_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path  # 쿼리 및 앵커 제거
            if parsed_url.netloc == urlparse(base_url).netloc:
                links.add(clean_url)
        return links


    def crawl_website(self,start_url, max_depth = 2):
        # 방문할 페이지들의 리스트
        to_visit = [(start_url,0)] #Url과 깊이
        link_content_dict= {}
        visited = set()

        while to_visit:
            url,depth = to_visit.pop(0)
            if depth > max_depth:
                logging.info(f"Reached maximum depth at {url}")
                continue

            if url not in visited:
                print(f"Visiting: {url}")
                html = self.fetch_page(url)
                logging.info(f"Visiting {url} at depth {depth}")
                if html:
                    # 해당 페이지에서 필요한 정보를 처리
                    link_content_dict[url] =self.parse_html(html) # 여기에 필요한 파싱 로직을 추가
                    visited.add(url)
                    if depth < max_depth:
                        links = self.parse_links(html, url)
                        for link in links:
                            if link not in visited: # 페이지에서 새로운 링크를 찾고 큐에 추가
                                to_visit.append((link, depth + 1))

        print("Finsih")
        logging.info(f"Finshi")
        return link_content_dict

    @staticmethod
    def parse_html(html):
        content =""
        soup = BeautifulSoup(html, 'html.parser')
        headers = soup.find_all("h2")
        for header in headers:
            content = content + header.text+"/"
        return content



def main():
    #start_url = "https://www.miyakoh.co.jp/rosen/ticket/1day.html" 
    start_url = "https://www.surutto.com/kansai_rw/ko/krp.html"
    crawler = Crawler()
    print(crawler.crawl_website(start_url,1))
if __name__ == "__main__":
    main()
