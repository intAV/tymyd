#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from urllib import request
import json
import time
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from tkinter import *
import threading
import re
import inspect
import ctypes


COOKIE = ""


#截取字符串
def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex>=0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]



# 过滤表情
def filter_emoji(desstr,restr=''):  
    try:  
        co = re.compile(u'[\U00010000-\U0010ffff]')  
    except re.error:  
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')  
    return co.sub(restr, desstr)


#退出子进程
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
#退出子进程
def stop_thread(thread):
	text2.insert(END,"已经结束子进程"+"\n")
	text2.see(END)
	_async_raise(thread.ident, SystemExit)



#查看主页
def doLookMian(friendUserId):
	time.sleep(1)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/user/getuserinfo&callback=jQuery17100012562480264131093_{}1588&uin=1192769569&userId=7904671&friendUserId={}"
	headers = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	        'Cookie':COOKIE
	    }
	base_url = url.format(friendUserId,friendUserId)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseTxt = GetMiddleStr(response.read().decode("utf-8"),'(',')')
		sMsg = json.loads(responseTxt)['sMsg']
		popularity = json.loads(json.loads(responseTxt)['jData']['jData'])['data']['popularity']

		myPrint("--------------人气[{}]--------------异常:{}".format(popularity,sMsg))
	except Exception as r:
		myPrint('未知错误 %s' %(r))



#说说点赞
def doDianzan(momentId):
	time.sleep(5)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/moment/like&callback=jQuery171006764405901210213_1590{}&uin=1192769569&userId=7904671&momentId={}&type=1&_={}"
	headers = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	        'Cookie':COOKIE
	    }
	
	base_url = url.format(momentId,momentId,momentId)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseText = response.read().decode("utf-8")[42:-2]
		sMsg = json.loads(responseText)['sMsg']
		returnMsg = json.loads(json.loads(responseText)['jData']['jData'])['returnMsg']
		myPrint("---------------点赞{}---------------异常:{}".format(sMsg,returnMsg))
	except Exception as r:
		myPrint('点赞未知错误 %s' %(r))


#说说评论
def doPinglun(momentId):
	time.sleep(5)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/moment/addcomment&callback=jQuery17108402774150402388_1590{}&uin=1192769569&userId=7904671&roleId=1318055637&text=%e7%a9%ba%e9%97%b4%e4%ba%92%e8%b8%a9%e4%ba%92%e5%85%b3&momentId={}&replyCommentId=0"
	headers = {
	        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	        'Cookie':COOKIE
	    }

	base_url = url.format(momentId,momentId,momentId)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseText = response.read().decode("utf-8")[41:-2]
		sMsg = json.loads(responseText)['sMsg']
		returnMsg = json.loads(json.loads(responseText)['jData']['jData'])['returnMsg']
		myPrint("---------------评论{}---------------异常:{}".format(sMsg,returnMsg))
	except Exception as r:
		myPrint('评论未知错误 %s' %(r))




#获取热门话题内容(momentId,userId,text,name)
def getHotText(huatiId):
	nowtime = int(time.time() * 1000)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/moment/topicmomentlist&callback=jQuery17109485360742260489_{}&gameId=10002&userId=7904671&fromIds=&topicId={}&sortType=1&_={}".format(nowtime,huatiId,nowtime)
	headers = {
	        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	        'Cookie':COOKIE
	    }
	req = request.Request(url,headers=headers)
	objHotText = []
	try:
		response = request.urlopen(req)
		responseText = response.read().decode("utf-8")[41:-2]
		msg = json.loads(responseText)['jData']['jData']
		data_list = json.loads(msg)['data']

		
		for l in data_list['list']:
			hotText={}
			hotText['momentId'] = l['momentId']
			hotText['userId'] = l['userId']
			hotText['text'] = l['text']
			hotText['name'] = l['name']
			objHotText.append(hotText)

		return(objHotText)

	except Exception as r:
		myPrint('获取热门话题内容未知错误 %s' %(r))
		return(objHotText)
		

	



#获取热门话题id
def getHuatiId():
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/gethottopiclist&callback=jQuery17100504510865243335_1590662496827&gameId=10002&userId=7904671&tagId=0&fromIds=0&_=1590662497426"
	headers = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	        'Cookie':COOKIE
	    }

	req = request.Request(url,headers=headers)
	huatiId_list = []

	try:
		response = request.urlopen(req)
		responseTxt = GetMiddleStr(response.read().decode("utf-8"),'(',')')
		data_list = json.loads(json.loads(responseTxt)['jData']['jData'])['data']['list']

		#只获取大于1000条动态的id
		for i in data_list:
			if int(i['desc'][:-2]) > 1000:
				huatiId_list.append(str(i['id']))	
		return huatiId_list

	except Exception as r:
		myPrint('获取热门话题id未知错误 %s' %(r))
		return(huatiId_list)


#说说id输入txt文本
def inputTxtid(momentId):
	with open("idlist", 'a',encoding='utf-8') as file_object:
		file_object.write(str(momentId)+"\n")
	file_object.close()



#获取txt文本的说说id(查看是否为新说说)
def getTxtid():
	if not os.path.isfile("idlist"):
		fd = open("idlist", mode="w", encoding="utf-8")
		fd.close()
	f = open('idlist', 'r')
	idtxt = f.readlines()
	f.close()
	return idtxt


def go():

	while True:

		#获取热门话题id
		huatiId = getHuatiId()

		for id in huatiId:

			#根据id获取说说列表
			hotText = getHotText(id)

			#遍历每条说说
			for hot in hotText:
				#判断该说说是否是新内容
				if (hot['momentId']+"\n") not in getTxtid():
					inputTxtid(hot['momentId'])
					myPrint("\nmomentId:{}\nuserId:{}\ntext:{}\nname:{}\n".format(hot['momentId'],hot['userId'],hot['text'],hot['name']))
					doDianzan(hot['momentId'])
					doPinglun(hot['momentId'])
					doLookMian(hot['userId'])
					myPrint("========================[%s]======================"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
		
		#60秒获取一次
		time.sleep(60)



def myPrint(s):
	#过滤表情特殊字符
	txt = filter_emoji(s, restr='')
	text2.insert(END,txt+"\n")
	text2.see(END)


def setCookie():
	global COOKIE
	COOKIE = text1.get(1.0,END).strip().replace("\n","").encode()
	go()



def btnClick():
	if btn['text'] == "开始":
		t1.start()
		btn['text'] = "结束"
		return
	if btn['text'] == "结束":
		stop_thread(t1)
		btn['text'] = "退出"
		return
	if btn['text'] == "退出":
		exit()
	



if __name__=="__main__":
	root = Tk()
	root.title("天涯明月刀空间点赞")
	text1 = Text(width=67, height=10)
	text2 = Text(width=67, height=30)

	btn = Button(text="开始", bg="lightblue", width=10,command=btnClick)
	t1 = threading.Thread(target=setCookie)

	text1.pack()
	btn.pack()
	text2.pack()
	root.mainloop()
















