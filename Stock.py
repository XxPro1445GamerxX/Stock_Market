from yahoo_fin import stock_info as si # Make sure you have this moduel
import time
import os, sys
the_len = len(sys.argv)
try:
    if the_len > 1:
        os.system('cls')
        print('Moduels loaded')
        os.system('color 71')
        count = 0
        while True:
            def amazonS():
                global count
                company = 'amzn' #Change company STOCK AABBREVIATION HERE currently amazon
                current_stock = si.get_live_price(company)
                time.sleep(20) # Change time here if you want a schedule based code import schedule and use its code
                current_stocks = si.get_live_price(company)
                count = count + 1
                if current_stock > current_stocks:
                    diff = float(current_stock) - float(current_stocks)
                    os.system('cls')
                    print('Amazons stock went down by: ', diff, '$\'s', 'COUNT: ', count, 'PRESS CTRL + C to exit')
                    
                elif current_stock < current_stocks:
                    diff = float(current_stock) - float(current_stocks)
                    os.system('cls')
                    print('Amazons stock went up by: ', diff, '$\'s', 'COUNT: ', count, 'PRESS CTRL + C to exit')
                else:
                    os.system('cls')
                    print('Nothing yet!!', 'COUNT: ', count, 'PRESS CTRL + C to exit')
            amazonS()
    else:
         print('In order to use the script \nOpen script in cmd and type \nPATH:', os.path.dirname(os.path.abspath(__file__)), '\npython stock.py stock')
         input()
         time.sleep(2)
except KeyboardInterrupt:
    sys.exit()
