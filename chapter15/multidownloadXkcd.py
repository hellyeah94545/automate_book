#! /usr/bin/env python3
# multidownloadXkcd.py: Multi threaded downloader from XKCD comics

import requests
import bs4
import os
import threading

os.makedirs('xkcd2', exist_ok=True)


def downloadXkcd(startComic, endComic):
    url = "https://xkcd.com/"
    image_tag = "#comic img"
    for urlNumber in range(startComic, endComic):
        print("Downloading page http://xkcd.com/%s..." % (urlNumber))
        res = requests.get(url + str(urlNumber), 'html.parser')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features='lxml')

        comicElem = soup.select(image_tag)
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = url + comicElem[0].get('src')
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl, 'html.parser')
            res.raise_for_status()

            imageFile = open(os.path.join('xkcd2', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# TODO: Create and start the Thread objects.
downloadThreads = []
for i in range(2000, 2500, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()
# TODO: Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
#downloadXkcd(2502, 2503)
