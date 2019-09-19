import matplotlib.pyplot as plt 
import time, random
import numpy as np
score = 0
x = [] 
y = []
#print('Collecting data... Please Wait |')
for i in range(4):
    xl = len(x)
    zlx = int(xl) + 1
    x.append(zlx)
    ran = random.randint(1, 30)
    y.append(ran)
print(x)
while True:
        score = score + 1
        xl = len(x)
        zlx = int(xl) + 1
        x.append(zlx)
        if score > 4:
            y22 = random.randint(20, 99)
        else:
            y22 = random.randint(10, 34)
        y.append(y22)
        
        plt.plot(x, y, linewidth = 2, 
                 marker='o', markerfacecolor='blue', markersize=7)  
        plt.draw()
        plt.pause(1)
        plt.clf()
        print('ok')
