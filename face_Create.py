# encoding:utf-8
import json
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
    result = json.loads(content)
    print(result['access_token'])

    # access_token = result['access_token']

    '''
    人脸检测与属性分析
    
    '''

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

    params = "{\"image\":\"9f55e46e9ba2ecccda24a9f5b4d84da7\",\"image_type\":\"FACE_TOKEN\",\"face_field\":\"expression,faceshape,facetype\"}"

    access_token = result['access_token']
    request_url = request_url + "?access_token=" + access_token
    request = urllib2.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        print content






