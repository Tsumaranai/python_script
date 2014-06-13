# -*- coding: cp936 -*-
#'Accept':'image/webp,*/*;q=0.8',
    #'Accept-Encoding':'gzip,deflate,sdch',
    #'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh-TW;q=0.4',
    #'X-Requested-With':'XMLHttpRequest'
    

import os
import urllib
import urllib2

import cookielib
import re
import types
import time

login_url = 'https://login.xiami.com/member/login'
sign_url = 'http://www.xiami.com/task/signin'
home_url = 'http://www.xiami.com'
filename = 'D:\\JustCookie\\cookie.txt'
get_token_url = 'http://www.xiami.com/index/feed?_=1397614182561'
get_TSA_url = 'http://www.xiami.com/index/home?_=1397615226343'
check_url = 'http://www.xiami.com/task/checkindex?_=1397650442687'

data = {
	'_xiamitoken' : '',
	'done' : 'http%3A%2F%2Fwww.xiami.com%2F',
	'email' : 'jaychou_pku@163.com',
	'password' : '521521521',
	'autologin': '1',
	'submit' : '登 录',
        'from':'web'
}

#DAMN!culprit the XIAMI check 'Referer' ... 
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'http://www.xiami.com'
    }

cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

req = urllib2.Request(login_url, headers)

#website_html = opener.open(req).read()

#Because website hide the _xiamitoken into the html,we should extract it!
website_html = opener.open(login_url).read()
pa = re.compile('\"_xiamitoken\" value=\"[a-z0-9]{32}')
result = pa.search(website_html)
x_t = re.search('[a-z0-9]{32}', result.group(0)).group(0)
data["_xiamitoken"] = x_t

#post the login information
post_data = urllib.urlencode(data)

req = urllib2.Request(login_url, post_data, headers)

resp_html = opener.open(req).read()

#req = urllib2.Request(home_url, None, headers)

#opener.open(req)

#get the _xiamitoken again, secrue cookie will vanish when http changed into https
req = urllib2.Request(get_TSA_url, None, headers)
#They should be jason
data = opener.open(req).read()
print data

#I don't know it works, just trying
req = urllib2.Request(check_url, None, headers)

opener.open(req)

#req = urllib2.Request(get_token_url, None, headers)

#opener.open(req)

req = urllib2.Request(sign_url, '', headers)

opener.open(req)



