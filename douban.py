import urllib
import urllib2
import os

import cookielib
import re
import time

D_photo_path_large = 'http://img3.douban.com/view/photo/large/public/p'
D_photo_path_small = 'http://img5.douban.com/view/photo/photo/public/p'

D_album_url = '1'

total = '1'

album_name = '1'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
    'Referer':'http://www.douban.com/photos/photo/1972891629/',
    'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh-TW;q=0.4',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    
    }

size = True

cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

def find_num(pic_url, i):

    global total, album_name, D_album_url, size
    req = urllib2.Request(pic_url, None, headers)

    resp = urllib2.urlopen(req)

    #print resp.__doc__
    web_html = resp.read()

    #print web_html
    pa = re.compile('link rel=\"next\" href=\"http:\/\/www\.douban\.com\/photos\/photo\/[0-9]*?\/"')
    result = pa.search(web_html)

    D_album_url = re.search('http:\/\/www\.douban\.com\/photos\/photo\/[0-9]*?\/', result.group(0)).group(0)
    pic_num = re.search('[0-9]+', pic_url).group(0)

    pa = re.compile('查看大图')
    result = pa.search(web_html)

    if result:
        size = True
    else:
        size = False
    #print pic_num
    #print D_album_url

    if(i == 0):
        pa = re.compile('共[0-9]+张')
        result = pa.search(web_html)
        total = re.search('[0-9]+', result.group(0)).group(0)
        pa = re.compile('(?<=data-name=").+(?= 的)')
        album_name = pa.search(web_html).group(0)

    
    #print int(total)
    #print album_name
    return pic_num 




def main():

    global D_album_url, size
    i = 0
    flag = False
    times = 0
    file_dir = 'D:\\douban_image'
 
    D_album_url = raw_input('Please input a photo url:\n')
    pic_num = find_num(D_album_url, i)

    print album_name
    file_path = file_dir + '\\' + album_name
    file_path = file_path.decode('utf-8')
    if not os.path.exists(file_path):
	    os.makedirs(file_path)

    t = int(total)
	
    while not (i == t):

        if size:
            D_photo_path = D_photo_path_large
        else:
            D_photo_path = D_photo_path_small

        pic_url = D_photo_path + pic_num + '.jpg'

        
		
        while flag == False and times < 3:
		
            try:
                print 'Python is downloading the picture from ' + pic_url
                urllib.urlretrieve(pic_url, file_path + '//' +str(i) + '.jpg')
                flag = True
            except:
                #print 'something wrong!'
                if times < 3:
                    print 'Well someting wrong~I gonna try it again!'
                    times += 1
		
        if times == 3:
            print "It failed to downloading this picture"
		
        times = 0
        flag = False
        time.sleep(2)		
        pic_num = find_num(D_album_url, i)

        i += 1

    print 'Mission Completed!!'

if __name__ == '__main__':
    main()
    

    
