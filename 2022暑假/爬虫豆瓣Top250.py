#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
import bs4
import pprint

def findWeb(html,hea):
    #i=1
    if html.status_code!='200':
        #print(html.text)
        html_all=html.text
        #pprint.pprint(html_all)
        new_url=re.compile(r'<a href="(.*?)">')
        link=re.findall(new_url,html_all)
        #print(link)
        for html in link:
            #print(html)
            result=re.findall('\d',html)
            #print(result)
            if len(result)>=6 and html.find('class')==-1:
                #print(html)
                #print(i)
                #i=i+1
                connect_fWeb(html,hea)
            else:
                #print('Something wrong !!!!!')
                pass
        #print(i)
    else:
        print('Something wrong !!!!!')
        pass

def connect_fWeb(html,hea):
    try:
        end_html=requests.get(html,headers=hea)
        #print(html.text)
        html_all=end_html.text
        re_name=re.compile(r'<span property="v:itemreviewed">(.*)</span>')
        re_director=re.compile(r'v:directedBy">(.*)</a>')
        re_author=re.compile(r'>编剧</span>:(.*)</a></span></span><br/>')
        re_actor=re.compile(r'<meta property="video:actor" content="(.*)" />')
        re_title=re.compile(r'<span property="v:genre">(.*)</span>')
        re_country=re.compile(r'<span class="pl">制片国家/地区:</span>(.*)<br/>')
        re_language=re.compile(r'<span class="pl">语言:</span>(.*)<br/>')
        re_start_move=re.compile(r'<span property="v:initialReleaseDate" content="(.*)</span> / <span')
        re_move_howlong=re.compile(r'<span class="pl">片长:</span> <span property="v:runtime" content="(.*)">')
        re_another_name=re.compile(r'<span class="pl">又名:</span>(.*)<br/>')
        re_score=re.compile(r'property="v:average">(.*)</strong>')
        re_brief_introduction=re.compile(r'<span class="all hidden" style="display: inline;">(.*)</span>')
        name=re.findall(re_name,html_all)
        name=''.join(name)
        name=name+".txt"
        director=re.findall(re_director,html_all)
        director=''.join(director)
        author=re.findall(re_author,html_all)
        author=''.join(author)
        author = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",author)
        author = re.sub('[a-zA-Z]',' ',author)
        author = re.sub('[0-9]','',author)
        actor=re.findall(re_actor,html_all)
        actor='/'.join(actor)
        title=re.findall(re_title,html_all)
        title=''.join(title)
        title = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",title)
        title = re.sub('[a-zA-Z]','/',title)
        title=title.replace("//////////////////////","/")
        country=re.findall(re_country,html_all)
        country=''.join(country)
        language=re.findall(re_language,html_all)
        language=''.join(language)
        start_move=re.findall(re_start_move,html_all)
        start_move=''.join(start_move)
        #print(start_move)
        #start_move=str(''.join(start_move))
        #print(start_move)
        move_howlong=re.findall(re_move_howlong,html_all)
        move_howlong=''.join(move_howlong)
        another_name=re.findall(re_another_name,html_all)
        another_name=''.join(another_name)
        score=re.findall(re_score,html_all)
        score=''.join(score)
        brief_introduction=re.findall(re_brief_introduction,html_all)
        brief_introduction=''.join(brief_introduction)
        print(name)
        f=open(name,"w+")
        f.writelines("导演:"+director+"\n")
        f.writelines("编剧:"+author+"\n")
        f.writelines("主演:"+actor+"\n")
        f.writelines("类型:"+title+"\n")
        f.writelines("制片国家:"+country+"\n")
        f.writelines("语言:"+language+"\n")
        f.writelines("上映时间:"+start_move+"\n")
        f.writelines("片长:"+move_howlong+"\n")
        f.writelines("又名:"+another_name+"\n")
        f.writelines("豆瓣评分:"+score+"\n")
        f.close()
    except:
        pass

def movie(html):
    try:
        bf = bs4.BeautifulSoup(html.content, 'html.parser')
        #获取标题
        
    except:
        pass


def main():
    url='https://movie.douban.com/top250?start='
    hea={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'}

    for i in range(0,5):
        ys_url=url+str(i*5)
        #print(ys_url)
        html=requests.get(ys_url,headers=hea)
        #print(html)
        findWeb(html,hea)

if __name__=="__main__":
    main()