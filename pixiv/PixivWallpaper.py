import urllib.request, urllib.error, urllib.parse
import urllib
import demjson
import json
import requests
import time
import socket


def get_pixiv(url,headers):
    res = requests.get(url=url,headers=headers)
    return res.text



def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()


def login(uasename,password,key,token):
    login_url = 'https://accounts.pixiv.net/api/login?lang=zh'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "Referer": "https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page",
        'user-agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
    }
    body=\
        {
            "pixiv_id":uasename,
            "password":password,
            "post_key":key,
            "source":"pc",
            "ref":"wwwtop_accounts_index",
            "return_to":"https://www.pixiv.net/",
            "recaptcha_v3_token":token
         }
    try:
        res = requests.post(url=login_url, headers=headers, data=body)
        cookie = res.cookies['PHPSESSID']
        return cookie + res.text
    except Exception as err:
        print('获取cookie失败：\n{0}'.format(err))


def SaveImage(url, path):   # 传入的url是图片url地址
    request = urllib.request.Request(url)   # 模拟浏览器头部信息
    request.add_header('accept','image/webp,image/apng,*/*;q=0.8')
    request.add_header('accept-encoding','gzip, deflate, br')
    request.add_header('accept-language','zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6')
    request.add_header('sec-fetch-dest','image')
    request.add_header('sec-fetch-mode','no-cors')
    request.add_header('sec-fetch-site','cross-site')
    request.add_header('referer','https://www.pixiv.net/tags/%E7%BA%B1%E9%9B%BE')
    request.add_header('user-agent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)')
    try:
        response = urllib.request.urlopen(request)  # 打开该url得到响应
        img = response.read()   # read读取出来
        f = open(path, 'wb')    # 以二进制写入的格式打开
        f.write(img)    # 写入
        f.close()       # 关闭
    except urllib.error.URLError as ue:  # 捕获urlerror
        if hasattr(ue, 'code'):  # 如果ue中包含'code'字段, 则打印出来
            print(ue.code)
        if hasattr(ue, "reason"):# 如果ue中包含'reason'字段, 则打印出来
            print(ue.reason)
    except IOError as ie:
        print(ie)


    return 




if __name__ == "__main__":
    cookie = ""
    s = requests.session()
    '''
    s = requests.session()
    cookie = ""
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "Referer": "https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page",
        'user-agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
    }

    headers1 = {
        "content-type": "application/x-protobuffer",
        "Accept": "application/json",
        "Referer": "https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LfJ0Z0UAAAAANqP-8mvUln2z6mHJwuv5YGtC8xp&co=aHR0cHM6Ly9hY2NvdW50cy5waXhpdi5uZXQ6NDQz&hl=zh-CN&v=aUMtGvKgJZfNs4PdY842Qp03&size=invisible&cb=fd0hccv370ud",
        'user-agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
    }
    
    fhStr = s.get("https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page",headers=headers)
    fhStr = fhStr.text
    postKey = getmidstring(fhStr,"postKey\":\"", "\"")
    k = getmidstring(fhStr,"recaptchaV2SiteKey\":\"", "\"")
    k = get_pixiv("https://www.recaptcha.net/recaptcha/api2/reload?k="+k,headers1)
    recaptcha_v3_token = getmidstring(k,"\"rresp\",\"","\"")
    print(k)
    '''
    
    '''
    print(postKey)
    cookie = "PHPSESSID="+login("imcys","imcys19909384476",postKey,recaptcha_v3_token)
    print(cookie)
    '''

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "cookie": cookie,
        "Referer": "https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page",
        'user-agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
    }

    word = input('输入搜索内容')
    p = input('输入抓取页码')

    string = get_pixiv("https://www.pixiv.net/ajax/search/illustrations/"+word+"?word="+word+"&p="+p+"&lang=zh",headers)
    list1 = demjson.decode(string)
    i = 0
    while i < len(list1['body']['illust']['data']) - 1:
        id = list1['body']['illust']['data'][i]['id']
        headers = {
            'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
        }
        s.keep_alive = False # 关闭多余连接
        string = get_pixiv("https://www.pixiv.net/ajax/illust/"+id+"?lang=zh",headers)
        Strjson = demjson.decode(string)
        imgurl = Strjson['body']['urls']['original']
        imgurl = imgurl.replace("i.pximg.net", "i.pixiv.cat")
        print(imgurl)
        name = list1['body']['illust']['data'][i]['title']+id
        print(name)
        path = "F:\下载文件\图片\\"+ name + ".png"
        SaveImage(imgurl, path)
        i= i + 1
        print(i)