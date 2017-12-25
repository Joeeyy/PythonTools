import urllib
import urllib2
import json
import time

def login():
	host='https://www.leisujsq.xyz:23243'
	api='/api/v53/login.php'
	postdata={}
	postdata['password']='shuangzi19940621'
	postdata['userlan']='zh-Hans-CN'
	postdata['username']='joeeeee000'
	params=urllib.urlencode(postdata)
	request=urllib2.Request(host+api,params)
	request.add_header('Content-Type','application/x-www-form-urlencoded; charset=utf-8')
	request.add_header('User-Agent',' GreenVPN/4 (iPhone; iOS 10.2.1; Scale/2.00)')
	request.add_header('Accept-Language','zh-Hans-CN;q=1, en-CN;q=0.9, ja-JP;q=0.8')
	request.add_header('Accept-Encoding','gzip, deflate')
	result=urllib2.urlopen(request)
	jsonarr=json.loads(result.read())
	userscore=jsonarr['userscore']
	userprize=jsonarr['userprize']
	loginMsg=jsonarr['loginMsg']
	username=jsonarr['username']
	
	
def renew():
	host='https://www.leisujsq.xyz:23243'
	api='/api/v53/prize_click.php'
	postdata={}
	postdata['prodid']='0105'
	postdata['token']='9dcb46038e4bf1ff015f9211be18a3c5'
	postdata['username']='joeeeee000'
	params=urllib.urlencode(postdata)
	request=urllib2.Request(host+api,params)
	request.add_header('Content-Type','application/x-www-form-urlencoded; charset=utf-8')
	request.add_header('User-Agent',' GreenVPN/4 (iPhone; iOS 10.2.1; Scale/2.00)')
	request.add_header('Accept-Language','zh-Hans-CN;q=1, en-CN;q=0.9, ja-JP;q=0.8')
	request.add_header('Accept-Encoding','gzip, deflate')
	result=urllib2.urlopen(request)
	jsonarr=json.loads(result.read())
	msg=jsonarr['Msg']
	print msg
	while msg=='msg_checkin_dup':
		result=urllib2.urlopen(request)
		jsonarr=json.loads(result.read())
		msg=jsonarr['Msg']
		time.sleep(1)
	
def execute():
	host='https://www.leisujsq.xyz:23243'
	api='/api/v53/prize_click.php'
	postdata={}
	postdata['prodid']='0103'
	postdata['token']='9dcb46038e4bf1ff015f9211be18a3c5'
	postdata['username']='joeeeee000'
	params=urllib.urlencode(postdata)
	request=urllib2.Request(host+api,params)
	request.add_header('Content-Type','application/x-www-form-urlencoded; charset=utf-8')
	request.add_header('User-Agent',' GreenVPN/4 (iPhone; iOS 10.2.1; Scale/2.00)')
	request.add_header('Accept-Language','zh-Hans-CN;q=1, en-CN;q=0.9, ja-JP;q=0.8')
	request.add_header('Accept-Encoding','gzip, deflate')
	result=urllib2.urlopen(request)
	jsonarr=json.loads(result.read())
	msg=jsonarr['Msg']
	while msg=='msg_checkin_for_score_dup':
		result=urllib2.urlopen(request)
		jsonarr=json.loads(result.read())
		msg=jsonarr['Msg']
		time.sleep(1)

if __name__=='__main__':
	print 'main'
	#login()
	#execute()
	renew()
