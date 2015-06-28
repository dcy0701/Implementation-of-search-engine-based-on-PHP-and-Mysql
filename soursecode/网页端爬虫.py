#-*- coding:utf-8 -*-
import jieba
import urllib
import urllib2
import re
from bs4 import BeautifulSoup


## main模块

def fenci():
    str_a = raw_input('请输入搜索内容:')
    #str_a = '请输入搜索内容:'
    #print type(str_a)
    seg_list = jieba.cut(str_a,cut_all = False)
    #print ' '.join(seg_list)
    return ' '.join(seg_list)

def search_weibo(url):
    #url = 'http://s.weibo.com/weibo/%25E5%2591%25A8%25E7%25A5%2589%25E6%2580%2580&Refer=index'
    url = 'http://s.weibo.com/weibo/%E8%91%A3%E5%B4%87%E6%B4%8B&Refer=index'
    #url = 'http://s.weibo.com/weibo/%25E5%25BC%25A0%25E5%25A9%25B7?topnav=1&wvr=6&b=1'
    #url = 'http://www.weibo.com/u/3075975003?from=myfollow_all'
    page = urllib.urlopen(url)
    content = page.read()
    #print content
    transcode = content.decode('utf-8','ignore').encode('utf-8','ignore')
    #print type(content)
    #transcode=content.decode('gbk','ignore').encode('utf-8','ignore') 
    o = BeautifulSoup(transcode)

    #print o
    #print type(o)
    #print dir(o)
    #print o.find_all('p')
    
    #print o.findAll('p')
    #print o.title
    
    f = open('web.txt','w+')
    '''
    for item in o: 
        f.write("%s" % item)
    f.close()
    '''
    open('origin.txt','w+').write(transcode)

    f.write(o.encode('gbk'))
    f.close()

def zhuanma():
    f1 = open('weibo_cache.txt','r+')
    f2 = open('weibo_content.txt','w')
    f3 = open('weibo_temp.txt','w')
    #f2.write('用户名和微博')
    for item in f1.readlines():
        

        
        pat1 = re.compile(r'(?<=nick-name=\\")(.*?)(?=")')
        list1 = pat1.findall(item)
    #print list1
        name_str = ''.join(list1)
    #print name_str.decode('unicode-escape').encode('gbk')
        f_str = "u\'"+name_str+"\'"
        list2 = f_str.split()
        str2 = str(list2).replace('\\\\','\\')
        str3 = str2.replace('u\'','\'')
        str4 = ''.join(str3.decode("unicode-escape").encode('utf-8'))
        #print type(str4)
        str4 = str4[3:-3]
        #print str4
        if not str4:
            f2.write('Repost ')
        else:
            f2.write('ID   '+str4+'  ')

        
        pat2 = re.compile(r'>.*')
        list3 = pat2.findall(item)
        content_str = ''.join(list3)
        f_str_2 = "u\'"+content_str+"\'"
        list4 = f_str_2.split()
        str5 = str(list4).replace('\\\\','\\')
        str6 = str5.replace('u\'','\'')
        str7 = ''.join(str6.decode("unicode-escape").encode('utf-8'))
        if True:
            pass  #此处判断微博非文本内容。
        #print str7
        str7 = str7[3:-3]
        f2.write('Content   '+str7)
        pat3 = re.compile(r'<a.*a>')
        pat4 = re.compile(r'<em.*em>')
        list5 = pat3.findall(str7)
        list6 = pat4.findall(str7)
        str8 = str(list5)
        str9 = str(list6)
        f3.write(str8+str9+'\n')
        f2.write('\n')
        '''
        pat5 = re.compile(r'(?<=name=")(.*?)(?=")')
        list7 = pat5.findall(str8)
        at_name = ''.join(list7)
        '''
        #print list7
        #print str8
        #print str9
    '''
        pat5 = re.compile(r'?<=class=W_linkb>)(.*?)(?=<\\\/a)')
        pat5.findall(str7)
        str8 = str(list5).relace(str7,str5)
        print str8
    '''
    f2.close()
    f1.close()
    f3.close()

def rebs4():
    j=1
    origin = open('web.txt','r')
    f = open('weibo_cache.txt','w')
    #print origin.read()
    #s = origin.readlines()
    for i in origin.readlines():
            pat = re.compile(r'(?<=<p class=\\"comment_txt)(.*?)(?=<\\\/p>)')
            ma=pat.findall(i)
            #print match
            for e in ma:
                    #print type(e)
                    f.write(str(j)+'   '+e)
                    f.write('\r\n')
                    j = j+1
                    #print type(ma)
    f.close()

    f1 = open('weibo_cache.txt','r')
    for item in f1.readlines():
            pat1 = re.compile(r'(?<=nick-name=\\")(.*?)(?=")')
            list1 = pat1.findall(item)
            #print list1
    #else:
    #print "********************************************"
    #print j
    origin.close()
    f1.close()

def temp_p():
    f1 = open('weibo_content.txt','r')
    f2 = open('final_temp.txt','a') #在末尾添加
    for item in f1.readlines():
        
        #print item
        pat1 = re.compile(r'(?<=href=")(.*?)(?=\")')
        list1 = pat1.findall(item)
        
        #print list1 #@用户的url
        pat3 = re.compile(r'(?<=name=)(.*?)(?=")')
        list3 = pat3.findall(item)
        
        #print list3 #@用户的ID
        name = ' '.join(list3)
        #print name
        if name:
            name = '@'+name
        pat2 = re.compile(r'(?<=red">)(.*?)(?=<)')
        list2 = pat2.findall(item)

        
        #print list2 #搜索的内容
        '''
        for i in item:
            print i
        '''
        
        #print type(item)
        item1 = item.replace('<\/em>','')
        item1 = item1.replace('''<em", 'class="red">''','')
        item1 = item1.replace('''<em', 'class="red">''','')
        
        #print item1
        pat4 = re.compile(r'<a.*a>')
        list4 = pat4.findall(item)
        
        #print list4
        str4 =''.join(list4)
        
        #print str4
        item1 = item1.replace(str4,name)
        item1 = item1.replace('>','')
        item1 = item1.replace("'",'')
        
        item1 = item1[:-3]
        #print item1
        pat5 = re.compile(r'(?<=a")(.*?)(?="#)')
        list5 = pat5.findall(item1)
        #print list5
        str5 = ''.join(list5)
        # 去掉话题
        #print str5
        item1 = item1.replace(str5,'')
        


        pat6 = re.compile(r'(?<=a",)(.*?)(?=a,)')
        list6 = pat6.findall(item1)
        
        str6 = ''.join(list6)
        #print str6
        #if str6:
            #print ('此处找到')
        #print name
        item1 = item1.replace(str6,'')
        item1 = item1.replace('<a""','')
        #item1 = item1.replace('<\/a','')
        pat7 = re.compile(r'(?<=<a,)(.*?)(?=\/a)')
        list7 = pat7.findall(item1)
        str7 = ''.join(list7)
        item1 = item1.replace(str7,'')
        item1 = item1.replace('<\/a','  meme')
        item1 = item1.replace('<a,/a,','')
        pat8 = re.compile(r'(?<=img)(.*?)(?=e",)')
        list8 = pat8.findall(item1)
        pat9 = re.compile(r'(?<=title=")(.*?)(?=])')
        
        #print list8
        for mmm in list8:
            temp_str = ''.join(mmm)
            expre_list = pat9.findall(temp_str)
            expre = ''.join(expre_list)
            item1 = item1.replace(temp_str,expre+']')
        pat10 = re.compile(r'(?<=href=)(.*?)(?=meme)')
        list9 = pat10.findall(item1)
        #print list9
        for nnn in list9:
            temp_str_2 = ''.join(nnn)
            #print temp_str_2
            name_list = pat3.findall(temp_str_2)
            name1 = ''.join(name_list)
            item1 = item1.replace(temp_str_2,'@'+name1)
        
        item1 = item1.replace('<img','')
        item1 = item1.replace('e",','')
        item1 = item1.replace('href=','')
        item1 = item1.replace('meme','')
        item1 = item1.replace('\/','')
        item1 = item1.replace('<a','')
        item1 = item1.replace('",a,','')
        item1 = item1.replace(' class="W_btn_c6"','')
        item1 = item1.replace(',,',' ')
        print item1+'\n'
        #input()
        f2.write(item1[:-1]+'\n')
        
    f1.close()
    f2.close()

a = fenci()
print a
b = int(raw_input('请输入需要爬的页数'))
a = a.encode('gbk')
print type(a)
list1 = a.split()
a = '%20'.join(list1)
#print a
for item in range(1,b+1):
    url = 'http://s.weibo.com/weibo/'+a+'&Refer=index'+'&page='+str(item)
    print url
    #print item
    search_weibo(url)
    rebs4()
    zhuanma()
    temp_p()

