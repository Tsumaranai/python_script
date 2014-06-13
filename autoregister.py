import urllib
import urllib2

import cookielib
import string
import re

import time


login_url = 'http://localhost/booked/Web/register.php?action=register'
verify_code_url = 'http://localhost/booked/Web/Services/Authentication/show-captcha.php?show=true'


data = {
    "login":"",
    "password":"",
    "passwordConfirm":"",
    "fname":"first",
    "lname":"",
    "defaultHomepage":"1",
    "email":"",
    "timezone":"Asia/Shanghai",
    "phone":"",
    "organization":"",
    "position":"",
    "captcha":""
    }


headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'
    }

username = ("zhangxiao","heqinlu", "sunjian", "wanghuifeng", "guowan", "qichanying", 
            "zhangruijie", "liufangyi", "zhuyanbing", "zhaoxiaonan", "liani", 
            "zhangboyang", "chenwenjia")
#urllib2.urlopen('http://localhost/booked/Web/register.php')

def regist(info):
    #initialize a jar to cope with the cookie stuffs
    cookieJar = cookielib.CookieJar()

    #initialize a object to opner to open with cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))


    #just for get cookie and use the open
    #urllib2.Request('http://localhost/booked/Web/register.php')


    data["login"] = info
    data["password"] = info + '123'
    data["passwordConfirm"] = info + '123'
    data["lname"] = info
    data["email"] = info + '@mail.com'

    #open and read the verify code
    verify_code_data = opener.open(verify_code_url).read()
    file_name = 'D:\\verify_image\\tmp.png'
    output = open(file_name, 'wb')
    output.write(verify_code_data)
    output.close()
    time.sleep(1)

    #go to D:to check the verify code
    captcha = raw_input('Verify Code:\n')
    data["captcha"] = captcha


    post_data = urllib.urlencode(data)

    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor)

    #req~I think that it is a handler like~
    req = urllib2.Request(login_url, post_data, headers)
    #opener.open open this handler just think~
    response = opener.open(req)

    text = response.read()
    #show the state
    print text
    reg = re.compile('Error')
    result = reg.match(text)
    if result == None:
        return True
    else:
        return False


def main():

    for item in username:
        print item
        while (not regist(item)):
            continue
        
    print 'complete!\n'

if __name__ == '__main__':
    main()
