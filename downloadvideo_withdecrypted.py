# -*-coding:utf-8 -*-

#必须使用m3u8

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
from urllib.parse import urljoin

import subprocess
from accesscmd import python2cmd

import os

from Crypto.Cipher import AES
import binascii


k=0

html=input("请输入m3u8文件的地址:")
name2save=input("请输入想要保存的文件名:")

#def downloadvideo(k):

for k in range(5):

	print("正在下载m3u8_0",k,"文件")
	f=open(r"C:\Users\ASUS\Desktop\m3u8_0"+str(k),"r")
	m3u8=f.read()

	results=re.findall(r"(?:[a-z]|\d).*",m3u8)
	#print(results)

	orilinks=results
	links=[]
	for link in orilinks:
		if link.endswith(".ts"):
			links.append(link)
	#print(links[0])

	keyhtml=re.search(r"h.*?\"",m3u8)
	keyhtml=keyhtml.group(0)
	#print(keyhtml[:-1])

	ivresult=re.search(r"(?:0x).*",m3u8)
	ivresult=ivresult.group(0)[2:]
	#print(ivresult)


	#----------------------------------------------构造请求头 获取360对应课程的密钥-----------------------------------
	header={
		'Host': 'trans.college.360.cn',
		'Connection': 'keep-alive',
		'Origin': 'https://admin.college.360.cn',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400',
		'Accept': '*/*',
		'Referer': 'https://admin.college.360.cn/user/student/course/1189',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9'
	}
	rkey=requests.get(keyhtml[:-1],headers=header)

	#等会儿解密使用
	key=rkey.text.encode("utf-8")
	iv=binascii.a2b_hex(ivresult)
	mode=AES.MODE_CBC
	cryptos=AES.new(key,mode,iv)

	#-------------------------------------------------------------------------------------------------------------------
	
	i=0

	#路径皆使用双杠 照顾好用但愚蠢的ffmpeg
	#若不存在 则创建一个单独的文件夹
	videopath=r"F:\\SomePythonProjects\\videos\\"+name2save
	videopath+="_0"+str(k)
	os.mkdir(videopath)
	#用于记录ts文件名 方便使用ffmpeg合并
	videopath+=r"\\"

	findex=open(videopath+name2save+".txt","w+")

	#设置个进度条长度 单纯为了单行显示的美观
	tq=tqdm(links,ncols=60)
	for link in tq:
		if i<=9:
			videoname=name2save+"0"+str(i)+".ts"
		else:
			videoname=name2save+str(i)+".ts"
		i+=1
		f=open(videopath+videoname,"wb+")
		#先规范化一下路径 可能为相对路径
		link=urljoin(html,link)
		ts=requests.get(link)
		
		#解密ts内容再写入
		ts_dec=cryptos.decrypt(ts.content)
		
		f.write(ts_dec)
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