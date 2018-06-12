# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# 引入Speech SDK  
from aip import AipSpeech  
import subprocess  
import datetime  
import sys  
import os  
import time  
#from pydub import AudioSegment  
import math  
  
# 定义常量  
#APP_ID = '你的 App ID'  
APP_ID = '11318658'  
#API_KEY = '你的 API Key'  
API_KEY = 'adM73GfL7Xkv0vkWx06WUGPq'  
#SECRET_KEY = '你的 Secret Key'  
SECRET_KEY = 'LRAwER9jlOmR71BFGuCmU2IOK6mgeOne'  
# 初始化AipSpeech对象  
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)  
  
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {
    'dev_pid': 1536,
})


# 文件处理  
def get_wave_filename(fileFullName):  
    # MP3文件转换成wav文件  
    # 判断文件后缀，是mp3的，直接处理为16k采样率的wav文件；  
    # 是wav的，判断文件的采样率，不是8k或者16k的，直接处理为16k的采样率的wav文件  
    # 其他情况，就直接返回AudioSegment直接处理  
    fileSufix = fileFullName[fileFullName.rfind('.')+1:]  
    print(fileSufix)  
    filePath = fileFullName[:fileFullName.find(os.sep)+1]  
    print(filePath)  
    if fileSufix.lower() == "mp3":  
        wavFile = "wav_%s.wav" %datetime.datetime.now().strftime('%Y%m%d%H%M%S')  
        wavFile = filePath + wavFile  
        cmdLine = "ffmpeg -i \"%s\" -ar 16000 " %fileFullName  
        cmdLine = cmdLine + "\"%s\"" %wavFile  
        print(cmdLine)  
        ret = subprocess.run(cmdLine)  
        print("ret code:%i" %ret.returncode)  
        return wavFile  
        #if ret.returncode == 1:  
        #   return wavFile  
        #else:  
        #   return None  
    else:  
        return fileFullName  
  

#文件分片  
try:  
    script, fileFullName = sys.argv  
except:  
    print("参数 文件名 未指定!")  
    exit()  
  
if not os.path.isfile(fileFullName):  
    print("参数 %s 不是一个文件名" %fileFullName)  
    exit()  
  
if not os.path.exists(fileFullName):  
    print("参数 %s 指定的文件不存在" %fileFullName)  
    exit()  
  
filePath = fileFullName[:fileFullName.find(os.sep)+1]  

# 文件处理为Wav，采样率16k的文件，返回文件名  
wavFile = get_wave_filename(fileFullName)  
print(wavFile)  
record = AudioSegment.from_wav(wavFile)  
if wavFile != fileFullName:  
    time.sleep(1)  
    os.remove(wavFile)  
  
recLen = record.duration_seconds  
interval = 120 * 1000  
maxLoop = math.ceil(recLen*1000/float(interval))  
for n in range(0,math.ceil(recLen*1000/float(interval))):  
    recSeg = record[n * interval : (n + 1)*interval]  
    #print("Segment:%i,startat:%i,length:%i" %n,n*interval/1000,recSeg.duration_seconds)  
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> Segment:" + str(n) +"/" + str(maxLoop))  
    segFile = filePath + "seg%s.wav" %("0"*7 + str(n))[-6:]  
    # 把分段的语音信息保存为临时文件  
    file_handle = recSeg.export(segFile,format="wav",codec = "libvorbis")  
    file_handle.close()  
    # 读取分段的临时文件为字节  
    file_handle = open(segFile, 'rb')  
    file_content = file_handle.read()  
    file_handle.close()  
    # 删除临时文件  
    os.remove(segFile)  

    # 用百度API处理该语音  
    result=aipSpeech.asr(file_content, 'pcm', 16000, {'lan': 'zh'})  
    if result['err_no'] == 0:  
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> " + result['result'][0])  
    else:  
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> " + "err_no:" + str(result['err_no']))