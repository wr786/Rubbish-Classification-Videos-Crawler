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
pattern = re.compile(r'<a title=(.*?) href=(.*?) target="_blank" class="title">.*?<em class="keyword">.*?</a>')
f = open('fengtai.html','w')
f.write("<html><head><title>枫台</title></head><body><h1>枫台</h1><br/>")
while pagenum <= 10:
    browser.get(url + str(pagenum))
    data = browser.page_source.encode("gbk","ignore").decode("gbk")
    items = re.findall(pattern,data)
    for item in items:
        #f.write(item[0] + "http:" + item[1][1:-2] + '\n')
        f.write("<a href=" + "http:" + item[1][1:-2] + ">" + item[0] + "</a><br/>\n")
    pagenum += 1
browser.close()
browser.quit()
#response = urllib.request.urlopen(url)
#data = response.read().decode('utf-8')
f.write("</body></html>")
f.close()
