#!usr/bin/python3
import datetime
present=datetime.datetime.now()
name=input("enter your name")
if present.hour>=6 and present.hour<12:
	print("GOOD MORNING",name)
elif present.hour>=12 and present.hour<16:
	print("GOOD AFTERNOON",name)
elif present.hour>=16 and present.hour<19:
	print("GOOD EVENING",name)
elif present.hour>=29:
	print("GOOD NIGHT",name)




