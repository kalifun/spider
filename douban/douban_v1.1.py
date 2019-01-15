# -*- coding:utf-8 -*-
import re
import sys
import pygal
import operator
import  requests
from bs4 import BeautifulSoup

reload(sys) 
sys.setdefaultencoding('utf8')

url = "https://movie.douban.com/top250?start="
year_list = []
country_list = []

def create_bar(x,y):
    line_chart = pygal.Bar()
    line_chart.title = 'Movies Yearth'
    line_chart.x_labels = map(str,x)
    line_chart.add('Year', y)
    line_chart.render()
    line_chart.render_to_file('bar.svg')

def count(year_list):
    results = {}
    for i in year_list:
        if i in results:
            results[i] = results[i]+1
        else:
            results[i] = 1
    sorted_result = sorted(results.items(),key=operator.itemgetter(0))
    final_result = dict(sorted_result)
    x = final_result.keys()
    y = final_result.values()
    create_bar(x,y)
def city_count(country_list):
    country_count = {}
    for i in country_list:
        if i in country_count:
            country_count[i] = country_count[i]+1
        else:
            country_count[i] = 1
    
def reload_html(data):
#     readfile = open("moviedata.txt",'rb')
#     soup = BeautifulSoup(readfile,'html.parser')
    soup = BeautifulSoup(data,'html.parser')
    MovieALL=soup.find('ol',attrs={'class':'grid_view'})
    for MovieList in MovieALL.find_all('li'):
        top_num = MovieList.find(name='em').string
        print top_num
        title = MovieList.find_all(name='span',class_='title')
        chiness_name = title[0].string
        print chiness_name
        class_bd = MovieList.find(name='div',class_='bd').getText()
        MovieInfo = class_bd.split("\n")[3]
        # MovieYearth = re.findall(r'\d{4}',str(class_bd[1]))[0]
        MovieYearth_All = MovieInfo.split("/")[0]
        MovieYearth = re.findall(r'\d{4}',MovieYearth_All)[0]
        MovieCountry = MovieInfo.split("/")[1]
        MovieCountry_split = MovieCountry.split()
        for country in MovieCountry_split:
            country_list.append(country)
        MovieType = MovieInfo.split("/")[2].replace(" ",",")
        print MovieType
        year_list.append(int(MovieYearth))
        

def get_html(douban_url):
    req = requests.get(douban_url)
    data = req.text
    reload_html(data)
#     outputfile=open("moviedata.txt",'wb')
#     outputfile.write(data)
#     reload_html()

if __name__ == "__main__":
    start = 0
    for i in range(10):
        douban_url = url+str(start)
        print douban_url
        get_html(douban_url)
        start += 25
    #print year_list
    city_count(country_list)
    #count(year_list)
    # print year_list
    