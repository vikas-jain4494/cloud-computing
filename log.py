import os
import time
import sys
import thread
def func2(user):
	os.system("cut -d: -f1 /etc/passwd > /tmp/username")
	f=open("/tmp/username")
	k=0
	for i in f:
		j=i.strip()
		if user==j:
			break
		else:
			k+=1
	f.close()
	os.system("cut -d: -f1 /etc/passwd |wc -l > /tmp/lines")

	fhlines=open("/tmp/lines", "r")
	p=fhlines.read()
	fhlines.close()
	z=int(p)
	t=(z,k)
	return t

def func4(c):
	user=c.recv(20)
	t=func2(user)
	passwd=c.recv(20)
	if t[0]!=t[1] and passwd=="redhat" :
		m=0
		m1=str(m)	
		c.send(m1)
		echo=1
		p=(m,echo)
		return p
	else:
		m=1
		m1=str(m)	
		c.send(m1)
		ech=c.recv(5)
		echo=int(ech)
		p=(m,echo)
		return p
	







