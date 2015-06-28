#coding:utf-8
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
import MySQLdb
import re
import time

def create_HTML(row):
    #print type(row)
    path='E:apache/htdocs/conn/id/'
    page = row[0]+1
    path = path+str(page)+'.html'
    #print path,row[4]
    html = open(path,'w')
    html.write("""
<html>
<head>
  <title>结果~~~~||DCY</title>
  <meta charset="utf-8">
  <style>img{float:left;margin:5px;}</style>
</head>
<body bgcolor="#e7e7e7" text="red" background="0.jpg">
""")
    html.write('<p><h1 color="orange">文章： '+row[4].encode('utf-8')+'</h1><br/>')
    html.write('<h1>作者： '+row[10].encode('utf-8')+'<br/></h1>')
    html.write('<h3>转发数：'+str(row[3])+'   评论数：'+str(row[1])+'   赞：'+str(row[2])+'</h3>')
    html.write('<h3>时间：'+str(row[6])+'<br/></h3></p>')
    if row[13]!='none':
        html.write('<p><h2>原文文章： '+row[11].encode('utf-8')+'</h2><br/>')
        html.write('<h1>原文作者： '+row[12].encode('utf-8')+'<br/></h1>')
        html.write('<h3>原文转发数：'+str(row[9])+'   原文评论数：'+str(row[8])+'   赞原文：'+str(row[7])+'</h3>')
        url = "http://weibo.com/"+row[13]
        html.write('<a href='+url.encode('utf-8')+'> 原微博作者地址 </a></body>')
        
        
    

conn = MySQLdb.Connect("localhost", "root", "dcy0701", "weibo", charset="utf8")
cur =conn.cursor()

sql="select * from think_love"
if True:
    cur.execute(sql)
    results = cur.fetchall()#格式是元组
    for row in results:
        id = row[0]
        print id
        create_HTML(row)
#except:
    #print 'error'
    
