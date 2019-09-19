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
import random as r
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
try:
    try:
        try:
            try:
                try:
                    LARGE_FONT= ("Verdana", 12)


                    class SeaofBTCapp(tk.Tk):

                        def __init__(self, *args, **kwargs):
                            
                            tk.Tk.__init__(self, *args, **kwargs)

                            tk.Tk.iconbitmap(self, default="clienticon.ico")
                            tk.Tk.wm_title(self, "Sea of BTC client")
                            
                            
                            container = tk.Frame(self)
                            container.pack(side="top", fill="both", expand = True)
                            container.grid_rowconfigure(0, weight=1)
                            container.grid_columnconfigure(0, weight=1)

                            self.frames = {}

                            for F in (StartPage, PageOne, PageTwo, PageThree):

                                frame = F(container, self)

                                self.frames[F] = frame

                                frame.grid(row=0, column=0, sticky="nsew")

                            self.show_frame(StartPage)

                        def show_frame(self, cont):

                            frame = self.frames[cont]
                            frame.tkraise()

                            
                    class StartPage(tk.Frame):

                        def __init__(self, parent, controller):
                            tk.Frame.__init__(self,parent)
                            label = tk.Label(self, text="Start Page", font=LARGE_FONT)
                            label.pack(pady=10,padx=10)

                            button = ttk.Button(self, text="Visit Page 1",
                                                command=lambda: controller.show_frame(PageOne))
                            button.pack()

                            button2 = ttk.Button(self, text="Visit Page 2",
                                                command=lambda: controller.show_frame(PageTwo))
                            button2.pack()

                            button3 = ttk.Button(self, text="Graph Page",
                                                command=lambda: controller.show_frame(PageThree))
                            button3.pack()


                    class PageOne(tk.Frame):

                        def __init__(self, parent, controller):
                            tk.Frame.__init__(self, parent)
                            label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
                            label.pack(pady=10,padx=10)

                            button1 = ttk.Button(self, text="Back to Home",
                                                command=lambda: controller.show_frame(StartPage))
                            button1.pack()

                            button2 = ttk.Button(self, text="Page Two",
                                                command=lambda: controller.show_frame(PageTwo))
                            button2.pack()


                    class PageTwo(tk.Frame):

                        def __init__(self, parent, controller):
                            tk.Frame.__init__(self, parent)
                            label = tk.Label(self, text="THIS IS THE RAJ PAGE", font=LARGE_FONT)
                            label.pack(pady=10,padx=10)

                            button1 = ttk.Button(self, text="Back to Home",
                                                command=lambda: controller.show_frame(StartPage))
                            button1.pack()

                            button2 = ttk.Button(self, text="Page One",
                                                command=lambda: controller.show_frame(PageOne))
                            button2.pack()


                    class PageThree(tk.Frame):

                        def __init__(self, parent, controller):
                            tk.Frame.__init__(self, parent)
                            label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
                            label.pack(pady=10,padx=10)

                            button1 = ttk.Button(self, text="Back to Home",
                                                command=lambda: controller.show_frame(StartPage))
                            button1.pack()
                            c = []
                            b = []
                            f = Figure(figsize=(5,5), dpi=100)
                            a = f.add_subplot(111)
                            
                            while True:
                                time.sleep(10)
                                random1 = r.randint(1, 10)
                                c.append(random1)
                                
                                bb = len(b)
                                aa = int(bb)
                                bb = bb + 1
                                b.append(bb)
                                print(c, b)
                                a.plot(b,c)
                                canvas = FigureCanvasTkAgg(f, self)
                                canvas.draw()
                                canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                                toolbar = NavigationToolbar2Tk(canvas, self)
                                toolbar.update()
                                canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                    
                    app = SeaofBTCapp()
                    app.mainloop()
                    
                except KeyboardInterrupt:
                    print('none')
            except KeyboardInterrupt:
                print('none')
        except KeyboardInterrupt:
            print('none')
    except KeyboardInterrupt:
        print('none')
except KeyboardInterrupt:
    print('none')

