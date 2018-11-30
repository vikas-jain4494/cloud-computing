#!usr/bin/python2
import os
import time
import sys
import thread
import socket
import commands
def func11():
	def t5():
		os.system("yum install scsi-target-utils -y &> /dev/null")
	def t6():
		os.system("dialog  --pause 'please wait for installation ....' 15 30 10")

	x=commands.getstatusoutput("rpm -q scsi-target-utils")[0]
	if x==0:
		pass
	else:
		try:
			thread.start_new_thread(t5,())
			thread.start_new_thread(t6,())
		except:
			print "unable to read thread"
		time.sleep(15)
		os.system("dialog  --msgbox 'installation complete :) :)' 10 40")
def func12(size,address):
	fhlvnumber=open("/root/Desktop/project/lvname","r+")
	lvnumber=fhlvnumber.read()
	lvnumber=lvnumber.strip()
	os.system('lvcreate --size '+size+'M --name lv'+lvnumber+' newvg')

	fhtidnumber=open("/root/Desktop/project/tidname","r+")
	tidnumber=fhtidnumber.read()
	tidnumber=tidnumber.strip()
	
	os.system("service tgtd restart")
	os.system("tgtadm --lld iscsi --mode target --op new --tid "+tidnumber+" --targetname myiscsi"+tidnumber)
	os.system("tgtadm --lld iscsi --mode logicalunit --op new --lun 1 --tid "+tidnumber+" --backing-store /dev/newvg/lv"+lvnumber)
	os.system("tgtadm --lld iscsi --mode target --op bind --tid "+tidnumber+" --initiator-address "+address)	
	iscsiname='myiscsi'+tidnumber	
		
	fhiscsi=open("/etc/tgt/targets.conf","r+")
	fhiscsi.seek(0,2)
	#fhiscsi.write("<target myiscsi"+tidnumber+">"+'\n \t'+"backing-store /dev/newvg/lv"+lvnumber+'\n \t'+'initiator-address '+address+'\n'+'</target> \n')
	fhiscsi.close()
	os.system("service tgtd restart")
	
	tidnumber=int(tidnumber)+1
	fhtidnumber.seek(0,0)
	tidnumber=str(tidnumber)
	fhtidnumber.write(tidnumber)
	fhtidnumber.close()

	lvnumber=int(lvnumber)+1
	fhlvnumber.seek(0,0)
	lvnumber=str(lvnumber)
	fhlvnumber.write(lvnumber)
	fhlvnumber.close()
	return iscsiname

def func19(snapname ,size):
	fhlvnumber=open("/root/Desktop/project/lvname","r+")
	lvnumber=fhlvnumber.read()
	lvnumber=lvnumber.strip()
	os.system("lvcreate --name "+snapname+" --size "+size+"M --snapshot /dev/newvg/lv"+lvnumber)
	os.system("mount /dev/newvg/"+snapname+" /media/snap"+lvnumber)	
	snappath='/media/snap'+lvnumber	
	fhlvnumber.close()
	return snappath
	
