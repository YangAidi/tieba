# 爬取贴吧图片

import urllib.request
import re
import os


#获取一页图片
def fetch_pictures(url,t,page):
    #print('页码' + str(page))
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img class="BDE_Image" src="(.*?)"')
    #print(r)
    #print("------------------------------------------------------------------------------------------------------")
    picture_url_list = r.findall(html_content.decode('utf-8'))
    #print(picture_url_list)
    #os.chdir(os.path.join(os.getcwd(), 'pictures'))
    for i in range(len(picture_url_list)):
        picture_name =str(t)+'-'+ str(page)+'-'+str(i) + '.jpg'
        try:
            urllib.request.urlretrieve(picture_url_list[i], picture_name)
            print('页码' + str(page)+":图片链接" + picture_url_list[i])
        except:
            print("Fail to download " + picture_url_list[i])


#获取页码数，执行多少循环
def onetie(url,t):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<span class="red">(.*?)</span>')
    #print(r)
    #print("------------------------------------------------------------------------------------------------------")
    pages = r.findall(html_content.decode('utf-8'))
    #print(pages)
    for page in range(1, int(pages[1])):
        try:
            fetch_pictures(url+'?pn='+ str(page),t, page)
        except:
            break

def main(url):
    html_content = urllib.request.urlopen(url).read()
    #print(html_content)
    #html_content=''
    r = re.compile('"/p/(.*?)\?pid')
    #r = re.compile('<span class="red">(.*?)</span>')
    #print('类型'+str(r))
    #print("------------------------------------------------------------------------------------------------------")
    urlnext = r.findall(html_content.decode('GBK'))
    #print(urlnext)
    for t in range(1, int(urlnext[1])):
        try:
            print('爬取帖子编号'+urlnext[t])
            onetie('http://tieba.baidu.com/p/'+urlnext[t],t)
        except:
            print("帖子异常")
            print(urlnext[t])






if __name__ == '__main__':
    #os.mkdir('pictures')
    path = 'D:\BeautifulPicture2'
    os.chdir(path)
    #onetie('http://tieba.baidu.com/p/4995772159')
    #url='http://tieba.baidu.com/f/search/res?ie=utf-8&kw=哈尔滨商业大学&qw=爆照'
    url = "http://tieba.baidu.com/f/search/res?ie=utf-8&kw=%E5%93%88%E5%B0%94%E6%BB%A8%E5%95%86%E4%B8%9A%E5%A4%A7%E5%AD%A6&qw=%E7%88%86%E7%85%A7&rn=50"
    main(url)
    print('OVER')