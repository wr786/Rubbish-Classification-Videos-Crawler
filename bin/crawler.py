#author:wr786
#-*- coding:utf-8 -*- 
import urllib.request
import re
import os
import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  
browser = webdriver.Chrome(abspath)

url = "http://search.bilibili.com/all?keyword=%E5%9E%83%E5%9C%BE%E5%88%86%E7%B1%BB&page="
pagenum = 1
pattern = re.compile(r'<div class="lazy-img"><img alt="" src="(.*?)"></div>.*?<a title=(.*?) href=(.*?) target="_blank" class="title">.*?<em class="keyword">.*?</a>')
f = open('fengtai.html','w')
f.write('<html><head><title>枫台</title>\
    <link rel="stylesheet" type="text/css" href="https://cdn.bootcss.com/semantic-ui/2.2.13/semantic.min.css">\
    <style type="text/css">\
    img{width: 200px;height: 120px;top:50%;position: relative;}\
    .top{top:-40px;color:black;height:100px;background-color:grey;border:black;}\
     ul li{list-style-type:none;}\
    a:link {color: white; text-decoration:none;}a:active:{color: red; } a:visited {color:white;text-decoration:none;} a:hover {color:red; text-decoration:underline;}\
    </style></head><body>')
#f.write('<div class="top"><h1 style="font-size:65px;">枫台</h1><img style="width:auto;height:80%;position:relative;top:100%" alt="" src="https://s2.ax1x.com/2019/08/07/e5aGbn.png"></div><br/>')
f.write('<div class="pusher">\
        <div class="ui inverted vertical masthead center aligned segment">\
            <div class="ui container">\
                <div class="ui large secondary inverted pointing menu">\
                    <a class="active item">bilibili</a>\
                    <a class="item" href=".\\zhihu.html">知乎</a>\
                    <div class="right item">\
                        <a class="ui inverted button" target="_blank" href="">枫台</a>\
                    </div>\
                </div>\
            </div>')                        #UI Originally designed by @lin714093880
f.write('<div class="ui four column doubling stackable grid container" id="img-grid" style="margin: 10px">')
while pagenum <= 10:#可自定义页数
    browser.get(url + str(pagenum))
    data = browser.page_source.encode("gbk","ignore").decode("gbk")
    items = re.findall(pattern,data)
    for item in items:
        #f.write(item[0] + "http:" + item[1][1:-2] + '\n')
        f.write('<div class="column">' + '<a href="' + "http:" + item[2][1:-2] + '">' + '<ul><li><img class="ui rounded image" alt="" src="http:' + item[0] + '"></li><li>' + item[1][0:35] + "...</li></ul></a></div>\n")
    pagenum += 1
f.write("</div></body></html>")
f.close()
f2 = open('zhihu.html','w')
f2.write('<html><head><title>枫台</title>\
    <link rel="stylesheet" type="text/css" href="https://cdn.bootcss.com/semantic-ui/2.2.13/semantic.min.css">\
    <style type="text/css">\
    img{width: 200px;height: 120px;top:50%;position: relative;}\
    .top{top:-40px;color:black;height:100px;background-color:grey;border:black;}\
     ul li{list-style-type:none;}\
    a:link {color: white; text-decoration:none;}a:active:{color: red; } a:visited {color:white;text-decoration:none;} a:hover {color:red; text-decoration:underline;}\
    </style></head><body>')
f2.write('<div class="pusher">\
        <div class="ui inverted vertical masthead center aligned segment">\
            <div class="ui container">\
                <div class="ui large secondary inverted pointing menu">\
                    <a class="item" href=".\\fengtai.html">bilibili</a>\
                    <a class="active item">知乎</a>\
                    <div class="right item">\
                        <a class="ui inverted button" target="_blank" href="">枫台</a>\
                    </div>\
                </div>\
            </div>')
url = "https://www.zhihu.com/search?type=content&q=%E5%9E%83%E5%9C%BE%E5%88%86%E7%B1%BB"
browser.get(url)
data2 = browser.page_source.encode("gbk","ignore").decode("gbk")
pattern2 = re.compile(r'<meta itemprop="url" content="(.*?)">.*?<meta itemprop="name" content="(.*?)">.*?<span class="RichText ztext CopyrightRichText-richText" itemprop="text"><b>(.*?)</b>：(.*?)</span>')
items = re.findall(pattern2,data2)
for item in items:
    f2.write('<a href="' + item[0] + '"<p style="font-size:28px;color:white;">' + item[1] + '</p>' + '<p style="font-size:12px;color:white;">' + item[2] + ':' + item[3] + '</p></a><br/>\n')
#response = urllib.request.urlopen(url)
#data = response.read().decode('utf-8')
browser.close()
browser.quit()
f2.write("</div></body></html>")
f2.close()
