# coding:utf-8
"""
@version:0.0.1xz,by Binjie Gui
"""
import requests
def gc():
    global c
    c=[]

def get_download_chucks(url):
    gc()
    a = requests.get(url=url, stream=True)
    for b in a.iter_content(chunk_size=512):
        if b:
            c.append(b)
def gdc(url):
    get_download_chucks(url=url)
    return c