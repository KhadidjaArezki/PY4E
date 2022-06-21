import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# http://py4e-data.dr-chuck.net/comments_42.json
url=input('Enter location: ')
print('Retrieving', url)
uh=urllib.request.urlopen(url, context=ctx)
data=uh.read().decode()
print('Retrieved ',len(data),'characters')
try:
    js=json.loads(data)
except:
    js=None
#print(json.dumps(js, indent=2))
lst=list()
print('Count: ',len(js['comments']))
for user in js['comments']:
    lst.append(int(user['count']))
print('Sum: ',sum(lst))