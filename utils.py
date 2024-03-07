import urllib.parse

import requests
from bs4 import BeautifulSoup


def fetch_links_from_sitemap(resource_url: str) -> list:
    links = []
    try:
        r = requests.get(urllib.parse.urljoin(resource_url, "/sitemap.xml"), verify=False)
        if r.status_code == 200:
            xml = r.text
            soup = BeautifulSoup(xml)
            for link in soup.findAll("loc"):
                link = link.getText("", True)
                links.append(link)
        else:
            print(f"Fetch urls. Status code: {r.status_code}", r.content)
    except Exception as e:
        print(f"Error on fetching urls: {e}")
    return links
