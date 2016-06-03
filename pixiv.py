#coding:UTF-8

__author__ = 'monburan'
__version__ = '0.10 only_international'
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

    def Pic_Type(self,real_url):                    #区分图片分辨率
        p_type = re.search(re.compile('png',re.S),real_url)
        if p_type == None:
            self.pic_type = 'jpg'
            return self.pic_type
        else:
            self.pic_type = 'png'
            return self.pic_type

    def Pic_Style(self,soupfile):
        single = re.search(re.compile('<.*?work\s_work\s".*?href="(.*?)">',re.S),soupfile)
        multiple = re.search(re.compile('<a.*?work\s_work\smultiple\s.*?href="(.*?)">',re.S),soupfile)
        video = re.search(re.compile('<a.*?work\s_work\sugoku-illust\s.*?href="(.*?)">',re.S),soupfile)
        manga = re.search(re.compile('<a.*?work\s_work\smanga\smultiple\s.*?href="(.*?)">',re.S),soupfile)

        return single,multiple,manga,video

    def Pic_Style_M(self,soupfile):
        single = re.findall(re.compile('<.*?work\s_work\s".*?href="(.*?)">',re.S),soupfile)
        multiple = re.findall(re.compile('<a.*?work\s_work\smultiple\s.*?href="(.*?)">',re.S),soupfile)
        video = re.findall(re.compile('<a.*?work\s_work\sugoku-illust\s.*?href="(.*?)">',re.S),soupfile)
        manga = re.findall(re.compile('<a.*?work\s_work\smanga\smultiple\s.*?href="(.*?)">',re.S),soupfile)
        return single,multiple,manga,video

class Pixiv_Spider:

    def __init__(self):
        self.tool = Tools()
        self.p_id = ''
        self.p_pw = ''
        self.p_choice = ''
        self.dl_dir = ''
        self.pic_type = ''
        self.p_your_collect_url = 'http://www.pixiv.net/bookmark.php'           #个人收藏url
        self.p_your_follow_url = 'http://www.pixiv.net/bookmark.php?type=user'      #关注页面url
        self.p_international_url = 'http://www.pixiv.net/ranking_area.php?type=detail&no=6'     #国际排行榜url
        self.p_today_hot_url = 'http://www.pixiv.net/ranking.php?mode=daily'        #今日热点url

    def Login(self):                        #处理登录所需要的请求信息
        p_login_url = 'https://www.pixiv.net/login.php'        
        data = {                                    #登录所要post的信息
                'mode':'login',
                'skip':1
                }
        data['pixiv_id'] = self.p_id                #传入登录id以及password
        data['pass'] = self.p_pw
        p_login_data = urllib.urlencode(data)
        p_login_header = {                          #头信息
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
            cookie_file = 'cookie.txt'                  #生成cookie
            cookie = cookielib.MozillaCookieJar(cookie_file)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))         
            response = opener.open(request)             #登录
            cookie.save(ignore_discard = True,ignore_expires = True)
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print "登录失败？？？",e.reason
    
    def Download_Request(self,opener,make_url,real_url):
            p_download_header = {                          #头信息
                'Accept-Language':'zh-CN,zh;q=0.8',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0'
            }
            p_download_header['Referer'] = self.tool.removebig(make_url)        #将处理过的referer加入header，没有referer会显示403               
            download_request = urllib2.Request(
                url = real_url.group(1),
                headers = p_download_header
                )
            decode_url = opener.open(download_request)
            return decode_url.read()

    def Cookie_Login(self):                         #读取之前登陆生成的cookie
            cookie_login = cookielib.MozillaCookieJar()
            cookie_login.load('cookie.txt',ignore_discard = True,ignore_expires = True)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_login))
            return opener

    def Choice_Pixiv(self,opener):     #选择要跳转到的页面
        if (self.p_choice == '1'):
            try:
                p_page = opener.open(self.p_international_url)
                p_international = p_page.read()
                dl_dir = 'international'
                self.Pixiv_International(opener,p_international,dl_dir)
            except urllib2.URLError,e:
                if hasattr(e,"reason"):
                    print "连接错误:",e.reason
        if (self.p_choice == '2'):
            try:
                p_page = opener.open(self.p_your_follow_url)
                p_your_follow = p_page.read()
                self.Pixiv_Your_Follow(opener,p_your_follow)
            except urllib2.URLError,e:
                if hasattr(e,"reason"):
                    print "连接错误:",e.reason

    def Pixiv_International(self,opener,p_international,dl_dir):
        soup = BeautifulSoup(p_international)
        for i in range(1,101):                              #已知pixiv国际榜的排名为100名，用for循环来完成
            get_information = str(soup.find(id=i))          #通过bs处理html将我们所需要的信息大体提取出来
            pic_style = self.tool.Pic_Style(get_information)
            if pic_style[3] == None:
                if pic_style[2] == None:                   #判断是否为manga
                    if pic_style[1] == None:                     #判断是否为多图
                        p_num = '1'
                        p_url = self.tool.removesomething('http://www.pixiv.net/' + pic_style[0].group(1))
                        print "报告！前方发现单张图片..."
                        p_id = self.Download_Data(i,get_information,p_url,opener,dl_dir)
                        self.Download_Pic(p_num,opener,p_url,p_id,dl_dir)
                    else:
                        p_num = 'more'
                        p_url = self.tool.removesomething('http://www.pixiv.net/' + pic_style[1].group(1))
                        print "报告！前方发现多张图片..."
                        p_id = self.Download_Data(i,get_information,p_url,opener,dl_dir)
                        self.Download_Pic(p_num,opener,p_url,p_id,dl_dir)
                else:
                    p_num = 'more'
                    p_url = self.tool.removesomething('http://www.pixiv.net/' + pic_style[2].group(1))
                    print "报告！前方发现多张漫画..."
                    p_id = self.Download_Data(i,get_information,p_url,opener,dl_dir)
                    self.Download_Pic(p_num,opener,p_url,p_id,dl_dir)
            else:
                print "报告！前方这是张动图...无能为力啊...╮(╯▽╰)╭"
                
    def Pixiv_Your_Follow(self,opener,p_your_follow):
        soup = BeautifulSoup(p_your_follow)
        user_num = re.search(re.compile('(\d+)',re.S),str(soup.find_all(class_="unit-count")))
        print '共有' + str(user_num.group(1)) + '位正在关注的画师...'
        if int(user_num.group(1))/48!=0:
            u_p = int(user_num.group(1))/48 + 1
        else :
            u_p = int(user_num.group(1))/48
        for i in range(1,u_p+1):
            f_url = 'http://www.pixiv.net/bookmark.php?type=user&rest=show&p=' + str(i)
            self.User_Data(opener,f_url)

    def User_Data(self,opener,f_url):
        soup = BeautifulSoup(opener.open(f_url))
        uname_list = re.findall(re.compile('data-user_name="(.*?)"',re.S),str(soup.find_all(class_="userdata")))
        uid_list = re.findall(re.compile('data-user_id="(.*?)"',re.S),str(soup.find_all(class_="userdata")))
        for h in range(0,len(uid_list)):
            user_name = uname_list[h]
            user_id = uid_list[h]
            user_page = 'http://www.pixiv.net/member_illust.php?id=' + user_id
            os.mkdir(r'E:/pixivdata/'+user_id+'/')
            user_info = BeautifulSoup(opener.open(user_page))
            pic_num = re.search(re.compile('(\d+)',re.S),str(user_info.find(class_="count-badge")))
            print '画师:' + user_name + '共有' + pic_num.group(1) + '幅作品'
            if (int(pic_num.group(1))%20)!=0:
                p = (int(pic_num.group(1))/20) + 1
            else :
                p = int(pic_num.group(1))/20
            massage1 = []
            massage2 = []
            massage3 = []
            for i in range(1,p+1):
                pic_s = self.tool.Pic_Style_M(str(BeautifulSoup(opener.open(user_page + '&type=all&p=' + str(i)))))
                print '第'+str(i)+'页共有' + str(len(pic_s[0])) + '张单图'
                for j in range(0,len(pic_s[0])):
                    p_num = '1'
                    pic_s[0][j] = self.tool.removesomething('http://www.pixiv.net/' + pic_s[0][j])
                    p_id = re.search(re.compile('(\d+)',re.S),pic_s[0][j])
                    self.Download_Pic(p_num,opener,pic_s[0][j],p_id.group(1),user_id)
                print '第'+str(i)+'页共有' + str(len(pic_s[1])) + '套多图'
                for k in range(0,len(pic_s[1])):
                    p_num = 'more'
                    pic_s[1][k] = self.tool.removesomething('http://www.pixiv.net/' + pic_s[1][k])
                    p_id = re.search(re.compile('(\d+)',re.S),pic_s[1][k])
                    self.Download_Pic(p_num,opener,pic_s[1][k],p_id.group(1),user_id)
                print '第'+str(i)+'页共有' + str(len(pic_s[2])) + '套漫画'
                for l in range(0,len(pic_s[2])):
                    p_num = 'more'
                    pic_s[2][l] = self.tool.removesomething('http://www.pixiv.net/' + pic_s[2][l])
                    p_id = re.search(re.compile('(\d+)',re.S),pic_s[2][l])
                    self.Download_Pic(p_num,opener,pic_s[2][l],p_id.group(1),user_id)
                if len(video) == 0 :
                    print '没有动图...'
                else:
                    print'第'+str(i)+'页共有' + str(len(video)) + '张动图,主动放弃...'
    def Download_Data(self,i,get_information,p_url,opener,dl_dir):
        #通过使用正则表达式再处理一遍经过bs处理的html代码，找到需要的信息(url,title,user)
        result_title = re.search(re.compile('<a href=".*?>(.*?)</a>',re.S),get_information)
        result_id = re.search(re.compile('<a class.*?illust_id=(.*?)">',re.S),get_information) 
        result_user = re.search(re.compile('<span class.*?>(.*?)</span>',re.S),get_information)
        
        p_rank = str(i)
        p_id = result_id.group(1)
        p_title = result_title.group(1)
        p_user = result_user.group(1)
        print "RANK #" + p_rank + "\nPixiv ID:" + p_id + "\nTitle:" + p_title +"\nUser:" + p_user

        file_data = open('E:/pixivdata/' + dl_dir + '/pixiv_' + p_id + '.txt','w')     #创建信息文件

        massage = [                         #保存信息
            'rank:' + p_rank +'\n',
            'id:' + p_id + '\n',
            'title:' + p_title + '\n',
            'user:' + p_user + '\n',
            'url:' + p_url
            ]

        file_data.writelines(massage)
        file_data.close()
        print "报告！pixiv信息保存成功..."           #将信息以txt格式保存下来
        return p_id

    def Download_Pic(self,p_num,opener,p_url,p_id,dl_dir):
        if p_num == '1':
            soup = BeautifulSoup(opener.open(p_url))
            real_url = re.search(re.compile('.*?data-src="(.*?)"',re.S),str(soup.find_all("img",class_="original-image")))
            print '成功找到大图链接(ˉ﹃ˉ)...\n' + real_url.group(1)
            p_type = self.tool.Pic_Type(real_url.group(1))
            file_pic = open('E:/pixivdata/' + dl_dir + '/pixiv_' + p_id + '.' + p_type,'wb')                
            file_pic.write(self.Download_Request(opener,p_url,real_url))
            file_pic.close()
            print '成功下载到本地(/≧▽≦)/...'
            
        if p_num == 'more':
            soup = BeautifulSoup(opener.open(p_url))
            result_pic_more = re.search(re.compile('</li><li>.*?\s(.*?)P</li>',re.S),str(soup.find_all("ul",class_="meta")))
            print "发现图片" + result_pic_more.group(1) + "张...⊙▽⊙"
            for j in range(0,int(result_pic_more.group(1))):
                make_url = self.tool.make_big_url(p_url)+'&page='+str(j)        #生成多张的url
                m_soup = BeautifulSoup(opener.open(make_url))
                real_url = re.search(re.compile('<img.*?src="(.*?)"/>',re.S),str(m_soup.find_all("img")))
                p_type = self.tool.Pic_Type(real_url.group(1))
                print '成功找到大图链接（ˉ﹃ˉ）...\n' + real_url.group(1)     #下载图片并保存
                file_pic = open('E:/pixivdata/' + dl_dir + '/pixiv_' + p_id + '_' + str(j) + '.' + p_type,'wb')  
                file_pic.write(self.Download_Request(opener,make_url,real_url))
                file_pic.close()
                print '成功下载到本地(/≧▽≦)/...'        

    def Program_Start(self):
        self.Login()
        opener = self.Cookie_Login()
        self.Choice_Pixiv(opener)

ps = Pixiv_Spider()
ps.p_id = raw_input('请输入你的pixiv id:')
ps.p_pw = raw_input('请输入你的pixiv密码:')
print ('1.进入国际排行榜 2.进入你的关注 3.进入你的收藏')
ps.p_choice = raw_input()
ps.Program_Start()
