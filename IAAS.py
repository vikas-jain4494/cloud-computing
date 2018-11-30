import os
import time
import sys
import thread
import socket
#instance b3 ,a3
import commands 
s=socket.socket()

def func13():
	def t11():
		os.system("yum install libvirt -y &> /dev/null")
	def t12():
		os.system("dialog  --pause 'please wait for installation ....' 15 30 10")

	x=commands.getstatusoutput("rpm -q libvirt")[0]
	if x==0:
		pass
	else:
		try:
			thread.start_new_thread(t11,())
			thread.start_new_thread(t12,())
		except:
			print "unable to read thread"
		time.sleep(15)
		os.system("dialog  --msgbox 'installation complete :) :)' 10 40")

def func14(ip ,port):
	s.connect((ip ,port))
	osname=commands.getoutput("dialog --menu 'Enter OS name' 40 30 10 1 'redhat' 2 'fedora' 3 'backtrack' 4 'ubuntu' 5 'windows 7' 6 'windows 8' 7 'windows xp' --stdout")
	s.send(osname)
	if osname=='1':
		ram=commands.getoutput("dialog --inputbox 'Enter ram size (MB)' 10 30  --stdout")
		s.send(ram)

		cpu=commands.getoutput("dialog --inputbox 'Enter cpu core' 10 30  --stdout")
		s.send(cpu)

		hdsize=commands.getoutput("dialog --inputbox 'Enter HD size (GB)' 10 30  --stdout")
		s.send(hdsize)

		ostype=commands.getoutput("dialog --inputbox 'Enter OS Type' 10 30  --stdout")
		s.send(ostype)
		k=0
		fhosname=open("/root/Desktop/project/osname","r+")
		for i in fhosname:
			i=i.strip()
			if i==ostype:
				os.system("dialog --msgbox 'sorry ! this name already exit in system' 15 40")
				break
			else:
				k+=1
		p=commands.getoutput("cat < /root/Desktop/project/osname |wc -l")
		p=int(p)
		if k==p:
			os.system("dialog --msgbox 'good ! this name does not exit in our system' 15 40")
			wayinstall=commands.getoutput("dialog --menu 'enter by which do u want to install os ' 30 50 2 1 'Local install media (CDROM or ISO IMAGE)' 2 'Network install (HTTP,FTP or NFS)' --stdout")
			if wayinstall=='1':
				fhosname.seek(0,2)
				fhosname.write(ostype+'\n')
				fhosname.close()
				s.send(wayinstall)
				s.recv(10)
				service=commands.getoutput("dialog --menu 'by what do u want to be connect' 30 30 4 1 'ssh' 2 'vncviewer' 3 'rdesktop' --stdout")
				s.send(service)
				s.recv(10)
				if service=='1':
					os.system("dialog --msgbox 'dude i'm sorry ..i don't know the commands of behind it' 10 40")
					s.send("ok")
				if service=='2':
					fhvncport=open("/root/Desktop/project/vncport","r+")
					vncport=fhvncport.read()
					vncport=vncport.strip()
					vncport=int(vncport)-1
					vncport=str(vncport)
					os.system("vncviewer "+ip+":5900")
					fhvncport.close()
					s.send("ok")
				if service=='3':
					os.system("yum install rdesktop -y")
					os.system("rdesktop "+ip+" -p vikas")
					s.send("ok")
				
			else:	
				fhosname.close()			
				os.system("dialog --msgbox 'sorry actually we don't have this choice ....that was just for show' 15 40")
				s.send(wayinstall)
				s.recv(10)
				s.send('4')
				s.recv(10)
				s.send("ok")
		else:
			fhosname.close()
			s.send('3')
			s.recv(10)
			s.send('4')
			s.recv(10)
			s.send("ok")
	else:
		os.system("dialog --msgbox 'sorry actually we don't have this os ...that was just for show' 15 40")

	
	
	


