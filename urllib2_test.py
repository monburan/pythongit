import urllib2

url = 'http://tool.chinaz.com/subdomain/'
page = urllib2.urlopen(url)
print page.read()
