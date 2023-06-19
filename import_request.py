import requests
from bs4 import BeautifulSoup
import re

url = 'https://new.ss.ge/en/real-estate/search?realEstateType=5&realEstateDealType=4&cityIdList=95&currencyId=1'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

listings = soup.find_all('div', class_='listing-title')
for listing in listings:
    title = listing.text.strip()
    print(title)
print('------')

base_url = 'https://ss.ge/en/real-estate/'
params = {
    'RealEstateDealTypeId': '4',
    'MunicipalityId': '95',
    'PriceType': 'false',
    'CurrencyId': '1'
}

response = requests.get(base_url, params=params, proxy='')
soup = BeautifulSoup(response.content, 'html.parser')

page_links = soup.find('div', class_='pagination-links')
last_page_link = page_links.find_all('a')[-1]['href']
last_page_number = int(last_page_link.split('=')[-1])

for page in range(1, last_page_number + 1):
    page_url = base_url + f'?Page={page}'
    scrape_page(page_url)


# Determine the number of pages to scrape
response = requests.get(base_url, params=params, proxy='')
soup = BeautifulSoup(response.content, 'html.parser')

page_links = soup.find('div', class_='pagination-links')

if page_links is not None:
    last_page_link = page_links.find_all('a')[-1]['href']
    last_page_number = int(last_page_link.split('=')[-1])
    # Scrape data from each page
    for page in range(1, last_page_number + 1):
        page_url = base_url + f'?Page={page}'
        scrape_page(page_url)
else:
    print("No page links found.")