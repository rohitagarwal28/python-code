#!/usr/bin/python2
#send msg 'exit' to terminate connection
import socket
import os
import sys
recv_ip = "127.0.0.1"
recv_port = 4455
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
	while 1:
		msg = raw_input("SEND : ")
		if len(msg)>150:
			print("message length exceeded ")
		else :
			break
	s.sendto(msg,(recv_ip,recv_port))
	if msg=='exit':
		s.close()
		break
	data=s.recvfrom(150)
	if str(data[0]) == 'exit':
		print("exit from other host")
		s.close()
		break
	else:		
		print("RECEIVED : "+str(data[0]))
