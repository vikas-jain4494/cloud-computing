#!usr/bin/python2
import os
import time
import sys
import thread
import socket
import commands
def func8():
	def t3():
		os.system("yum install nfs-utils -y &> /dev/null")
	def t4():
		os.system("dialog  --pause 'please wait for installation ....' 15 30 10")

	x=commands.getstatusoutput("rpm -q nfs-utils")[0]
	if x==0:
		pass
	else:
		try:
			thread.start_new_thread(t3,())
			thread.start_new_thread(t4,())
		except:
			print "unable to read thread"
		time.sleep(15)
		os.system("dialog  --msgbox 'installation complete :) :)' 10 40")
def func5(size,d1):
	fhlvnumber=open("/root/Desktop/project/lvname","r+")
	lvnumber=fhlvnumber.read()
	lvnumber=lvnumber.strip()
	os.system('lvcreate --size '+size+'M --name lv'+lvnumber+' newvg')
	os.system("mkfs.ext4 /dev/newvg/lv"+lvnumber)
	os.system("mkdir /mnt/staas"+lvnumber)
	os.system("mount /dev/newvg/lv"+lvnumber+" /mnt/staas"+lvnumber)
	path1='/mnt/staas'+lvnumber
	os.system("chmod 777 /mnt/staas"+lvnumber)
	fhnfs=open("/etc/exports","r+")
	fhnfs.seek(0,2)
	fhnfs.write('\n')
	fhnfs.write("/mnt/staas"+lvnumber+" *(rw,no_root_squash)")
	fhnfs.close()
	os.system("service nfs restart")
	lvnumber=int(lvnumber)+1
	fhlvnumber.seek(0,0)
	lvnumber=str(lvnumber)
	fhlvnumber.write(lvnumber)
	fhlvnumber.close()

	return path1
def func9(szincz):
	fhlvnumber=open("/root/Desktop/project/lvname","r+")
	lvnumber=fhlvnumber.read()
	lvnumber=lvnumber.strip()
	lvnumber=int(lvnumber)-1
	lvnumber=str(lvnumber)
	os.system("lvextend --size +"+ szincz +"M  /dev/newvg/lv"+lvnumber )
	os.system("resize2fs /dev/newvg/lv"+lvnumber)
	fhlvnumber.close()
def func10(szdcz):
	fhlvnumber=open("/root/Desktop/project/lvname","r+")
	lvnumber=fhlvnumber.read()
	lvnumber=lvnumber.strip()
	lvnumber=int(lvnumber)-1
	lvnumber=str(lvnumber)
	os.system("umount /mnt/staas"+lvnumber)
	os.system("e2fsck -fy /dev/newvg/lv"+lvnumber)
	os.system("resize2fs /dev/newvg/lv"+lvnumber+ " "+szdcz)
	os.system("lvreduce --size "+szdcz+"M /dev/newvg/lv"+lvnumber+" -fy")
	os.system("mount /dev/newvg/lv"+lvnumber+" /mnt/staas"+lvnumber)
	fhlvnumber.close()
def func18(snapname ,size):
	fhlvnumber=open("/root/Desktop/project/lvname","r+")
	lvnumber=fhlvnumber.read()
	lvnumber=lvnumber.strip()
	lvnumber=int(lvnumber)-1
	lvnumber=str(lvnumber)
	os.system("lvcreate --name "+snapname+" --size "+size+"M --snapshot /dev/newvg/lv"+lvnumber)
	os.system("mount /dev/newvg/"+snapname+" /mnt/snap"+lvnumber)	
	snappath='/mnt/snap'+lvnumber	
	fhlvnumber.close()
	return snappath


