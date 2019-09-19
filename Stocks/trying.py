import tkinter as tk
import re
# --- functions ---
'''
def get_name():
    global name # inform function to use global variable instead of creating local one
    global name2
    name = name_entry.get() # assign text to global variable
    name2 = name_entry2.get()
    root.destroy()
# --- main ---
name = ''  # global variable with default value (if you don't put name)
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
TheTime = name2
print(company)
print(TheTime)

'''

txtDoc = 'sampleText.txt'
File_object = open(txtDoc).read()
if ',' in File_object:
    the_number = File_object
    File_object2 = re.sub(r'.*,', '', the_number)
    print(File_object2)#Long list of numbers
File_object3 = len(File_object2.split('\n'))
f3 = File_object3 #Number of lines
first = File_object2[0]
second = File_object2[1]
middle = f3 / 2
middle = File_object2[int(middle)]
print(middle, second, first)
