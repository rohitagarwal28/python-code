#!usr/bin/python3
import time
import webbrowser
from googlesearch import search
print("you can search the data by two ways::")
print("1--> by typing")
print("2--> by voice")
choice=int(input("enter your choice"))
if choice==1:
	data=input("enter something you are interested for::")
	li=[]
	for i in search(data,stop=5):
		li.append(i)
		time.sleep(1)
		print(i)
		webbrowser.open_new_tab('https://www.google.com/search?q='+i)
		print(li)
else:
	print("hey")

