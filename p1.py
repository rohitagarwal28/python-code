#!usr/bin/python3
import datetime
name=input("enter the name")
age=int(input("enter the age"))
current_year=datetime.datetime.now()
x=95-age
print("year will be",x+current_year.year)

