# -*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
from urllib.parse import urljoin

import subprocess
from accesscmd import python2cmd

import os

#f=open(r"F:\SomePythonProjects\fordownload.txt","w+",encoding="utf-8")		#规定文件的编码方式 否则无法保存源文件

f=open(r"C:\Users\ASUS\Desktop\m3u8","r")
m3u8=f.read()

result=re.findall(r"[a-z].*",m3u8)
#print(type(result[0]))

links=result
#print(links[0])

html=input("请输入m3u8文件的地址:")
name2save=input("请输入想要保存的文件名:")

i=0
flag=0

#路径皆使用双杠 照顾好用但愚蠢的ffmpeg
#若不存在 则创建一个单独的文件夹
videopath=r"F:\\SomePythonProjects\\videos\\"+name2save
if not os.path.exists(videopath):
	os.mkdir(videopath)
#用于记录ts文件名 方便使用ffmpeg合并
videopath+=r"\\"

findex=open(videopath+name2save+".txt","w+")

#设置个进度条长度 单纯为了单行显示的美观
tq=tqdm(links,ncols=60)
for link in tq:
	if flag==0:
		print("开始下载")
		flag+=1
	if i<=9:
		videoname=name2save+"0"+str(i)+".ts"
	else:
		videoname=name2save+str(i)+".ts"
	i+=1
	f=open(videopath+videoname,"wb+")
	#先规范化一下路径 可能为相对路径
	link=urljoin(html,link)
	ts=requests.get(link)
	f.write(ts.content)
	findex.write(r"file "+videopath+videoname)
	findex.write("\n")
	f.close()

tq.close()
findex.close()
ts.close()

indexfilename=videopath+name2save+".txt"
print(indexfilename)
videofilename=videopath+name2save+".mp4"
print(videofilename)
ffcommand=["ffmpeg","-f","concat","-safe","0","-i",indexfilename,"-c","copy",videofilename]

python2cmd(ffcommand)

#ffmpeg -f concat -safe 0 -i F:\SomePythonProjects\videos\00.txt -c copy F:\SomePythonProjects\videos\test00.mp4