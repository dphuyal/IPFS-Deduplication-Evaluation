#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib
import requests
import time
import os

t0 = time.time()


def imageScrapper(link):
    r = requests.get("http://" + link)
    data = r.text

    soup = BeautifulSoup(data, "html.parser")
    soup.find_all('a', {"id": "piclink"})

    for link in soup.find_all("img"):
        if "jpg" in str(link.get("src")):
            img = link.get("src")

    os.chdir('images_5secs/') #images_2secs for 2 secs interval images
    for x in range(183, 1000):
        time.sleep(5)
        images = urllib.request.urlretrieve(img, str(x) + ".jpg")
    print("Done in  %0.3fs." % (time.time() - t0))
    return images


url = input("Enter a website to extract the URL's from: ")
imageScrapper(url)
