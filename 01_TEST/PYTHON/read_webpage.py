import requests
from bs4 import BeautifulSoup

def get_page_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # 안전하게 추출
    title = soup.title.string if soup.title else None

    desc_tag = soup.find('meta', attrs={'name': 'description'})
    meta_description = desc_tag['content'] if desc_tag and 'content' in desc_tag.attrs else None

    keyword_tag = soup.find('meta', attrs={'name': 'keywords'})
    keywords = keyword_tag['content'] if keyword_tag and 'content' in keyword_tag.attrs else None

    return title, meta_description, keywords


def print_page_info(title, meta_description, keywords):
    print("Title:", title)
    print("Meta Description:", meta_description)
    print("Keywords:", keywords)


if __name__ == '__main__':
    url = "https://www.google.com"
    title, meta_description, keywords = get_page_info(url)
    print_page_info(title, meta_description, keywords)