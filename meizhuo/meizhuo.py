# -*- coding:utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup


def analysispic(pic_url):
    req_data = requests.get(pic_url)
    Album_data = req_data.text
    get_album = BeautifulSoup(Album_data,'html.parser')
    album_url = get_album.find(name='ul',class_='scroll-img clearfix')
    for album_img in album_url.find_all('img'):
        original_pic = album_img.get("data-original")
        newpic = original_pic.replace("_120_80","")
        pic_split = newpic.split('/')
        pic_name = pic_split[-1]
        img_data = requests.get(newpic)
        img = img_data.content
        with open(str(pic_name),'wb') as f:
            f.write(img)

def getalbum(pageurl):
    pagedata = requests.get(pageurl)
    getpagedata = pagedata.text
    soup = BeautifulSoup(getpagedata,'html.parser')
    AllUrl = soup.find(name='div',class_='tab_box')
    for analysisurl in AllUrl.find_all('a'):
        pic_url =  analysisurl.get("href")
        analysispic(pic_url)   



def analysishtml(url):
    data = requests.get(url)
    getdata = data.text
    soup = BeautifulSoup(getdata,'html.parser')
    Pagenum = soup.find(name='div',class_='pages')
    for page in Pagenum.find_all('a'):
        pageurl = page.get('href')
        getalbum(pageurl)
    AllUrl = soup.find(name='div',class_='tab_box')
    for analysisurl in AllUrl.find_all('a'):
        pic_url =  analysisurl.get("href")
        analysispic(pic_url)

    
if __name__ == "__main__":
    url = "http://www.win4000.com/wallpaper_192_0_7_1.html"
    analysishtml(url)