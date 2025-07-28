import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def find_forms(url):
    forms = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for form in soup.find_all("form"):
            forms.append(form)
    except Exception as e:
        print(f"[!] Failed to crawl {url} - {e}")
    return forms

def get_all_links(url):
    urls = set()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for a_tag in soup.find_all("a"):
            href = a_tag.get("href")
            if href and href.startswith("/"):
                full_url = urljoin(url, href)
                urls.add(full_url)
            elif href and href.startswith("http"):
                urls.add(href)
    except Exception as e:
        print(f"[!] Failed to get links from {url} - {e}")
    return list(urls)
