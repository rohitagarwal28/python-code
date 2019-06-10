#!usr/bin/python3
adhoc=[1,2,3,1,4,66,5,22,0,9]
l1=[]
l2=[]
for i in adhoc:
	if i >5:
		print(i)
		l1.append(i)
	elif i <=2:
		print(i)
		l2.append(i)
print(l1)
print(l2)

		
