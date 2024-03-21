import re
import json
import requests
from pprint import pprint #格式化输出

url='https://www.acfun.cn/v/ac35510357'
headers={
    #用户代理 表示浏览器基本身份标识
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
}

response=requests.get(url=url,headers=headers)

#print(response.text)

title=re.findall('<title >(.*?) - AcFun弹幕视频网',response.text)[0]
html_data=re.findall(' window.pageInfo = window.videoInfo = (.*?);',response.text)[0]
#re.findall('window.pageInfo')
#print(title)
#print(html_data)
json_data=json.loads(html_data)
#print(json_data)
#pprint(json_data)
m3u8_url=json.loads(json_data['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['backupUrl'][0]
#print(m3u8_url)
m3u8_data=requests.get(url=m3u8_url,headers=headers).text
m3u8_data=re.sub('#E.*','',m3u8_data).split()
print(m3u8_data)
for ts in m3u8_data:
    ts_url='https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/'+ts
    print(ts_url)
    ts_content=requests.get(url=ts_url,headers=headers).content
    with open(title + '.mp4' , mode='ab') as f:
        f.write(ts_content)
    print(ts_url)