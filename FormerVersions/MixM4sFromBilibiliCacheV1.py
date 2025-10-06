#Mix By HF
#Multi-Process

from os import system, walk, path, getcwd, chdir, environ
from glob import iglob, glob
import json
from time import sleep
import winreg
#ToolDir=r'D:\HF_Doc\Program\mkvtoolnix\mkvmerge.exe'
special_chars=r'\/:*?"><=|'

def WorkList():
    '''
    lit=[]
    for root, dirs, files in walk(getcwd()):
        for file in files:
            t=path.join(root, file)
            if t.endswith('video.m4s'):
                lit.append(t)
    '''
    '''
    Path=getcwd()+"\\**\\video.m4s"
    prelit=iglob(Path,recursive=True)
    lit=[]
    '''
    Path=getcwd()+"\\**\\video.m4s"
    prelit=glob(Path,recursive=True)
    '''
    lit=[]
    for i in prelit:
        if i.endswith("video.m4s"):
            lit.append(i)
    '''
    lit=[]
    for i in prelit:
        lit.append(i)
    return lit

def Dos(Dir):
    chdir(Dir[:-9])#去掉‘video.m4s’
    with open(environ['appdata']+f"\\MixM4sFromBilibiliCache",encoding="utf-8") as f:
        ToolDir=f.read()
    system(ToolDir+r' --ui-language zh_CN --output ^".\Mixed.mkv^" --language 0:und ^"^(^" ^".\audio.m4s^" ^"^)^" --language 0:und ^"^(^" ^".\video.m4s^" ^"^)^" --track-order 0:0,1:0')
    #sleep(5)
    with open(r"..\entry.json","r",encoding="utf-8") as f:
        rdata=json.load(f)
        try:
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
            title=str(rdata.get("title"))
    #system(f"rename mixed.mkv {title}.mkv")
    for char in special_chars:
        title = title.replace(char," ")
    downpath = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"),"{374DE290-123F-4565-9164-39C4925E467B}")[0]
    f=f'move mixed.mkv "{downpath}\\{title}.mkv"'
    print(f)
    system(f)

Wlist=WorkList()
for i in Wlist:
    Dos(i)
system("pause")

'''
这里使用mkvtoolnix进行混合, 需要修改路径
用replace方法替换掉文件名中不能出现的特殊字符
winreg调取downloads文件夹位置, {374DE290-123F-4565-9164-39C4925E467B}代表下载文件夹目录
上一级文件夹的json文件包含视频名称
系统move可以在移动的同时重命名
os.chdir(path)函数用于更改当前工作目录到指定的目录
os.getcwd()函数用来遍历文件
os.environ['appdata']获得其位置

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
