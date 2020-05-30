import requests
from urllib import request
import json
import time
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


COOKIE = "PTTactFirstTime=1590105600000; isActDate=18412; pgv_pvi=1715803136; pgv_pvid=3301987761; RK=1pAdkfKGdD; ptcz=b5f0a361ffeb806a4146e43f7847b12f6939c3b355ac940b9d27bd4fb3906600; eas_sid=I1a5S8q5B3H9r90303s676E5q2; ts_uid=9332089732; psrf_qqaccess_token=3FC957E084210883ACF0584D9FA7D4BC; psrf_access_token_expiresAt=1593257253; psrf_qqrefresh_token=35AFEE2C13179EF5F1B9EE64BAEE8F65; psrf_qqunionid=D47DFCBBE769E1B57AA5AF32B7A646A6; psrf_qqopenid=61A4AE31AF7BB7FF37DBA95AF9C7B0EB; PTTuserFirstTime=1585699200000; tvfe_boss_uuid=d044f4a88eef8e6c; pac_uid=1_1639983233; XWINDEXGREY=0; weekloop=19-20-21-22; ied_qq=o1192769569; uin_cookie=o1192769569; ptui_loginuin=1192769569; o_cookie=1878893924; uin=o1192769569; 9fc0fc1340b8040279718c2990788fb9=1192769569; isHostDate=18412; isOsSysDate=18412; pgv_info=ssid=3301987761; ts_last=wuxia.qq.com/cp/a20180423myzone/index.shtml; tokenParams=%3FindexId%3D0; gpmtips_cfg=%7B%22iSendApi%22%3A0%2C%22iShowCount%22%3A0%2C%22iOnlineCount%22%3A0%2C%22iSendOneCount%22%3A0%2C%22iShowAllCount%22%3A0%2C%22iHomeCount%22%3A0%7D; _qpsvr_localtk=0.3166931431784936; pgv_si=s8752208896; skey=@qXJSnIgSx; wuxiaqqcomrouteLine=a20180423myzone_a20180423myzone; IED_LOG_INFO2=userUin%3D1192769569%26nickName%3D2toPt%26nickname%3D2toPt%26userLoginTime%3D1590825066%26logtype%3Dqq%26loginType%3Dqq%26uin%3D1192769569"


#截取字符串
def GetMiddleStr(content,startStr,endStr):
    startIndex = content.index(startStr)
    if startIndex>=0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]



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

		print("-----------人气值[{}]---------访问主页{}".format(popularity,sMsg))
	except Exception as r:
		print('未知错误 %s' %(r))



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
		print("---------------点赞{}---------------异常:{}".format(sMsg,returnMsg))
	except Exception as r:
		print('点赞未知错误 %s' %(r))


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
		print("---------------评论{}---------------异常:{}".format(sMsg,returnMsg))
	except Exception as r:
		print('评论未知错误 %s' %(r))




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
		print('获取热门话题内容未知错误 %s' %(r))
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
		print('获取热门话题id未知错误 %s' %(r))
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
				print("\nmomentId:{}\nuserId:{}\ntext:{}\nname:{}\n".format(hot['momentId'],hot['userId'],hot['text'],hot['name']))
				doDianzan(hot['momentId'])
				doPinglun(hot['momentId'])
				doLookMian(hot['userId'])
				print("=======================[%s]======================"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

	
	#60秒获取一次
	time.sleep(60)






