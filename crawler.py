import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

logging.basicConfig(filename='JTPI_Error.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to fetch {url}: {e}")
        return None

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


def crawl_website(start_url):
    # 방문할 페이지들의 리스트
    to_visit = set([start_url])
    visited = set()

    while to_visit:
        url = to_visit.pop()
        if url not in visited:
            print(f"Visiting: {url}")
            html = fetch_page(url)
            if html:
                # 해당 페이지에서 필요한 정보를 처리
                parse_html(html)  # 여기에 필요한 파싱 로직을 추가
                visited.add(url)
                # 페이지에서 새로운 링크를 찾고 큐에 추가
                links = parse_links(html, url)
                to_visit.update(links - visited)

def parse_html(html):

    soup = BeautifulSoup(html, 'html.parser')

    headers = soup.find_all('h1')
    for header in headers:
        print(header.text)


def main():
    start_url = "https://www.miyakoh.co.jp/rosen/ticket/1day.html" 
    crawl_website(start_url)

if __name__ == "__main__":
    main()
