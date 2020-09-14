# -*- coding: utf-8 -*- 
from lexicalAnal import *

import tkinter as tk
from tkinter import filedialog
#import Tka11y as tk
from Tka11y import *

from gtts import gTTS

import datetime

import pygame
from pygame import mixer
import mutagen.mp3

mixer.init(frequency=23700)

textSpell = ''
latex = ''
#folderPath = './'

################# -- GUI -- #################

window = tk.Tk()
window.title('MathExpress v.2.0.1')
window.geometry('500x500')

v = tk.StringVar(window)
folderPath = tk.StringVar(window)
fileDir = tk.StringVar(window)

header = tk.Label(window, text='MathExpress v.2.0.1: เครื่องมืออ่านนิพจน์ทางคณิตศาสตร์เป็นเสียงภาษาไทย')

lblLaTeX = tk.Label(window,text='พิมพ์ LaTeX:')
ent = tk.Entry(window, width=30, font="Courier 20",justify="center")
latex = ent.get()

spell = tk.Label(window,textvariable = v, wraplength=200)

############## -- callback -- ###############
def processLaTeX():
    latex = ent.get()
    tokens = []
    try:
        tokens = cleanTokens(lexAnal(latex))
    except:
        v.set('invalid syntax')
        return
    
    textSpell = ' '.join(tokens)
    v.set(textSpell)
    tts = gTTS(text=textSpell, lang='th')
    currentTime = str(datetime.datetime.now())
    path = folderPath.get()+'/'+currentTime+'.mp3'
    print(path)
    try:
        tts.save(path)
        fileDir.set(path)
    except:
        tts.save(currentTime+'.mp3')
        fileDir.set(currentTime+'.mp3')

def browse_callback():
    fileName = filedialog.askdirectory()
    folderPath.set(fileName)

def play_callback():
    print('getting:',fileDir.get())
    try:
        mp3 = mutagen.mp3.MP3(fileDir.get())
        mixer.music.load(fileDir.get())
        mixer.music.play()
    except:
        print('no file!')

############################################

readButton = tk.Button(window, text='อ่านออกเสียง', command=processLaTeX)
browseButton = tk.Button(window, text='เปลี่ยนที่อยู่', command=browse_callback)
playbackButton = tk.Button(window, text='ฟังเสียง', command=play_callback)

header.pack()
lblLaTeX.pack()
ent.pack()
readButton.pack()
browseButton.pack()
spell.pack()
playbackButton.pack()

window.mainloop()
