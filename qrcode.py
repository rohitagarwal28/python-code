from googlesearch import search
import pyqrcode
#from pyqrcode import QRcode
inp=input("enter the search text")
li=[]
for i in search(inp,stop=3):
	li.append(i)
	print(i)
	url=pyqrcode.create(i)
	for j in range(3):
		url.svg(str(j)+".svg",scale=8)
		
