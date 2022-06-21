from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
#import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# http://py4e-data.dr-chuck.net/comments_42.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count=0
nums=list()
tags = soup('span')
for tag in tags:
    #n=re.findall('[0-9]+',str(tag.contents[0]))
    count+=1
    nums.append(tag.contents[0])
#print(nums)
for i in range(len(nums)):
    nums[i]=int(nums[i])
print('Count ',count)
print('Sum ',sum(nums))