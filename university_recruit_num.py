import os
import urllib
import urllib2

import cookielib
import re
import time
import json

url_u = "http://data.api.gkcx.eol.cn/soudaxue/queryProvinceScore.html"
university = (
'北京大学',
'北京航空航天大学',
'北京理工大学',
'北京师范大学',
'大连理工大学',
'电子科技大学',
'东北大学',
'东南大学',
'复旦大学',
'哈尔滨工业大学',
'湖南大学',
'华东师范大学',
'华南理工大学',
#'华中科技大学',
'吉林大学',
'兰州大学',
'南京大学',
'南开大学',
'清华大学',
'厦门大学',
'山东大学威海分校',
'山东大学',
'上海交通大学',
'四川大学',
'天津大学',
'同济大学',
'武汉大学',
'西安交通大学',
'西北工业大学',
'西北农林科技大学',
'浙江大学',
'中国海洋大学',
'中国科学技术大学',
'中国农业大学',
'中国人民大学',
'中南大学',
'中山大学',
'中央民族大学',
'重庆大学')

province = ('河南',
'北京',
'天津',
'上海',
'宁夏',
'湖北'
)
data = {
'messtype':'jsonp',
'url_sign':'queryProvinceScore',
'provinceforschool':'',
'schooltype':'',
'page':1,
'size':10,
'keyWord':'',
'schoolproperty':'',
'schoolflag':'',
'schoolsort':'',
'province':'',
'fsyear':'',
'fstype':'理科',
'zhaoshengpici':'',
'suiji':'',
'callback':'nihao',
'_':1403166208410
}
##keyWord = 大学名称
#province = 录取地区


headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'http://gkcx.eol.cn'
    }

#cj = cookielib.CookieJar()
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#data['keyWord'] = '北京大学'
data['province'] = '河南'
data['fsyear'] = 2013
data['zhaoshengpici'] = '一批'
text_file_path = 'E:\\PYTHON\\recruit_json.txt'
print_line = ''



for i_u in university:

	text_file = open( text_file_path, 'a')
	print_line += i_u.decode('utf-8')
	print_line += u':'
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	if True:
		data['keyWord'] = i_u
		#data['province'] = i_p
		get_data = urllib.urlencode(data)
		get_url = url_u + '?' + get_data

		req = urllib2.Request(get_url, None, headers)
		resp_html = opener.open(req).read()

		resp_html = resp_html.replace('nihao(','')
		resp_html = resp_html.replace(');','')

		recruit_json = json.loads(resp_html)
		#print get_data
		#print resp_html
		#text_file.write( resp_html )
		#pa = re.compile('(?<="num": ")\d{1,5}(?=",)')
		#result = pa.search( resp_html )
		for school_info in recruit_json[u'school']:

			if school_info[u'year'] == u'2013':	
				print_line += u'\t\t\t\t' + school_info[u'max']
				print_line += u'\t' + school_info[u'min']
				print_line += u'\t' + school_info[u'var_score']
				print print_line
				print_line = ''


		time.sleep(10)
		


		'''try:
			tmp = i_p + result.group(0) + '	'
			print_line += tmp
		except:
			print_line += i_p
			print_line += 'None		'
		time.sleep(10)


	#out of p_u
	print print_line
	text_file.write( print_line )
	print_line = ''
	text_file.close()'''

