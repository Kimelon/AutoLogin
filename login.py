# -*- coding: UTF-8 -*-
import requests
import re
import time
import ConfigParser
import base64

login_data = {
	'username': '',
	'domain': '',
	'password': '',
	'enablemacauth': ''
}

headers_base = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'a.nuist.edu.cn',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
	#X-Requested-With:XMLHttpRequest
	}

def login():

	session = requests.session()
	baseurl = 'http://a.nuist.edu.cn/index.php/index/login'
	content = session.post(baseurl, headers = headers_base, data = login_data)
	print (content.text.decode('unicode-escape'))

def check():
	rtn = requests.get('http://a.nuist.edu.cn/index.php/index/login')
	info = "\u670d\u52a1\u5931\u6548\uff0c\u8bf7\u68c0\u67e5\u8d26\u6237\u53ca\u5230\u671f\u72b6\u6001"
	flag = rtn.text.find(info)
	if (flag != -1):
		print "Wifi has been disconnected.\nTry to reconnect."
		return False
def Readini():
	config = ConfigParser.ConfigParser()
	config.readfp(open('logindata.ini'))
	login_data['username'] = config.get("login","username")
	login_data['domain'] = config.get("login","domain")
	login_data['password'] = base64.b64encode(config.get("login","password"))
	login_data['enablemacauth'] = '0'

def main():
	Readini()
	print "The default login user:"	
	print login_data['username']
	print login_data['domain']
	while(1):
		if (check() == False):
			login()
		time.sleep(30)
main()
