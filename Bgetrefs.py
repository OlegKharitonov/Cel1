from bs4 import BeautifulSoup as BS
import requests

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44', 'accept': '*/*'}


def get_refs(page):

    refs = []

    req = requests.get(page, headers = HEADERS)
    sreq = BS(req.content, 'html.parser')

    if 'hawtcelebs' in page:
        for el in sreq.find_all('a', class_='post-entry'):
            refs.append(el.get('href'))
    elif 'celebmafia' in page:
        for el in sreq.find_all('a', class_='entry-title-link'):
            refs.append(el.get('href'))
    elif 'gotceleb' in page:
        for el in sreq.find_all('div', class_='post-thumbnail-big'):
            refs.append(el.get('href'))
    else:
        refs.append('https:')

    refs = set(refs)

    return refs
