import linecache
import easygui as g
from tkinter import *
import os



def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()


def search(word,JDpath):
    count = len(open(JDpath, 'r', encoding='utf-8').readlines())
    i = 1
    x = 1
    while i < count:
        keyword = linecache.getline(JDpath, i)
        if keyword.find(word) == -1:
            b = 1
        else:
            # 查询到了
            n = i
            print(2)
            while x < 2:
                keyword = linecache.getline(JDpath, n)
                if keyword.find("答案") == -1:
                    # 空值
                    b = 1
                else:
                    x = 2
                    Strtitle = keyword = linecache.getline(
                        JDpath, i)
                    keyword = linecache.getline(JDpath, n)
                    g.msgbox(msg=keyword, title=Strtitle, ok_button="确定")
                    i = count
                    # 查询到了
                    search(g.enterbox(msg="请输入搜索内容", title="禁毒正则"),JDpath)
                n = n + 1
        i = i + 1
    print("查询结束")


if __name__ == "__main__":
    JDpath = g.enterbox(msg="请输入题库路径", title="哔哩哔哩：萌新杰少")
    search(g.enterbox(msg="请输入搜索内容", title="禁毒正则"),JDpath)
