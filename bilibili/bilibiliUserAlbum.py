
import urllib.request, urllib.error, urllib.parse
import urllib
import demjson
import requests
import time



def SaveImage(url, path):   # 传入的url是图片url地址
    request = urllib.request.Request(url)   # 模拟浏览器头部信息
    request.add_header('accept','image/webp,image/apng,*/*;q=0.8')
    request.add_header('accept-encoding','gzip, deflate, br')
    request.add_header('accept-language','zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6')
    request.add_header('sec-fetch-dest','image')
    request.add_header('sec-fetch-mode','no-cors')
    request.add_header('sec-fetch-site','cross-site')
    request.add_header('referer','https://search.bilibili.com/')
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

if __name__ == "__main__" :
    headers = {
        'referer':'https://search.bilibili.com/',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
        'Cookie': '1'
    }
    UID = "6823116"
    getCountUrl = "https://api.vc.bilibili.com/link_draw/v1/doc/upload_count?uid=" + UID
    getCountJson = requests.get(getCountUrl,headers=headers).text
    CountJson = demjson.decode(getCountJson)
    all_count = CountJson['data']['all_count']
    getAlbumUrl = "https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid="+UID+"&page_num=0&page_size="+str(all_count)+"&biz=all"
    getAlbumJson = requests.get(getAlbumUrl,headers=headers).text
    AlbumJson = demjson.decode(getAlbumJson)
    AlbumList = AlbumJson['data']['items']
    a = 0
    while a < len(AlbumList):
        ImgList = AlbumJson['data']['items'][a]['pictures']
        ImgTitle = AlbumJson['data']['items'][a]['description']
        if (len(ImgList)==0):
            ImgUrl = AlbumJson['data']['items'][a]['pictures'][0]['img_src']
            SaveImage(ImgUrl, "F:\下载\投稿\\"+ ImgTitle + ".png")
        else:
            i = 0
            while i < len(ImgList) :
                ImgUrl = AlbumJson['data']['items'][a]['pictures'][i]['img_src']
                SaveImage(ImgUrl, "F:\下载\投稿\\"+ ImgTitle + str(i)+ ".png")
                i = i + 1
        a = a +1
    print('完成一次')



    

    