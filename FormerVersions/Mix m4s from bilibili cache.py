#Mix By HF

from os import system
import json
from time import sleep
import winreg
ToolDir=r'D:\HF_Doc\Program\mkvtoolnix\mkvmerge.exe'
special_chars=r'\/:*?"><=|'

system(ToolDir+r' --ui-language zh_CN --output ^".\Mixed.mkv^" --language 0:und ^"^(^" ^".\audio.m4s^" ^"^)^" --language 0:und ^"^(^" ^".\video.m4s^" ^"^)^" --track-order 0:0,1:0')
#sleep(5)
with open(r"..\entry.json","r",encoding="utf-8") as f:
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

975604735
└─c_411035633
    │  danmaku.xml
    │  entry.json
    │  
    └─116
            audio.m4s
            index.json
            video.m4s
'''
