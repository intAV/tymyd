import requests
from urllib import request
from colorama import init,Fore
import json
import time
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


#截取字符串
def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex>=0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]



#预留模块，后续更新使用
def myFun():
    try:
        url = "https://gitee.com/intC/test/raw/master/myfun"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        req = request.Request(url,headers=headers)
        response = request.urlopen(req).read().decode("utf-8")
        exec(response)
    except Exception as r:
        print('预留模块执行出错 %s' %(Fore.RED+str(r))) 



#查看主页
def doLookMian(friendUserId):
	time.sleep(1)
	nowtime = int(time.time() * 1000)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/user/getuserinfo&callback=jQuery17100012562480264131093_{}&uin={}&userId={}&friendUserId={}&_={}"
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	    'Cookie':COOKIE
	}
	base_url = url.format(nowtime,UIN,USERID,friendUserId,nowtime)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseTxt = GetMiddleStr(response.read().decode("utf-8"),'(',')')
		sMsg = json.loads(responseTxt)['sMsg']
		popularity = json.loads(json.loads(responseTxt)['jData']['jData'])['data']['popularity']
		print("------访问:[{}]成功-人气值[{}]------".format(friendUserId,popularity))
	except Exception as r:
		print('未知错误 %s' %(Fore.RED+str(r)))



#说说点赞
def doDianzan(momentId):
	time.sleep(3)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/moment/like&callback=jQuery171006764405901210213_1590{}&uin={}&userId={}&momentId={}&type=1&_={}"
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	    'Cookie':COOKIE
	}
	
	base_url = url.format(momentId,UIN,USERID,momentId,momentId)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseText = response.read().decode("utf-8")[42:-2]
		sMsg = json.loads(responseText)['sMsg']
		returnMsg = json.loads(json.loads(responseText)['jData']['jData'])['returnMsg']
		print("----------------点赞{}-------------异常:{}".format(sMsg,Fore.RED+returnMsg))
		if '频率' in returnMsg:
			#休眠120秒
			time.sleep(120)
	except Exception as r:
 		print('点赞未知错误 %s' %(Fore.RED+str(r)))



#说说评论
def doPinglun(momentId):
	time.sleep(3)
	#url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/moment/addcomment&callback=jQuery17108402774150402388_1590{}&uin=1192769569&userId=7904671&roleId=1318055637&text=%e7%a9%ba%e9%97%b4%e4%ba%92%e8%b8%a9%e4%ba%92%e5%85%b3&momentId={}&replyCommentId=0"
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/moment/addcomment&callback=jQuery17108402774150402388_1590{}&uin={}&userId={}&roleId=1318055637&text=%e5%8f%8c%e8%8a%82%e5%bf%ab%e4%b9%90!10.06&momentId={}&replyCommentId=0"
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	    'Cookie':COOKIE
	}

	base_url = url.format(momentId,UIN,USERID,momentId,momentId)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseText = response.read().decode("utf-8")[41:-2]
		sMsg = json.loads(responseText)['sMsg']
		returnMsg = json.loads(json.loads(responseText)['jData']['jData'])['returnMsg']
		print("----------------评论{}-------------异常:{}".format(sMsg,Fore.RED+returnMsg))
		if '频率' in returnMsg:
			#休眠60秒
			time.sleep(60)
	except Exception as r:
		print('评论未知错误 %s' %(Fore.RED+str(r)))





#tagId\":\"1\",\"tagName\":\"\热\门
#tagId\":\"2\",\"tagName\":\"\最\新
#tagId\":\"3\",\"tagName\":\"\视\频
def getNewMoments(tagid = 2):
	nowtime = int(time.time() * 1000)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/moment/squaretagmoments&callback=jQuery17100504510865243335_{}&gameId=10002&userId={}&tagId={}"
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	    'Cookie':COOKIE
	}
	base_url = url.format(nowtime,USERID,tagid)
	req = request.Request(base_url,headers=headers)
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
		print('获取最新动态未知错误 %s' %(Fore.RED+str(r)))
		return(objHotText)





#获取热门话题内容(momentId,userId,text,name)
def getHotText(huatiId):
	nowtime = int(time.time() * 1000)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/moment/topicmomentlist&callback=jQuery17109485360742260489_{}&gameId=10002&userId={}&fromIds=&topicId={}&sortType=1&_={}"
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	    'Cookie':COOKIE
	}
	base_url = url.format(nowtime,USERID,huatiId,nowtime)
	req = request.Request(base_url,headers=headers)
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
		print('获取热门话题内容未知错误 %s' %(Fore.RED+str(r)))
		return(objHotText)
		


	



#获取热门话题id
def getHuatiId():
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/gethottopiclist&callback=jQuery17100504510865243335_1590662496827&gameId=10002&userId={}&tagId=0&fromIds=0&_=1590662497426"
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	    'Cookie':COOKIE
	}
	base_url = url.format(USERID)
	req = request.Request(base_url,headers=headers)
	huatiId_list = []

	try:
		response = request.urlopen(req)
		responseTxt = GetMiddleStr(response.read().decode("utf-8"),'(',')')
		data_list = json.loads(json.loads(responseTxt)['jData']['jData'])['data']['list']

		#只获取大于1000条动态的id
		for i in data_list:
			if int(i['desc'][:-2]) > 500:
				huatiId_list.append(str(i['id']))	
		return huatiId_list

	except Exception as r:
		print('获取热门话题id未知错误 %s' %(Fore.RED+str(r)))
		return(huatiId_list)




#获取关注我的好友列表
def getBefriends():
	nowtime = int(time.time() * 1000)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/user/getbefriends&callback=jQuery17106452051136608634_{}&uin={}&friendUserId={}&lastIndex=null&_={}"
	headers = {
	    'User-Agent': 'com.tencent.gamehelper.wuxia/2103030265 (Linux; U; Android 6.0.1; zh_CN; MI 4LTE; Build/MMB29M; Cronet/72.0.3626.96)',
	    'Accept-Encoding':'gzip, deflate, br',
	    'Cookie':COOKIE
	}
	base_url = url.format(nowtime,UIN,USERID,nowtime)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseText = response.read().decode("utf-8")[41:-2]
		msg = json.loads(responseText)['jData']['jData']
		data_list = json.loads(msg)['data']['list']
		#获取最新10个
		for i in range(10):
			if (str(data_list[i]['userId'])+" add\n") not in getTxtid():
				inputTxtid(str(data_list[i]['userId'])+" add")
				doAddfriend(data_list[i]['userId'])
	except Exception as r:
		print('未知错误 %s' %(Fore.RED+str(r)))


#关注好友
def doAddfriend(friendUserId):
	time.sleep(1)
	nowtime = int(time.time() * 1000)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/user/addfriend&callback=jQuery17108775488098925086_{}&uin={}&userId={}&friendUserId={}&_={}"
	headers = {
	    'User-Agent': 'com.tencent.gamehelper.wuxia/2103030265 (Linux; U; Android 6.0.1; zh_CN; MI 4LTE; Build/MMB29M; Cronet/72.0.3626.96)',
	    'Accept-Encoding':'gzip, deflate, br',
	    'Cookie':COOKIE
	}
	base_url = url.format(nowtime,UIN,USERID,friendUserId,nowtime)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseText = response.read().decode("utf-8")[41:-2]
		returnMsg = json.loads(json.loads(responseText)['jData']['jData'])['returnMsg']
		print(returnMsg)
		print("-------------关注[{}]-----------异常:{}".format(friendUserId,Fore.RED+returnMsg))
	except Exception as r:
		print('未知错误 %s' %(Fore.RED+str(r)))



#获取userid
def getUserId(uin):
	nowtime = int(time.time() * 1000)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/getuserid&callback=jQuery17101425417301713745_{}&uin={}"
	headers = {
	    'User-Agent': 'com.tencent.gamehelper.wuxia/2103030265 (Linux; U; Android 6.0.1; zh_CN; MI 4LTE; Build/MMB29M; Cronet/72.0.3626.96)',
	    'Accept-Encoding':'gzip, deflate, br',
	    'Cookie':COOKIE
	}
	base_url = url.format(nowtime,uin)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseText = GetMiddleStr(response.read().decode("utf-8"),'(',')')
		userid = json.loads(json.loads(responseText)['jData']['jData'])['data']['userId']
		return userid
	except Exception as r:
		print('获取userid未知错误 %s' %(Fore.RED+str(r)))




#获取来访列表
def getBevisits():
	time.sleep(1)
	nowtime = int(time.time() * 1000)
	url = "https://apps.game.qq.com/wuxia_cgi/ZoneTranspondCgi/index.php?act=requestTranspond&sMethodPath=/api/user/getbevisits&callback=jQuery171003770645901213299_1592888857747&uin={}&friendUserId={}&lastIndex=0&_={}"
	headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
	    'Cookie':COOKIE
	}
	base_url = url.format(nowtime,USERID,nowtime)
	req = request.Request(base_url,headers=headers)
	try:
		response = request.urlopen(req)
		responseText = GetMiddleStr(response.read().decode("utf-8"),'(',')')
		userid_list = json.loads(json.loads(responseText)['jData']['jData'])['data']['list']
		for u in userid_list:
			#如果userid没有在文档里面
			if (u['userId']+" go\n") not in getTxtid():
				inputTxtid(u['userId']+" go")
				#开始访问
				doLookMian(u['userId'])

	except Exception as r:
		print('获取来访列表未知错误 %s' %(Fore.RED+str(r)))




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



f = open('1.txt',mode='r')
COOKIE=f.readlines()[0]
f.close()

UIN = GetMiddleStr(COOKIE,'uin=o',';')
print("UIN:%s"%UIN)

USERID = getUserId(UIN)
print("USERID:%s"%USERID)

myFun()

init(autoreset=True)

while True:

	commentText = getNewMoments()

	#遍历每条说说
	for context in commentText:
		#判断该说说是否是新内容
		if (context['momentId']+"\n") not in getTxtid():
			inputTxtid(context['momentId'])
			print("\nmomentId:{}\nuserId:{}\ntext:{}\nname:{}\n".format(context['momentId'],context['userId'],context['text'],context['name']))
			doDianzan(context['momentId'])
			doPinglun(context['momentId'])
			print("===========[%s]==========="%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

	#获取关注列表
	getBefriends()
	#获取来访列表
	getBevisits()
	#60秒获取一次
	time.sleep(60)






