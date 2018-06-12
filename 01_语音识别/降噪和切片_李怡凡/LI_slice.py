from pydub import AudioSegment
#需要提前用pip安装pydub
sound_new = AudioSegment.from_file("test.wav", format="wav")
#打开目标音频文件
len_sound = len(sound_new) 
#计算音频市时长
filename = "output"
for i in range(0,10):
    filename = "output"+str(i)+".wav"
    #命名输出文件名
    n=i+1
    sound_new[15000*i:15000*n].export(filename, format="wav")
    #每15秒一切分，并按顺序输出
    if len_sound<15000:
        break
    #当音频文件小于15秒时停止切分
    len_sound=len_sound-15000
    
