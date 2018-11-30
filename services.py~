import os
import time
import sys
import thread
import socket
#instant b1,a1
import commands 
import StaaS
import IaaS
s=socket.socket()
def func6(ip,port):
	s.connect((ip,port))
	ch=commands.getoutput("dialog --menu 'which service do u want' 30 25 5 1 SaaS 2 StaaS 3 IaaS 4 PaaS --stdout")
	s.send(ch)
	if int(ch)==1:
		software=commands.getoutput("dialog --inputbox 'which service do u want' 10 40 --stdout" )
		os.system("ssh -X -l vicky "+ip+" "+software)
		s.send("ok")
	elif int(ch)==2:
		StaaS.func7(ip , port)
	elif int(ch)==3:
		IaaS.func13()
		IaaS.func14(ip ,port)
	else:
		os.system("dialog --msgbox 'sorry this is not availiable till now' 10 40 ")

