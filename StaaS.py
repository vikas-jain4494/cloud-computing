import os
import time
import sys
import thread
import socket
#instance b2 ,a2
import commands 
s=socket.socket()
def func7(ip,port):
	s.connect((ip,port))
	c1=commands.getoutput("dialog --menu 'which service do u want' 30 25 2 1 'NAS' 2 'SAN' --stdout")
	s.send(c1)
	if int(c1)==1:
		d1=commands.getoutput("dialog --menu 'what do u want' 30 30 4 1 'newlv' 2 'increaselv' 3 'decreaselv'  --stdout")
		s.send(d1)
		if int(d1)==1:
			size=commands.getoutput("dialog  --inputbox 'size of object storage u want (MB) ' 10 40 --stdout")
			s.send(size)
			path1=s.recv(20)
			path=commands.getoutput("dialog  --inputbox 'name of drive ex-..dropbox' 10 40 --stdout")
			os.system('mkdir /media/'+path)
			os.system('mount '+ ip +':'+ path1 +' ' +'/media/'+path )
			os.system("dialog  --pause 'please wait for mounting ....' 15 30 60")
			s.send("ok")
		elif int(d1)==2:
			szincz=commands.getoutput("dialog  --inputbox 'size of object storage u want to increse in (MB) ' 10 40 --stdout")
			s.send(szincz)
			os.system("dialog  --pause 'please wait for resizing....' 15 30 30")
			s.send("ok")
		elif int(d1)==4:
			snapname=commands.getoutput("dialog --inputbox 'name of snapshot' 10 40 --stdout")
			s.send(snapname)
			size=commands.getoutput("dialog  --inputbox 'size of snap u want in (MB) ' 10 40 --stdout")
			s.send(size)
			snappath=s.recv(20)
			path=commands.getoutput("dialog  --inputbox 'path u want ex-../mnt/snap1' 10 40 --stdout")
			os.system('mount '+ ip +':'+ snappath +' ' +path )
			s.send("ok")
		else:
			szdcz=commands.getoutput("dialog  --inputbox 'size of object storage u want to decrease in (MB) ' 10 40 --stdout")
			s.send(szdcz)
			os.system("dialog  --pause 'please wait for resizing ....' 15 30 30")
			s.send("ok")			

	else:
		def t7():
			os.system("yum install iscsi-initiator-utils -y &> /dev/null")
		def t8():
			os.system("dialog  --pause 'please wait for installation ....' 15 30 10")

		x=commands.getstatusoutput("rpm -q iscsi-initiator-utils")[0]
		if x==0:
			pass
		else:
			try:
				thread.start_new_thread(t7,())
				thread.start_new_thread(t8,())
			except:
				print "unable to read thread"
			time.sleep(15)
			os.system("dialog  --msgbox 'installation complete :) :)' 10 40")
		e1=commands.getoutput("dialog --menu 'what do u want' 30 30 4 1 'new hard disk' 2 'increase size of hard disk' 3 'decrease size of hard disk'  --stdout")		
		s.send(e1)
				
		if int(e1)==1:
			os.system("service tgtd restart")
			size=commands.getoutput("dialog  --inputbox 'size of block storage u want (MB) ' 10 40 --stdout")
			s.send(size)
			iscsiname=s.recv(20)
			os.system("iscsiadm --mode discoverydb --type sendtargets --portal 10.1.1.55 --discover")
			os.system("iscsiadm --mode node --targetname "+ iscsiname +" --portal 10.1.1.55:3260 --login")
			s.send("ok")
		elif int(e1)==2:
			szincz=commands.getoutput("dialog  --inputbox 'size of block storage u want to increse in (MB) ' 10 40 --stdout")
			s.send(szincz)
			os.system("dialog  --pause 'please wait for resizing....' 15 30 30")
			s.send("ok")
		elif int(e1)==3:
			szdcz=commands.getoutput("dialog  --inputbox 'size of object storage u want to decrease in (MB) ' 10 40 --stdout")
			s.send(szdcz)
			os.system("dialog  --pause 'please wait for resizing ....' 15 30 30")
			s.send("ok")
		else:
			snapname=commands.getoutput("dialog --inputbox 'name of snapshot' 10 40 --stdout")
			s.send(snapname)
			size=commands.getoutput("dialog  --inputbox 'size of snap u want in (MB) ' 10 40 --stdout")
			s.send(size)
			snappath=s.recv(20)
			path=commands.getoutput("dialog  --inputbox 'path u want ex-../media/snap1' 10 40 --stdout")
			os.system('mount '+ ip +':'+ snappath +' ' +path )


