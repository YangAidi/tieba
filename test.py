#!/bin/env python
# -*- coding: utf-8 -*-
# 爬取网上图片,网址：http://tieba.baidu.com/p/3720487356

#导入模块
#import urllib2
import urllib.request
import re
import os
import glob

#设定抓取页数
page_amount = 5

#抓取首页的html代码
def get_page(url):
    req = urllib.request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')      #缺省部分填上浏览器字符串
    response = urllib.urlopen(req)
    html = response.read().decode('utf-8')
    return html

#抓取图片
def read_image(url):
    req = urllib.request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')      #缺省部分填上浏览器字符串
    response = urllib.urlopen(url)
    html = response.read()
    return html


#得到图片列表
def get_picturs_url_list(url):
    html = get_page(url)
    l = re.findall(r'<img class="BDE_Image" pic_type="0" width="\d\d\d" height="\d\d\d" src="(.*?)"',html)
    return l

#下载图片并存储到本地文件夹
def image_save(url,number):
    number = str(number)
    print( '正在抓取第',number,'张')
    filename = number + '.jpg'
    with open(filename,'wb') as fp:
        img = read_image(url)
        fp.write(img)

#准备存放图片的文件夹，并进入到指定路径
def floder_prepare(floder):
    a = glob.glob('*')
    if floder not in a:
        os.mkdir(floder)
    os.chdir(floder)

#主函数
def main():
    number = 5
    l = []
    amount = 0
    for n in range(0,page_amount):
        url = 'http://tieba.baidu.com/p/3720487356?pn=' + str(number-n)
        l += get_picturs_url_list(url)
    floder_prepare('pics_longzhu')
    for url in l:
        amount += 1
        image_save(url,amount)

if __name__ == '__main__':
    main()
    print( '全部抓完啦')