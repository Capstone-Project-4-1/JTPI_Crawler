import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def fetch_page(url):
    # 웹 페이지에서 HTML을 가져온다
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_links(html, base_url):
    # 주어진 HTML에서 모든 링크를 파싱하고 정규화
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for link in soup.find_all('a', href=True):
        full_url = urljoin(base_url, link['href'])
        if urlparse(full_url).netloc == urlparse(base_url).netloc:  
            links.add(full_url)
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
    start_url = "https://example.com" 
    crawl_website(start_url)

if __name__ == "__main__":
    main()
