import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import *
from yahoo_fin import stock_info as si #Make sure you have this moduel
import time
import sys
import matplotlib.pyplot as plt
from threading import Thread
import random
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
print('Modules Loaded')



the_len = len(sys.argv)
score = 0
score22 = 0
score33 = 0
score44 = 0
x = [] 
y = []
z = 0
open('sampleText.txt', 'w').close()


try:
    import tkinter as tk
# --- functions ---
    def get_name():
        global name 
        global name2
        name = name_entry.get() 
        name2 = name_entry2.get()
        root.destroy()

    name = ''  
    name2 = ''
    root = tk.Tk()
    name_label = tk.Label(root, text='STOCKS')
    name_label.pack()
    name_entry = tk.Entry(root)
    label = tk.Label(root, text="ENTER STOCK: ")
    label.pack(side = 'top')
    name_entry.pack(side='top')
    name_entry2 = tk.Entry(root)
    b = tk.Button(root, text='Submit', command=get_name)
    b.pack(side='bottom')
    name_entry2.pack(side='bottom')
    label1 = tk.Label(root, text="ENTER TIME: ")
    label1.pack(side = 'bottom')
    root.geometry('200x150') 
    root.mainloop()
    company = name
    TheTime = int(name2)
    print(company)
    print(TheTime)
    print('Press Ctrl + C to EXIT')
    os.system('color 71')
    count = 0
    current_stock = si.get_live_price(company)
    print(current_stock, ' is how much the stock is worth!')
    while True:
        def beepbeep():
            path_os = os.path.dirname(os.path.abspath(__file__))
            path_os = path_os + '\\BeepSound\\beep.WAV'
            mixer.init()
            mixer.music.load(path_os)
            mixer.music.play()


        def Main67():
            global count
            global company
            global current_stock
            global x
            global y
            global score
            global z
            global score22
            global score44
            global k
            other_current_stocks = si.get_live_price(company)
            time.sleep(TheTime) 
            current_stocks = si.get_live_price(company)
            count = count + int(TheTime)
            if current_stock < current_stocks:
                diff = float(current_stocks) - float(current_stock)
                os.system('cls')
                print(company, ' stock went up by: +', diff, '$\'s', 'Since : ', count, ' seconds ago')
                
            elif current_stock > current_stocks:
                diff = float(current_stock) - float(current_stocks)                                         #Diffrent possible outcomes
                os.system('cls')
                print(company,' stock went down by: -', diff, '$\'s', 'Since : ', count, 'seconds ago')
            else:
                os.system('cls')
                print('Nothing yet!!', 'Since: ', count, 'seconds ago')
            theFinalBeep = other_current_stocks - current_stocks
            if score22 == 3:
                pass
            TheNumber_11 = TheTime * 5
            TheNumber_111 = -(TheTime * 5)
            if theFinalBeep >= TheNumber_11 or theFinalBeep <= TheNumber_111:
                beepbeep()
            score = score + 1
            if score >= 0:
                z = int(z)
                zFinal = z / 3
                zFinal1 = int(zFinal) - 100
                zFinal2 = int(zFinal) + 100
                xl = len(x)
                zlx = int(xl) + 1
                x.append(zlx)
                print(x)
                y22 = current_stocks
                y.append(y22)
                print(y)
                score44 = score44 + 1
                if score44 == 3:
                    score44 = score44 - 3
                    z = z - z
                    y222 = y22 * 3
                    z = z + y222
                txtDoc = 'sampleText.txt'
                File_object = open(txtDoc, 'a+')
                File_object.write('\n' + str(zlx) + ',' + str(y22))
                print(File_object.read())

                
            else:
                print('Gathering Info... Please Wait')
                xl = len(x)
                zlx = int(xl) + 1
                x.append(zlx)
                y22 = current_stock
                y.append(y22)
                score22 =+ 1
                z = z + y22
        Main67()                                   
except KeyboardInterrupt:
    sys.exit()
