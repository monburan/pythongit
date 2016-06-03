import urllib2
from bs4 import BeautifulSoup
import sys

class Scaner():
    
    def geturl(self):
        url = sys.argv[1]
        if len (url and "://") == 0:
            url = "http://" + url

        headers = {
                'user-agent':'mozilla/5.0 (windows nt 10.0; win64; x64; rv:45.0) gecko/20100101 firefox/45.0',
                'accept-language':'zh-cn,zh;q=0.8'
                }
        request = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response,'lxml')
        print soup
    def Spider(self,soup):
        print soup
        
    def Main():
        target = self.url()
        print type(target)
        self.Spider(target)

if __name__ == "__main__":
    pg = Scaner()
    pg.geturl()
