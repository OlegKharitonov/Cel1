import os
from Bgetrefs import get_refs
from Ccheckrefs import checknew
from Dgetpics import get_pics
from Sload_pics import loadpic
from Zsaveintxt import save_txt


SITES = [('http://www.hawtcelebs.com', 'Hawtcelebs', 100),
         ('http://www.celebmafia.com', 'Celebmafia', 250),
         ('gotceleb.com', 'Gotceleb', 10)
         ]
# hawt - pages = 1000
# cm - pages
firstpage = 200


for item in SITES[1:2]:
    all_refs = []
    refs = []
    newitems = []
    pages = []
    webpage = item[0]
    path = 'C:/CEL/' + item[1] + '/'
    pathim = path + 'Images/'

    try:
        os.mkdir(path)
    except FileExistsError:
        print('Directory exists')
    os.chdir(path)

    try:
        os.mkdir(pathim)
    except FileExistsError:
        print('Directory exists')

    reffile = path + 'allarticles.txt'
    mistakes = path + 'mistakes.txt'

    if os.path.exists(reffile):
        print('File exists')
    else:
        myfile = open(reffile, 'a+')
        myfile.close()

    if os.path.exists(mistakes):
        print('File exists')
    else:
        myfile = open(mistakes, 'a+')
        myfile.close()

    max_page = item[2]

    # creating of all pages for uploading

    if 'hawtcelebs' in item[0] or 'celebmafia' in item[0]:
        pages = [webpage + '/page/' + str(i) + '/' for i in range(firstpage, max_page+1)]
    elif 'gottceleb' in item[0]:
        pages = [webpage + '/page/' + str(i) for i in range(firstpage, max_page+1)]
    else:
        pages = ''

    print(len(pages))

    # searching for all topics on every page

    for page in pages:
        refs = get_refs(page)
        for r in refs:
            all_refs.append(r)

    newitems = checknew(all_refs, reffile)
    print(f'New items - {len(newitems)}')

    getitems = []
    mistakeitems = []
    items = []

    # search of images for every celeb page

    for new in newitems:
        if 'hawtcelebs' in new:
            newdir = new.split('/')[-2].replace('-', ' ').title().strip()
            newpath = pathim + newdir
        elif 'celebmafia' in new:
            newdir = new.split('/')[-2][0:-7].replace('-', ' ').title().strip()
            newpath = pathim + newdir
        elif 'gotceleb' in new:
            newdir = new.split('/')[-1].replace('.html', '').title().strip()
            newpath = pathim + newdir
        else:
            print('no such new')

        try:
            os.mkdir(newpath)
        except FileExistsError:
            print('Directory exists')

        os.chdir(newpath)

        try:
            items = get_pics(new)
            getitems.append(new)
        except:
            print('Item in mistakes')
            mistakeitems.append(new)

        for pp in items:
            loadpic(pp)

    save_txt(reffile, getitems)
    save_txt(mistakes, mistakeitems)

    print(f'Recorded {len(getitems)}')
    print(f'In mistakes {len(mistakeitems)}')

