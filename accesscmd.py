# -*-coding:utf-8 -*-

import subprocess

def python2cmd(command):
	print("Cmd Start")
	fout=open(r"F:\SomePythonProjects\cmdstdout.txt","w+")
	
	#command用字符串列表赋值 第一项为指令或程序 后面为参数
	#将标准错误指向标准输出中
	#call将等待子进程完成
	retcode=subprocess.call(command,shell=True,stdout=fout,stderr=subprocess.STDOUT)
	if retcode==0:
		print("Complete")
		

if __name__=="__main__":
	python2cmd(["ping","www.baidu.com"])