import requests

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44', 'accept': '*/*'}

# pp = 'https://www.hawtcelebs.com/wp-content/uploads/2021/11/jordan-alexander-at-gossip-girl-season-1-part-2-premiere-in-new-york-11-18-2021-1.jpg'

def loadpic(pp):

    try:
        filename = pp.split('/')[-1].strip()
        image = pp
        im_file = open(filename, 'wb')
        p = requests.get(image, headers=HEADERS)
        im_file.write(p.content)
        im_file.close()
    except:
        print('Error image')

#
# loadpic(pp)]