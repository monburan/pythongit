#coding:UTF-8
__author__ = 'monburan'
__version__ = '0.3 optimization'
import os
import urllib
import urllib2
import cookielib
import re
from bs4 import BeautifulSoup
from urllib2 import urlopen        

class Tools:

    remove = re.compile('amp;')
    rmbig = re.compile('_big')
    make_m = re.compile('mode=medium')
    
    def removebig(self,x):
        x = re.sub(self.rmbig,"",x)
        return x.strip()

    def removesomething(self,x):
        x = re.sub(self.remove,"",x)
        return x.strip()

    def make_big_url(self,x):
        x = re.sub(self.make_m,"mode=manga_big",x)
        return x.strip()

    def Pic_Type(self,real_url):                    
        p_type = re.search(re.compile('png',re.S),real_url)
        if p_type == None:
            self.pic_type = 'jpg'
            return self.pic_type
        else:
            self.pic_type = 'png'
            return self.pic_type

    def Pic_Style_M(self,soupfile):
        single = re.findall(re.compile('<.*?work\s_work\s".*?href="(.*?)">',re.S),soupfile)
        multiple = re.findall(re.compile('<a.*?work\s_work\smultiple\s.*?href="(.*?)">',re.S),soupfile)
        video = re.findall(re.compile('<a.*?work\s_work\sugoku-illust\s.*?href="(.*?)">',re.S),soupfile)
        manga = re.findall(re.compile('<a.*?work\s_work\smanga\smultiple\s.*?href="(.*?)">',re.S),soupfile)
        return single,multiple,manga,video        

class Pixiv_Spider:

    def __init__(self):
        self.tool = Tools()
	self.dl_dir = ''
        self.pic_type = 'jpg'
        self.p_your_collect_url = 'http://www.pixiv.net/bookmark.php'           
        self.p_your_follow_url = 'http://www.pixiv.net/bookmark.php?type=user'      
        self.p_international_url = 'http://www.pixiv.net/ranking_area.php?type=detail&no=6'    

    def Login(self):                        	
        p_login_url = 'https://www.pixiv.net/login.php'        
        data = {                                    
                'mode':'login',
                'skip':1
                }
        data['pixiv_id'] = raw_input('pixiv id:') 
        data['pass'] = raw_input('pixiv password:')
        p_login_data = urllib.urlencode(data)
        p_login_header = { 
                'accept-language':'zh-cn,zh;q=0.8',
                'referer':'https://www.pixiv.net/login.php?return_to=0',
                'user-agent':'mozilla/5.0 (windows nt 10.0; win64; x64; rv:45.0) gecko/20100101 firefox/45.0'
                }
        request = urllib2.Request(
                url = p_login_url,
                data = p_login_data,
                headers = p_login_header
                )
        try:
            cookie_file = 'cookie.txt'                  
            cookie = cookielib.MozillaCookieJar(cookie_file)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))         
            response = opener.open(request)             
            cookie.save(ignore_discard = True,ignore_expires = True)
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "ERROR!!!reason:",e.reason

    def Cookie_Login(self):                         
        cookie_login = cookielib.MozillaCookieJar()
        cookie_login.load('cookie.txt',ignore_discard = True,ignore_expires = True)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_login))
        return opener
    
    def Download_Request(self,opener,make_url,real_url):
            p_download_header = {                          
                'Accept-Language':'zh-CN,zh;q=0.8',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0'
            }
            p_download_header['Referer'] = self.tool.removebig(make_url)                      
            download_request = urllib2.Request(
                url = real_url.group(1),
                headers = p_download_header
                )
            decode_url = opener.open(download_request)
            return decode_url.read()

    def Single(self,opener,pic,dl_dir):
        p_url = self.tool.removesomething('http://www.pixiv.net/' + pic)
        soup = BeautifulSoup(opener.open(p_url),'lxml')
        p_id = (re.search(re.compile('(\d+)',re.S),p_url)).group(1)
        real_url = re.search(re.compile('.*?data-src="(.*?)"',re.S),str(soup.find_all("img",class_="original-image")))
        print 'find real url...\n' + real_url.group(1)
        p_type = self.tool.Pic_Type(real_url.group(1))
        file_pic = open('pixiv_' + p_id + '.' + p_type,'w')                
        file_pic.write(self.Download_Request(opener,p_url,real_url))
        file_pic.close()
        print 'download ok...'

    def Multiple(self,opener,pic,dl_dir):
        p_url = self.tool.removesomething('http://www.pixiv.net/' + pic)
        p_id = (re.search(re.compile('(\d+)',re.S),p_url)).group(1)
        soup = BeautifulSoup(opener.open(p_url),'lxml')
        result_pic_more = re.search(re.compile('</li><li>.*?\s(.*?)P</li>',re.S),str(soup.find_all("ul",class_="meta")))
        print "find multpile" + result_pic_more.group(1)
        for j in range(0,int(result_pic_more.group(1))):
            m_soup = BeautifulSoup(opener.open(self.tool.make_big_url(p_url)+'&page='+str(j)))
            real_url = re.search(re.compile('<img.*?src="(.*?)"/>',re.S),str(m_soup.find_all("img")))
            p_type = self.tool.Pic_Type(real_url.group(1))
            print 'find real rul...\n' + real_url.group(1)    
            file_pic = open('pixiv_' + p_id + '_' + str(j) + '.' + p_type,'w')  
            file_pic.write(self.Download_Request(opener,(self.tool.make_big_url(p_url)+'&page='+str(j)),real_url))
            file_pic.close()
    	    print 'download ok...'

    def Choice_Pixiv(self,opener):
	print ('1.international 2.you follow')
	p_choice = raw_input()
        if (p_choice == '1'):
            try:
                p_page = opener.open(self.p_international_url)
                p_international = p_page.read()
                dl_dir = 'international'
                self.Pixiv_International(opener,p_international,dl_dir)
            except urllib2.URLError,e:
                if hasattr(e,"reason"):
                    print "ERROR!!!reason:",e.reason
        if (p_choice == '2'):
            try:
                p_page = opener.open(self.p_your_follow_url)
                p_your_follow = p_page.read()
                self.Pixiv_Your_Follow(opener,p_your_follow)
            except urllib2.URLError,e:
                if hasattr(e,"reason"):
                    print "ERROR!!!reason:",e.reason

    def Pixiv_International(self,opener,p_international,dl_dir):
        #htmlfile = open("C:\Users\monburan\Desktop\pixiv_int.htm","r")
        pic = self.tool.Pic_Style_M(str(BeautifulSoup(p_international,'lxml')))
        print "This page have Single:"+str(len(pic[0]))+"Multiple:"+str(len(pic[1]))+"Manga:"+str(len(pic[2]))+"Video:"+str(len(pic[3]))
#        print pic[0],pic[1],pic[2]
        for i in pic[0]:            
            self.Single(opener,i,dl_dir)
        for j in pic[1]:
            self.Multiple(opener,j,dl_dir)
        for k in pic[2]:
            self.Multiple(opener,k,dl_dir)

    def Pixiv_Your_Follow(self,opener,p_your_follow):
        soup = BeautifulSoup(p_your_follow,'lxml')
        user_num = re.search(re.compile('(\d+)',re.S),str(soup.find_all(class_="unit-count")))
        print 'you have' + str(user_num.group(1)) + 'following author...'
        if int(user_num.group(1))/48!=0:
            u_p = int(user_num.group(1))/48 + 1
        else :
            u_p = int(user_num.group(1))/48
        for i in range(0,u_p+1):
            f_url = 'http://www.pixiv.net/bookmark.php?type=user&rest=show&p=' + str(i+1)
            self.User_Page(opener,f_url)

    def User_Page(self,opener,f_url):
        soup = BeautifulSoup(opener.open(f_url),'lxml')
        uname_list = re.findall(re.compile('data-user_name="(.*?)"',re.S),str(soup.find_all(class_="userdata")))
        uid_list = re.findall(re.compile('data-user_id="(.*?)"',re.S),str(soup.find_all(class_="userdata")))
        for h in range(0,len(uid_list)):
            user_info = BeautifulSoup(opener.open('http://www.pixiv.net/member_illust.php?id=' + uid_list[h]))
            pic_num = re.search(re.compile('(\d+)',re.S),str(user_info.find(class_="count-badge")))
            print 'author:' + uname_list[h] + 'have' + pic_num.group(1) + 'pic'
            if (int(pic_num.group(1))%20)!=0:
                p = (int(pic_num.group(1))/20) + 1
            else :
                p = int(pic_num.group(1))/20
            for i in range(1,p+1):
                pic = self.tool.Pic_Style_M(str(BeautifulSoup(opener.open(('http://www.pixiv.net/member_illust.php?id=' + uid_list[h]) + '&type=all&p=' + str(i)))))
                print 'Page'+ str(i) + 'have Single:'+ str(len(pic[0])) + 'Multiple:' + str(len(pic[1])) + 'Manga:' + str(len(pic[2])) + 'Video:' + str(len(pic[3]))
                for j in pic[0]:
                    self.Single(opener,j,uid_list[h])
                for k in pic[1]:
                    self.Multiple(opener,k,uid_list[h])
                for l in pic[2]:
	            self.Multiple(opener,l,uid_list[h])

    def Program_Start(self):
        self.Login()
        opener = self.Cookie_Login()
        self.Choice_Pixiv(opener)

if __name__ == '__main__':
    ps = Pixiv_Spider()
    ps.Program_Start()
