#!/usr/bin/env python

import os
import sys
import urllib
import urllib2
import re
import cookielib


url_addr = 'http://fun.coolshell.cn/n/'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

def get_num( url ):
	
	req = urllib2.Request(url)

	resp_html = opener.open(req).read()

	pa = re.compile('[0-9]{1,}')

	result = pa.search(resp_html)

	try:
		return result.group(0)

	except:
		print resp_html
		return False


def main():
	
	num = '32286'

	while num:

		print num
		
		url = url_addr + num
		
		num = get_num(url)
	
	
if __name__ == '__main__':

	main()





