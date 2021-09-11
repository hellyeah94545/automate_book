#! /usr/bin/env python3
'''
Script to download XKCD comics
'''


import bs4
import requests
import os


url = "https://xkcd.com"
image_tag = "#comic img"
imageDir = "xkcd"

os.makedirs(imageDir, exist_ok=True)
stop_counter = 1

while (not url.endswith("#")) and stop_counter < 11:
    # TODO: Download the page.
    print("Downloading page {0}...".format(url))
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image
    comicElem = soup.select(image_tag)
    if comicElem == []:
        print('Could not find comic image.')
    else:
        imageUrl = url + comicElem[0].get('src')
        print("Downloading image {0}...".format(imageUrl))
        res= requests.get(imageUrl, "html.parser")
        res.raise_for_status()

        # TODO: Download the image
        # TODO: Save the image to ./xkcd
        imgFileName = imageUrl.split("/")[-1]
        imagePath = imageDir + "/" + imgFileName
        imageFile = open(imagePath, 'wb')
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
        imageFile.close()

    # TODO: Get the PREV button's URL
    prevTag = 'a[rel="prev"]'
    prevLink = soup.select(prevTag)[0].get('href')
    baseUrl = "https://xkcd.com/"
    url = baseUrl + prevLink

    stop_counter += 1

print("DONE")