from yahoo_fin import stock_info as si # Make sure you have this moduel
import time
import os, sys
from pynput.keyboard import Key 
from pynput.keyboard import Controller
k = Controller()
the_len = len(sys.argv)
try:
    if the_len > 1:
        os.system('cls')
        print('Moduels loaded\nPRESS CTRL + C to exit')
        company = sys.argv[1]
        os.system('color 71')
        count = 0
        current_stock = si.get_live_price(company)
        print(current_stock, ' is how much the stock is worth!')
        while True:
            def theStockCom():
                global count
                global company
                global current_stock
                time.sleep(20) # Change time here if you want a schedule based code import schedule and use its code
                current_stocks = si.get_live_price(company)
                count = count + 20
                if current_stock < current_stocks:
                    diff = float(current_stock) - float(current_stocks)
                    os.system('cls')
                    print(company, ' stock went down by: ', diff, '$\'s', 'Since : ', count, ' seconds ago')
                    
                elif current_stock > current_stocks:
                    diff = float(current_stock) - float(current_stocks)
                    os.system('cls')
                    print(company,' stock went up by: ', diff, '$\'s', 'Since : ', count, 'seconds ago')
                else:
                    os.system('cls')
                    print('Nothing yet!!', 'Since: ', count, 'seconds ago')
            theStockCom()
    else:
         print('In order to use the script \nOpen script in cmd and type \nPATH:', os.path.dirname(os.path.abspath(__file__)), '\npython stock.py {Name of stock}')
         input()
         time.sleep(2)
except KeyboardInterrupt:
    time.sleep(3)
    k.type('EXIT')
    k.press(Key.enter)
    k.release(key.enter)
    sys.exit()
