# -*- conding:utf-8 -*-
import re
import requests 
from bs4 import BeautifulSoup

def analysis(data):
    soup = BeautifulSoup(data,'html.parser')
    all_content = soup.find(name='ol',class_='grid_view')
    all_movies = all_content.find_all(name='li')
    for single in all_movies:
        top_num = single.find(name='em').string
        title = single.find_all(name='span',class_='title')
        chiness_name = title[0].string
        class_bd = single.find(name='div',class_='bd').contents
        movie_yearth = re.findall(r'\d{4}',str(class_bd[1]))[0]
        movie_rating = re.findall(r'\d?\.\d',str(class_bd[3]))[0]
        movie_country = re.findall(r'\d{4}.*$/',str(class_bd[1]))
        movie_eval = class_bd[3].find_all(name='span')[-1]  
def get_html(url):
    try:
        req = requests.get(url)
        req.decoding = 'utf-8'
        if req.status_code == 200 :
            data = req.text
            print data
            analysis(data)
        else:
            print "[-] "+url +" error" 
    except Exception,e:
        print e
if __name__ == "__main__":
    douban_url = "https://movie.douban.com/top250"
    get_html(douban_url)