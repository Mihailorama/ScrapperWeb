"""
Script for comparing scraper results and the target site's sitemap.

Command example: python check_scraper.py <path_to_site_sitemap> <target_scraper_data_name>(e.g. eng).

The result is two files. A list of URLs that are not in the scraper and a list of URLs that are not on the site.
"""

from bs4 import BeautifulSoup
import requests
import sys

scraper_url = "http://128.199.204.216/load_data"
result_file_site = "check_result_site.txt"
result_file_scraper = "check_result_scraper.txt"
target_url = sys.argv[1]
target_scraper_data_name = sys.argv[2]


def get_urls_of_xml(xml_url):
    links = []
    r = requests.get(xml_url)
    if r.status_code == 200:
        xml = r.text
        soup = BeautifulSoup(xml)
        for link in soup.findAll("loc"):
            link = link.getText("", True)
            links.append(link)
    else:
        print(f"Status code: {r.status_code}", r.content)
    return links


def get_url_from_scraper_data():
    request_data = {
        "name": target_scraper_data_name
    }
    r = requests.post(scraper_url, json=request_data)

    res = []
    if r.status_code == 200:
        data = r.json()
        for page in data:
            res.append(page.get("metadata").get("source"))
    else:
        print(f"Status code: {r.status_code}", r.content)

    return res


print(f"Make a call to {target_url}")
links_data_arr = get_urls_of_xml(target_url)
print(f"Parsed {len(links_data_arr)} links from the site")

print(f"Make a call to scraper ({scraper_url} {target_scraper_data_name})")
scraper_links = get_url_from_scraper_data()
print(f"Parsed {len(scraper_links)} links from the scraper")

diff_site = set(links_data_arr).difference(scraper_links)
with open(result_file_site, "w") as f:
    for line in diff_site:
        f.write(f"{line}\n")

diff_scraper = set(scraper_links).difference(links_data_arr)
with open(result_file_scraper, "w") as f:
    for line in diff_scraper:
        f.write(f"{line}\n")

print(f"Number of links that are not in the scraper (saved to {result_file_site}): {len(diff_site)}")
print(f"Number of links that are not on the site (saved to {result_file_scraper}): {len(diff_scraper)}")
