from bs4 import BeautifulSoup as BS
import requests

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44', 'accept': '*/*'}

# new = 'https://www.hawtcelebs.com/jordan-alexander-at-gossip-girl-season-1-part-2-premiere-in-new-york-11-18-2021/'

def get_pics(new):

    piccs = []
    itts = []

    req = requests.get(new, headers = HEADERS)
    sreq = BS(req.content, 'html.parser')

    if 'hawtcelebs' in new:
        for el in sreq.find_all('a'):
            piccs.append(el.get('href'))
            for pp in piccs:
                if '.jpg' in pp:
                    itts.append(pp)
    elif 'celebmafia' in new:
        for el in sreq.find_all('div', class_='image-gallery'):
            piccs.append(el.find('a').get('href'))
        try:
            for el in sreq.find_all('div', class_='image-box'):
                piccs.append(el.find('a').get('href'))
        except:
            print('no more pics')
        for pp in piccs:
            if '.jpg' in pp:
                itts.append(pp)
    # elif 'gotceleb' in new:
    #     for el in sreq.find_all('dl', class_='gallery-item'):
    #         piccs.append(el.get('href'))
    #         for pp in piccs:
    #             if '.jpg' in pp:
    #                 itts.append(pp)
    else:
        piccs.append('https:')

    items = set(itts)

    # print(items)
    print(len(items))

    return items

# get_pics(new)