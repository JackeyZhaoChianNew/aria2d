# coding:utf-8

"""
@by Gui binjie
#from "downloadchucks.py"get file chucks and write in file
"""
import basic_downloads.getchucks

def writefile(url,dir):
    c=open(dir,"wb")
    s=basic_downloads.getchucks.get_download_chucks(url=url)
    for y in s[1]:
        f=s[0][y]
        c.write(f)
    c.close()