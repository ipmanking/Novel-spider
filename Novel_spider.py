#　-*- conding:utf-8 -*-
import urllib.request
import re 


#　分析网页
#　获取主页面
#　获取章节的超链接
#　获取章节的超链接源码
#  获取小说内容
#  下载小说

def getNovelContent():
    html = urllib.request.urlopen('http://www.quanshuwang.com/book/44/44683').read()
    html = html.decode('gbk')
    # print(html) # 输出网页源码
    # 获取
    # "<li><a href="http://www.quanshuwang.com/book/44/44683/15379609.html" title="引子 穿越的唐家三少，共2744字">引子 穿越的唐家三少</a></li>"
    req = '<li><a href="(.*?)" title="(.*?)">(.*?)</a></li>'
    urls = re.findall(req, html)
    for url in urls:
        novel_url = url[0] # 小说的章节超链接
        title = url[1] # 小说的章节名
        chapt = urllib.request.urlopen(novel_url).read()
        chapt_html = chapt.decode('gbk')
        req = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">'
        # 多汗行匹配
        req = re.compile(req, re.S)
        chapt_content = re.findall(req, chapt_html)
        # print(chapt_content[0])
        chapt_content = chapt_content[0].replace('<br />', '')
        chapt_content = chapt_content.replace('&nbsp;', '')
        # print(chapt_content)
        # print(chapt_content)
        # print("正在下载%s"%novel_url)
        print("正在下载%s"%title)
        # 下载小说(1)
        # f = open('{}.txt'.format(title),'w')
        # f.write(chapt_content)
        # f.close()
        # 下载小说(2)
        with open('{}.txt'.format(title),'w') as f :
            f.write(chapt_content)
            f.close()
 
getNovelContent()