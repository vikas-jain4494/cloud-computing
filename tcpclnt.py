#!usr/bin/python2
#tcpdump -i lo port 5555 :done by client after telnet to check that hand shek is going on or not
#socket.socket(socket.AF_NET ,socket.SOCK_STREAM ,0)
import os
import time
import sys
import thread
import socket
import commands 
import services
s=socket.socket()

def func3():
	user=commands.getoutput("dialog  --inputbox 'Enter user to login' 10 40 --stdout")
	s.send(user)
	passwd=commands.getoutput("dialog  --passwordbox 'Enter password to login' 10 40  --stdout")
	s.send(passwd)

def t1():
	os.system("yum install dialog -y &> /dev/null")
def t2():
	os.system("dialog  --pause 'please wait for installation ....' 15 30 10")

x=commands.getstatusoutput("rpm -q dialog")[0]
if x==0:
	os.system("dialog  --msgbox 'yuppy !! dialog  already installed :) :)' 10 40")
else:
	try:
		thread.start_new_thread(t1,())
		thread.start_new_thread(t2,())
	except:
		print "unable to read thread"
	time.sleep(11)
	os.system("dialog  --msgbox 'installation complete :) :)' 10 40")

ip=commands.getoutput("dialog  --inputbox 'to which ip u want to connect' 10 40 --stdout")
port=commands.getoutput("dialog  --inputbox 'to which port u want ' 10 40 --stdout")

s.connect((ip, int(port)))

user=commands.getoutput("dialog  --inputbox 'Enter user to login (remember u have only at max 3 chances to login )' 10 40 --stdout")
s.send(user)
passwd=commands.getoutput("dialog  --passwordbox 'Enter password to login' 10 40  --stdout")
s.send(passwd)

m1=s.recv(1)
m=int(m1)
if m==0:
	os.system("dialog --msgbox 'your warm welcome' 10 40")
else:
	echo=os.system("dialog --yesno 'want to try again???' 10 40")
	ech=str(echo)
	s.send(ech)
	if echo==0:
		func3()
		m1=s.recv(1)
		m=int(m1)
		if m==0:
			os.system("dialog --msgbox 'your warm welcome' 10 40")
		else:
			echo=os.system("dialog --yesno 'want to try again???' 10 40")
			ech=str(echo)
			s.send(ech)
			if echo==0:
				func3()
				m1=s.recv(1)
				m=int(m1)
				if m==0:
					os.system("dialog --msgbox 'your warm welcome' 10 40")
				else:
					os.system("dialog --msgbox 'i will not allow u to login ...u may be fake user' 10 40")
			else:
				os.system("dialog --msgbox 'ok as your wish..good bye!!' 10 40")
	else:
		os.system("dialog --msgbox 'ok as your wish..good bye!!' 10 40")	
if m==0:
	poort=int(port)
	services.func6(ip ,poort)
else:
	pass








