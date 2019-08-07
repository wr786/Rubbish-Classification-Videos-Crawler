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
    </style></head><body>')
f.write('<div class="top"><h1 style="font-size:65px;">枫台</h1><img style="width:auto;height:80%;position:relative;top:100%" alt="" src="https://s2.ax1x.com/2019/08/07/e5aGbn.png"></div><br/>')
f.write('<div class="ui four column doubling stackable grid container" id="img-grid" style="margin: 10px">')
while pagenum <= 10:
    browser.get(url + str(pagenum))
    data = browser.page_source.encode("gbk","ignore").decode("gbk")
    items = re.findall(pattern,data)
    for item in items:
        #f.write(item[0] + "http:" + item[1][1:-2] + '\n')
        f.write('<div class="column">' + '<a href="' + "http:" + item[2][1:-2] + '">' + '<ul><li><img class="ui rounded image" alt="" src="http:' + item[0] + '"></li><li>' + item[1][0:35] + "...</li></ul></a></div>\n")
    pagenum += 1
browser.close()
browser.quit()
#response = urllib.request.urlopen(url)
#data = response.read().decode('utf-8')
f.write("</div></body></html>")
f.close()
