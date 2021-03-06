#!/usr/bin/env python3
import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
# .wav的音频和本脚本应放在同一目录下
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file



# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "0a6b1eeea32840ea99e871099ef98556"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

