# coding:utf-8
"""
@version:0.0.1xz,by Binjie Gui
"""
import requests

def get_download_chucks(url):
    a = requests.get(url=url, stream=True)
    m=1
    global c
    c = []
    for b in a.iter_content(chunk_size=512):
        print(type(b))
        if b:
            if c!=[]:
                if b != c[-1]:
                    c.append(b)
                else:
                    c.append(b)
            else:
                v=[]
                m+=1
                if m==len(c):
                    v.pop(-1)
                    return [c,v]