#Mix By HF

from os import system
import json
from time import sleep
import winreg
ToolDir=r"D:\mkvtoolnix\mkvmerge.exe"
special_chars=r'\/:*?"><='

system(ToolDir+r' --ui-language zh_CN --output ^".\Mixed.mkv^" --language 0:und ^"^(^" ^".\audio.m4s^" ^"^)^" --language 0:und ^"^(^" ^".\video.m4s^" ^"^)^" --track-order 0:0,1:0')
#sleep(5)
with open(r"..\entry.json","r",encoding="utf-8") as f:
    try:
        rdata=json.load(f)
        title1=str(rdata['title'])
        title2=str(rdata['page_data']['download_subtitle'])
        if title2==title1+' '+title1:
            title=title1
        else:
            title21=" P"+str(rdata['page_data']['page'])
            title22=title2.replace(title1,"")
            title20=title2.replace(title22,"")
            title=title20+title21+title22
    except:
        title=str(json.load(f).get("title"))
#system(f"rename mixed.mkv {title}.mkv")
for char in special_chars:
    title = title.replace(char," ")
downpath = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"),"{374DE290-123F-4565-9164-39C4925E467B}")[0]
print(f'move mixed.mkv "{downpath}\\{title}.mkv"')
system(f'move mixed.mkv "{downpath}\\{title}.mkv"')
#system("pause")
sleep(5)

'''
这里使用mkvtoolnix进行混合,需要修改路径
用replace方法替换掉文件名中不能出现的特殊字符
winreg调取downloads文件夹位置，{374DE290-123F-4565-9164-39C4925E467B}代表下载文件夹目录
上一级文件夹的json文件包含视频名称
系统move可以在移动的同时重命名
eval()可以把以字典方式书写的字符串转为字典
json.load(f)调取的元素格式会自动转换

975604735
└─c_411035633
    │  danmaku.xml
    │  entry.json
    │  
    └─116
            audio.m4s
            index.json
            video.m4s

with open(r"..\entry.json","r",encoding="utf-8") as f:
     title=str(json.load(f).get("page_data"))
     title1=str(json.load(f).get("title"))
     title=eval(title)
     title=title['download_subtitle']
     if title==title1*2:
         title=title1
'''
