#coding:UTF-8

import urllib
import urllib2
import cookielib

url = 'https://www.pixiv.net/login.php'
filename = 'cookie.txt'

p_id = raw_input("�������pixiv id:")
p_pw = raw_input("�������������:")

cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#build_opener�����������Զ���opener����ĺ���

data = {
    'mode':'login',
    'skip':1
        }

data['pass'] = p_pw
data['pixiv_id'] = p_id

p_login_data = urllib.urlencode(data)
print p_login_data

#�����pվ�ĵ�½��Ϣ
header = {
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Referer':'https://www.pixiv.net/login.php?return_to=0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
#��½��ʹ�õ�����ͷ��Ϣ
request = urllib2.Request(
    url,
    data = p_login_data,
    headers = header)

login_pixiv = opener.open(request)
#����ǰ�������ͷ��Ϣ��cookie��Ϣ���е�½

cookie.save(ignore_discard = True , ignore_expires = True)
#��½�ɹ�
bookmark_url = 'http://www.pixiv.net/bookmark.php'

login_pixiv =opener.open(bookmark_url)
page = login_pixiv.read()

file_html = open('pixiv-1.html','w')
file_html.write(page)
file_html.close()