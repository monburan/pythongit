__author__ = 'monburan'
#coding:utf-8
#vim: set fileencoding=utf-8
import urllib
import urllib2
import re
import io

class Tool:

  removeImg = re.compile('<img.*?>| {7}|')
  removeAddr = re.compile('<a.*?>|</a>')
  replaceLine = re.compile('<tr>|<div>|</div>|</p>')
  replaceTd = re.compile('<td>')
  replacePara = re.compile('<p.*?>')
  replaceBR = re.compile('<br><br>|<br>')
  removeExtraTag = re.compile('<.*?>')
  
  def removesomething(self,x):
    x = re.sub(self.removeImg,"",x)
    x = re.sub(self.removeAddr,"",x)
    x = re.sub(self.replaceLine,"\n",x)
    x = re.sub(self.replaceTd,"\t",x)
    x = re.sub(self.replacePara,"\n",x)
    x = re.sub(self.replaceBR,"\n",x)
    x = re.sub(self.removeExtraTag,"",x)
    return x.strip()


class BDTB:

  def __init__(self,baseUrl,seeLz,floorTag):
    self.baseURL = baseUrl
    self.seeLz = '?see_lz=' + str(seeLz)
    self.tool = Tool()
    self.file = None
    self.floor = 1
    self.defaultTitle = "Baidu Tieba"
    self.floorTag = floorTag
  def getPage(self,pageNum):
    try:
      url = self.baseURL + self.seeLz + '&pn=' + str(pageNum)
      request = urllib2.Request(url)
      response = urllib2.urlopen(request)
      return response.read().decode('utf-8')
    except urllib2.URLError,e:
      if hasattr(e,"reason"):
        print "Warning,Error:",e.reason
        return None

  def getTitle(self,page):
    pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
    result = re.search(pattern,page)
    if result:
      return result.group(1).strip()
    else:
      return None
  def getPageNum(self,page):
    pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
    result = re.search(pattern,page)
    if result:
      return result.group(1).strip()
    else:
      return None

  def getContent(self,page):
    pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
    items = re.findall(pattern,page)
    contents = []
    for item in items:
      content = "\n" + self.tool.removesomething(item) + "\n"
      contents.append(content.encode('utf-8'))
    return contents

  def setFileTitle(self,title):
    try:
      if title is not None:
        self.file = io.open('User/monburan/Desktop/python/spiderDate/' + title +'.txt' , 'w+',encoding = 'utf-8')
      else:
        self.file = open('User/monburan/Desktop/python/spiderDate/'+ self.defaultTitle + '.txt' , 'w+')
    except IOError ,e:
      print "File Error is :" ,e
  
  def writeData(self,contents):
    for item in contents:
      if self.floorTag == '1':
        floorLine = "\n" + str(self.floor) + "Floor - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
        self.file.write(floorLine)
      print item.decode('utf-8')
      self.file.write(item)
      
      self.floor += 1

  def programStart(self):
    indexPage = self.getPage(1)
    pageNum = self.getPageNum(indexPage)
    title = self.getTitle(indexPage)
    self.setFileTitle(title)
    if pageNum == None:
      print "Url Error,Please Try Again"
      return
    try:
      print "Title Is < %s>"%(title)
      print "Have " +str(pageNum) + " Page"
      for i in range(1,int(pageNum)+1):
        print "Writing " + str(i) + " page"
        page = self.getPage(i)
        contents = self.getContent(page)
        self.writeData(contents)
    except IOError,e:
      print "Writing Error" + e.message
    finally:
      print "success!!!"


tzid = raw_input("Please Innput Id -> http://tieba.baidu.com/p/")
baseURL = 'http://tieba.baidu.com/p/'+str(tzid)
seeLz = raw_input("If You Want See LZ Please Input 1 , If Not Input 0\n")
floorTag = raw_input("If You Want Write Floor Info Please input 1 , If not Input 0\n")
bdtb = BDTB(baseURL,seeLz,floorTag)
bdtb.programStart()
