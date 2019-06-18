#!/usr/bin/python
#send msg 'exit' to terminate connection
import socket
import os
import sys

recv_ip = "127.0.0.1"
recv_port = 4455 # 0-1024 are free

#creating udp socket
#              ip type 4,UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#fitting ip and port with udp socket
s.bind((recv_ip,recv_port))

# recv data from sender
while 4 > 2:	
	data=s.recvfrom(150)  #length of data to recieve in one go
	if str(data[0])=='exit':
		print("exit by other host")
		s.close()
		break
	print("RECEIVED : "+str(data[0]))
	while 1:
		reply = raw_input("SEND : ")
		if len(reply)>150:
			print("message length exceeded ")
		else :
			break
	s.sendto(reply,data[1])	
	if reply=='exit':
		s.close()
		break
