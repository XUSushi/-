# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:45:33 2018

@author: Lavina Zhu
"""

import http.client  
import hashlib  
import json  
import urllib  
import random  

def from_lang():
    """
    用户选择源语言
    通过输入数字1-5来选择语言，输入可以直接退出程序
    输入其他字符将重新选择源语言
    
    Args:
        flag：int 型，用来标记用户是否输入q以结束程序，flag = 1的时候程序结束
        fro：字符串，接收用户输入的内容
        fromLang：字符串型，代表不同语言
        
    Returns:
        1. 返回fromLang，字符串类型
        2. 返回flag的值，int 型
    """
    while True:
        print ("请选择源语言，如果退出请输入q：") 
        print ("1. 中文")
        print ("2. 英文") 
        print ("3. 日语")  
        print ("4. 法语")  
        print ("5. 西班牙语")
        flag = 0
        fro = input()
        fromLang = ''
        if fro == '1':
            fromLang = 'zh'
            break
        elif fro == '2':
            fromLang = 'en'
            break
        elif fro == '3':
            fromLang = 'jp'
            break
        elif fro == '4':
            fromLang = 'fra'
            break
        elif fro == '5':
            fromLang = 'spa'
            break
        elif fro == 'q':
            flag = 1
            break
        else:
            print ("请输入数字1-5")
    return (fromLang, flag);


def to_lang():
    """
    用户选择译文语言
    通过输入数字1-5来选择语言
    输入其他字符将重新选择译文语言
    
    Args:
        to：字符串，接收用户输入的内容
        toLang：字符串型，代表不同语言
        
    Returns:
        返回 toLang，字符串类型
    """
    while True:
        print ("请选择译文语言：")  
        print ("1. 中文")
        print ("2. 英文")  
        print ("3. 日语")  
        print ("4. 法语")  
        print ("5. 西班牙语")
        to = input()
        toLang = ''
        if to == '1':
            toLang = 'zh'
            break
        elif to == '2':
            toLang = 'en'
            break
        elif to == '3':
            toLang = 'jp'
            break
        elif to == '4':
            toLang = 'fra'
            break
        elif to == '5':
            toLang = 'spa'
            break
        else:
            print ("请输入数字1-5")
    return (toLang);
 
    
def baidu_translate(content, fromLang, toLang):
    """
    调用百度翻译API，解析百度翻译结果，并呈现出译文
    
    Args:
        appid：字符串类型，百度翻译 APP ID
        secretKey：字符串类型，百度翻译API密钥
        myurl：百度翻译API HTTP地址
        salt：随机数
        q：原文内容
        sign：签名，拼接 appid+q+salt+密钥字符串
        dst：翻译后的文本结果
        
    """
    appid = '20180527000167630'  #APP ID
    secretKey = 'ct2Zql2XnOFkrmNptBiF'  #密钥
    httpClient = None  
    myurl = '/api/trans/vip/translate'  
    q = content   
    salt = random.randint(32768, 65536)  
    sign = appid + q + str(salt) + secretKey  
    sign = hashlib.md5(sign.encode()).hexdigest()  
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(  
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(  
        salt) + '&sign=' + sign  
  
    try:  
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')  
        httpClient.request('GET', myurl)  
        response = httpClient.getresponse()  
        jsonResponse = response.read().decode("utf-8")  
        js = json.loads(jsonResponse)  
        dst = str(js["trans_result"][0]["dst"])   
        print (dst)   
    except Exception as e:  
        print (e)  
    finally:  
        if httpClient:  
            httpClient.close()  


def revise_or_not(content):
    """
    判断用户是否要修改原文，获取修改后的原文内容
    
    Args:
        ifrevise：接收用户输入的数字1或2
        afterContent：接收用户输入的修改后的内容
    
    Returns：
        返回afterContent，字符串类型
    """
    while True:
        print ("是否修改原文？")
        print ("1. 是")
        print ("2. 否")
        ifrevise = input()
        if ifrevise == '1':
            print ("请输入修改后的内容：")
            afterContent = input()
            break
        elif ifrevise == '2':
            afterContent = content
            break
        else:
            print ("请输入数字1-2")
    return (afterContent);


if __name__ == '__main__':  
    """
    获取用户选择的源语言和译文语言，调用baidu_translate函数进行机器翻译，判断用户是否对开始
    传入的原文进行了修改，若修改则调用baidu_translate函数重新进行机器翻译
    
    Args:
        fromLang： 源语言
        flag1：用来标记用户是否在选择源语言时就退出了程序
        toLang：译文语言
        content：用户输入的原文内容
        content2：原文修改后的内容
    """
    while True:
        fromLang, flag1 = from_lang()
        if flag1 == 1:  #判断用户是否在第一步选择源语言时就输入了‘q’，即退出程序
            break
        toLang = to_lang()
        print ("请输入要翻译的内容，如果退出请输入q：")  
        content = input()  
        if content == 'q':  
            break
        baidu_translate(content, fromLang, toLang)
        content2 = revise_or_not(content)
        if content2 == content:  
            continue
        else:
            baidu_translate(content2, fromLang, toLang)