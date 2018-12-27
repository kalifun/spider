# -*- coding:utf-8 -*-
import os
import json
import requests

code_path = os.getcwd()
illustration_url = "https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=illustration&type=hot&page_num="
cos_url = "https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num="
sifu_url = "https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=sifu&type=hot&page_num="

header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'l=v; LIVE_BUVID=AUTO7215458785803635; buvid3=26E51ACA-A5D8-4F10-AF69-EDE200D0404C85388infoc',
    'Host': 'api.vc.bilibili.com',
    'Origin': 'https://h.bilibili.com',
    'Referer': 'https://h.bilibili.com/eden/draw_area',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

def download_pic(username,img_src):
    pic_split = img_src.split('/')
    pic_name = pic_split[-1]
    data = requests.get(img_src)
    img = data.content
    try:
        if data.status_code == 200:
            print "[+] Downloading "+str(img_src)
            with open(str(username)+"/"+str(pic_name),'wb') as f:
                f.write(img)
        else:
            print "[-] ERROR " + str(img_src)
    except Exception,e:
        print e


def mkdir_forder(username,allpic_url):
    mkdir_path = code_path+"/"+str(username)
    try:
        if os.path.exists(mkdir_path):
            for pic_url in allpic_url:
                img_src = pic_url['img_src']
                print img_src
                download_pic(username,img_src)
        else:
            try:
                os.mkdir(mkdir_path)
                for pic_url in allpic_url:
                    img_src = pic_url['img_src']
                    print img_src
                    download_pic(username,img_src)
            except Exception,e:
                print e
    except Exception,e:
        print e


def analysis_json(json_file):
    loads_json = json.loads(json_file)
    for pic_info in loads_json['data']['items']:
        # username = pic_info['user']['name']
        username = pic_info['user']['uid']
        allpic_url = pic_info['item']['pictures']
        mkdir_forder(username,allpic_url)
def get_json(url):
    for i in range(0,25):
        newurl = url+str(i)
        try:
            req = requests.session()
            req.keep_alive = False
            data = req.get(newurl,headers=header)
            json_file = data.text
            analysis_json(json_file)
        except Exception,e:
            print e

if __name__ == "__main__":
    print """
        ------------------------------------------------------------------------
        ------------------------------------------------------------------------
                                    哔哩哔哩相簿
                                      1.ALL
                                      2.Sifu
                                    3.Cosplay
                                  4.Illustration
        ------------------------------------------------------------------------
        ------------------------------------------------------------------------
    """
    chooies_num = raw_input("Please chooies #")
    if int(chooies_num) == 1:
        get_json(sifu_url)
        get_json(cos_url)
        get_json(illustration_url)
    elif int(chooies_num) == 2:
        get_json(sifu_url)
    elif int(chooies_num) == 3:
        get_json(cos_url)
    elif int(chooies_num) == 4:
        get_json(illustration_url)
    else:
        print "Please input 1 or 2 or 3 or 4 !"
