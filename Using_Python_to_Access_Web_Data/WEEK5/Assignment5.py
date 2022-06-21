import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#http://py4e-data.dr-chuck.net/comments_42.xml
url = input('Enter location: ')
print('Retrieving', url)
xml=urllib.request.urlopen(url, context=ctx).read()
print(type(xml))
print('Retrieved', len(xml), 'characters')
#print(xml.decode())
lst=list()
tree = ET.fromstring(xml)
counts= tree.findall('comments/comment')
#print(counts)
print('Count :',len(counts)) 
for count in counts:
    lst.append(int(count.find('count').text))
print('Sum :',sum(lst))
