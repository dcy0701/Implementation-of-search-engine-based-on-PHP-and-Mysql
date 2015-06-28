#coding:utf-8
import urllib2
from WeiboCN import Fetcher
import MySQLdb
import re
import time
#from BeautifulSoup import BeautifulSoup as bs4
#list1 =[]
global val
val = 1
def getcontent(id_1,object,page):
    global val
    url = "http://weibo.cn/"+id_1+page
    #print '??-->>',url
    f = object.fetch(url)
    #print f
    
    username_pat = re.compile(r'(?<=title>).*?(?=title)')
    username = ''.join(username_pat.findall(f))[:-11]
    #print username,id_1

    weibo_pat = re.compile(r'(?<=div class="c").*?(?=div class="s")')
    list3 = weibo_pat.findall(f)
    #print list3[0]
    for item in list3:
        pat = re.compile(r'(?<=转发了)(.*?)(?=的微博:)')
        pat1 = re.compile(r'(?<=\">)(.*?)(?=</a>)')
        pat3 = re.compile(r'(?<=cn/)(.*?)(?=">)')
        pat2 = re.compile(r'[A-Za-z0-9]{3,11}')
        text = ''.join(pat.findall(item))
        text2 = ''.join(pat3.findall(text))
        text3 = ''.join(pat2.findall(text2))
        
        if text3 == '':
            text3 = 'none'
        user_from = text3
        #print text3
        sou_name = ''.join(pat1.findall(''.join(pat.findall(item))))
        if sou_name == '':
            sou_name = 'none'
        #import time
        #time.sleep(1)
        #print sou_name.decode('utf-8')
        sourse_content = content = 'null'
        s_num_pl = s_num_zf = S_num_zan = num_pl = num_zf =num_zan = '0'
        if user_from != 'none':
            pa = re.compile(r'(?<=原文评论\[)\d{0,7}')
            pa1 = re.compile(r'(?<=原文转发\[)\d{0,7}')
            pa2 = re.compile(r'(?<=cmt">赞\[)\d{0,7}')
            s_num_pl = ''.join(pa.findall(item))
            s_num_zf = ''.join(pa1.findall(item))
            S_num_zan = ''.join(pa2.findall(item))
            p = re.compile(r'(?<=评论\[)\d{0,7}')
            p1 = re.compile(r'(?<=转发\[)\d{0,7}')
            p2 = re.compile(r'(?<=">赞\[)\d{0,7}')
            num_pl = ''.join(p.findall(item)[1])
            num_zf = ''.join(p1.findall(item)[1])
            num_zan = ''.join(p2.findall(item)[1])

            pat_c = re.compile(r'(?<=ctt">)(.*?)(?=span)')
            temp = ''.join(pat_c.findall(item))
            pat_d = re.compile(r'(?<=href=")(.*?)(?=">)')
            for i in pat_d.findall(item):
                #print i
                temp = temp.replace(i,'')
            temp = temp.replace('<a href="">','')
            temp = temp.replace('</a>','')
            pat_3 = re.compile(r'<a.*</a>')
            for i in pat_3.findall(temp):
                temp = temp.replace(i,'')
            pat_f = re.compile(r'(?<=http)(.*?)(?=</)')
            temp_1 = ''.join(pat_f.findall(temp))
            temp = temp.replace(temp_1,'')
            
            temp = temp.replace('http','')
            temp = temp.replace('</','')

            #print temp.decode('utf-8')
            sourse_content = temp
            pat_cc = re.compile(r'(?<=转发理由:</span>)(.*?)(?=">赞)')
            content = ''.join(pat_cc.findall(item))
            content = content + '">'
            pat_dd = re.compile(r'(?<=href=")(.*?)(?=">)')
            for i in pat_dd.findall(content):
                content = content.replace(i,'')
            content = content.replace('<a href="">','')
            content = content.replace('</a>','')
            content = content.replace('&nbsp;','')
            pat_ff = re.compile(r'(?<=http)(.*?)(?=</)')
            temp_2 = ''.join(pat_ff.findall(content))
            content = content.replace(temp_2,'')
        else:
            s_num_pl = '0'
            S_num_zf = '0'
            s_num_zan = '0'
            pa = re.compile(r'(?<=评论\[)\d{0,7}')
            pa1 = re.compile(r'(?<=转发\[)\d{0,7}')
            pa2 = re.compile(r'(?<=">赞\[)\d{0,7}')
            num_pl = ''.join(pa.findall(item))
            num_zf = ''.join(pa1.findall(item))
            num_zan = ''.join(pa2.findall(item))
            pat_g = re.compile(r'(?<=class="ctt")(.*?)(?=</span>)')
            content = ''.join(pat_g.findall(item))
            pat_dd = re.compile(r'(?<=href=")(.*?)(?=">)')
            for i in pat_dd.findall(content):
                content = content.replace(i,'')
            content = content.replace('<a href="">','')
            content = content.replace('</a>','')
            content = content.replace('&nbsp;','')
            pat_ff = re.compile(r'(?<=http)(.*?)(?=</)')
            temp_3 = ''.join(pat_ff.findall(content))
            content = content.replace(temp_3,'')
            content = content[1:]
        #print sourse_content.decode('utf-8'),'1111'
        #print content,type(content),'????????here!'
        #print content.decode('utf-8'),'content'
        #print s_num_pl , s_num_zf , S_num_zan , num_pl , num_zf , num_zan
        pat_1 = re.compile(r'(?<=ct">)(.*?)(?=&nbsp)')
        time1 = ''.join(pat_1.findall(item))
        #print time.decode('utf-8'),'time',len(time)
        #print time1,type(time1)
        #print time1
        if len(time1)==12:
            time_1 = time.strftime("%y-%m-%d ")
            time1 = '20' + time_1 + time1[-5:] + ':00'
        
        elif len(time1)==16:
            time1 = '2015-' + time1[:2] + '-' + time1[5:7] + ' ' + time1[-5:] + ':00'
        elif len(time1)<=11:
            time1 = "0000-00-00 00:00:00"
            pass
            #time2 = time.strftime("%y-%m-%d %H:%i:%s")
            #temp = int(time2[-5:-3])-int(time1[0:2])
        else:
            time1 = time1
        #print time1,len(time1)
        #print int(num_pl),int(num_zan),int(num_zf),content,time1,int(S_num_zan),int(s_num_pl),int(s_num_zf)\
                 #,username,sourse_content,sou_name,user_from
        #print value,'value'
        #print time1,'??????',id_1,len(id_1)
        #save_db(value)
        conn = MySQLdb.Connect("localhost", "root", "dcy0701", "weibo", charset="utf8")
        cur = conn.cursor()
        #if True:
        try:
            #cur.execute('delete from test1')
            #cur.execute('insert into jjj values (%s,%s,%s,%s,%s)',(num_pl,num_zan,int(num_pl),time1,content))
            #cur.execute('insert into mytable values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            #(val,int(num_pl),int(num_zan),int(num_zf),content,time1,int(S_num_zan),int(s_num_pl),int(s_num_zf),username,sourse_content,sou_name,user_from))
            cur.execute('insert into think_test values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(val,int(num_pl),int(num_zan),int(num_zf),content,time1,int(S_num_zan),int(s_num_pl),int(s_num_zf),username,sourse_content,sou_name,user_from))
            val = val+1
        except:
            #'''(id,cout_comment,cout_like,cout_report,content,date) '''
            print 'error'
        conn.commit()
        #val = val+1
        print val,
        cur.close()
        conn.close()
def getallpage(item,object):
    page = ''
    for i in range(10):
        if i == 0:
            page = ''
        else:
            page = '?page=' + str(i)
        #print i,page
        getcontent(item,object,page)
    
def save_db(value):
    conn = MySQLdb.Connect("localhost", "root", "dcy0701", "weibo", charset="utf8")
    cur = conn.cursor()
    cur.execute('insert into my (cout_comment,cout_like,cout_report,content,date,sourse_like,sourse_comment,\
sourse_report,name,sourse_content,sourse_name,user_from)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',value)
    #except:
        #print 'data error!!!'
    conn.commit()
    cur.close()
    conn.close()
    
def geturl_uidlist(object):
    page = 1
    uid_list = ['3169591693','1966861553','3193701710','2260079222','678107223'\
                ,'2748941561','2991768953','3463922044','1777566953','2860391154'\
                ,'2072338567','3792967965','1909177521','2857054713','1778524065'\
                ,'121109851','2062754963','3686772403']
    for item in uid_list:
        uid = item
        #uid = '1966861553'
        for iter in range(10):
            page = iter + 1
            url = "http://weibo.cn/"+uid+"/fans?page=" + str(page)
            res = object.fetch(url)
            #print res
            #print type(res)
            pat1 = re.compile(r'(?<=uid=)\d{0,11}')
            list1 = pat1.findall(res)
            list1 = list1[1:-1]
            print list1
            #print list1
            for i in list1:
                getallpage(i,object)

if __name__=='__main__':
    LogIner = Fetcher()
    LogIner.login('username','password','cookies.lwp')
    geturl_uidlist(LogIner)

