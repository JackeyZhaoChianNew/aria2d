# coding:utf-8

"""
@by Gui binjie
#from "downloadchucks.py"get file chucks and write in file
"""
import basic_downloads.getchucks

def writefile(url,dir):
    c=open(dir,"wb")
    m=-1
    s=basic_downloads.getchucks.gdc(url=url)
    for y in s:
        m+=1
        f=s[m]
        c.write(f)
    c.close()
writefile("http://www.baidu.com","index.html")