# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:47:30 2018

@author: 许某某
"""
#接受的语音识别结果为text的字符串

def test(string):
    a=len(string);
    if a<=6000:
        print(a)
        print("已成功接收数据，请稍候片刻")        
       #串起来时，调用setting_key 
    #setting_key(id_list, key_list, fromLang, toLang, content)
    else:
        print("您好，字符串长度超出限制，请重试！")
        
if __name__ == '__main__':  
#   while True:
        string="我爱你祖国we love youjklllllllllllllllllllllllllllllllllllllllllllllll"
        test(string)
        toLang="en"
        fromLang="zh"
        id_list=['20180529000169010','20170601000049695','20180527000167630'];
        key_list=["opRustpMgAtMC18WVtlR","gOxjP2r4I9SsWRDF2ozO","ct2Zql2XnOFkrmNptBiF"];
 #       print(id_list[0])
 #      print(key_list[1])
   