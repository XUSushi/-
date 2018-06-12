# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:12:28 2018

@author: 许某某
"""
import http.client  
import hashlib  
import json  
import urllib  
import random  
import time
def errorsetting(id_list,key_list, fromLang, toLang, content):
    print("nihao")
    j=1
    i=1
    pp=id_list[i]
    kk=key_list[j]
        
    while i < len(id_list): 
        while j < len(key_list):
            print(i)
            print(j)
            qq = content
            pp= id_list[i]
            kk=key_list[j]
      #      print(pp)
            print(kk)
            saltt = random.randint(32768, 65536)  
            signn = pp + qq + str(saltt) + kk 
            print(signn)
            print('---------------------------------------------')                  
            signn = hashlib.md5(signn.encode()).hexdigest()
            myurll = '/api/trans/vip/translate'  + '?appid=' + pp + '&q=' + urllib.parse.quote(  
            qq) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(saltt) + '&sign=' + signn
            httpClientt = http.client.HTTPConnection('api.fanyi.baidu.com')  
            httpClientt.request('GET', myurll)  
            # response是HTTPResponse对象  
            responses = httpClientt.getresponse()  
            jsonResponses = responses.read().decode("utf-8")# 获得返回的结果，结果为json格式
                
                
            print(jsonResponses)
            jss = json.loads(jsonResponses)  # 将json格式的结果转换字典结构  
           #     print(js)   
            dss = str(jss["trans_result"][0]["dst"])  # 取得翻译后的文本结果  
            print (dss) # 打印结果                  
        i=i+1
    print("结束了")   
if __name__ == '__main__':  
   while True:
        toLang="en"
        fromLang="zh"
        id_list=['20180601000049695','20170601000049695','20180529000169010','20180527000167630'];
        key_list=["gOxjP2r4I9SsWRDF2ozO","gOxjP2r4I9SsWRDF2ozO","opRustpMgAtMC18WVtlR","ct2Zql2XnOFkrmNptBiF"];
 #       print(id_list[0])
 #      print(key_list[1])
   
       
        print ("请输入要翻译的内容，如果退出请输入q：")  
        content = input()  
        if content == 'q':  #判断用户输入内容，是否退出程序
            break
        errorsetting(id_list, key_list, fromLang, toLang, content)
 