import urllib, urllib2, sys
import ssl

#
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=RHMzvoPhVyN9IbeDk8vj1huq&client_secret=E4Dqh1eRcUdcRCCN4f9nvVnfgRL3teDR'
head = {'Content-Type':'application/json; charset=UTF-8'}

request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)

content = response.read()
if (content):
    print(content)
