#!/usr/bin/env python
# encoding:utf-8

import sys
import os

sys.path.append("..")
from lib.PublicSQLClass import *
from lib.ParamikoClass import *
import re
import multiprocessing
from optparse import OptionParser
import time


def helpFunc(a,b,c,d):
	print "\033[32;1mFor help:"
	print "superstar.py [-a (All ip) -i (IP address,xx1,xx2..) -M (Module name) -s (Super mode) -c (stop|O|restart)]"
	print "superstar.py -a -c start|stop|restart --all --cmd start|stop|restart"
	print "superstar.py -i ipaddr,[xx,xx] -c start|stop|restart --ip x1,x2,.. --cmd start|stop|restart"
	print "superstar.py -M modulename,[xx,xx] -c start|stop|restart --Mod mod1,mod2 --cmd start|stop|restart"
	print "superstar.py -i ipaddr,[xx,xx] -M modulename,[xx,xx] -c start|stop|restart"
	print '''---------------------------------------------------------------------------------------
For examples:
1 for general usage:
  python superstar.py -a -c start
  python superstar.py -M log -c start
  python superstar.py -i 192.168.199.117,192.168.199.118 -c start
  python superstar.py -i 192.168.199.117,192.168.199.118 -M log -c start
---------------------------------------------------------------------------------------\033[0m'''

def check_Ip(ip):
	hosts = []
	hosts_ok = []
	iphost = t.findAllHosts()
	for h in iphost:
		hosts.append(str(h[0]))
	for i in ip:
		if i not in hosts:
			print "\033[1;31;40m%s module not exist,please check!\033[0m" %i
			#continue
			sys.exit(3)

def check_ModName(mod):
	modnames = []
	modulename = t.findAllPubName()
	for m in modulename:
		modnames.append(str(m[0]))
	for mn in mod:
		if mn not in modnames:
			print "\033[1;31;40mModName %s not exist,please check!\033[0m" %mn
			print 30*'*'
			print "\033[1;33;40mInput Reference ModName:\033[0m" 
			for m in modnames:
				print "\033[1;33;40m%s\033[0m" %m
			sys.exit(3)

if len(sys.argv) != 1:
        if "-" in sys.argv:
                print "\033[1;31;40merror argv:-,please modify!\033[0m"
                sys.exit(3)
parser = OptionParser(add_help_option=0)
parser.add_option("-h", "--help", action="callback", callback=helpFunc)
parser.add_option("-c", "--cmd", action="store", type="string", dest="cmd",default="")
parser.add_option("-a", "--all", action="store_true", dest="all")
parser.add_option("-i", "--ip", action="store", type="string", dest="ip", default="")
parser.add_option("-M", "--Mod", action="store", type="string", dest="modname", default="")
parser.add_option("-m", "--mid", action="store", type="string", dest="mid",default="")
parser.add_option("-n", "--number", action="store", type="string", dest="number",default="")
parser.add_option("-f", "--force", action="store_true", dest="killforce")

(options, args) = parser.parse_args()
runcmd=options.cmd
runall=options.all
runip=options.ip
mid=options.mid
runmod=options.modname
order=options.number.split(',')
commandoption=args
killforce=options.killforce
num=8

t = SQLClass()

user="zhuser"
userInfo = t.findUserPass(user)

for i in userInfo:
	port = int(i[0])
	passwd = str(i[1])

#启停所有模块函数 BEGIN

ip_list=[]
ip_cmd_list=[]
for ip in t.findAllIp():
	ip_list.append(ip[0])

input_ip_list=runip.strip().split(',') #获取-i给出的IP地址列表
all_ip_list=[]
input_mod_list=runmod.strip().split(',')
somemod=[]


def startAll(j):
	login = ParamikoClass(j,port,user,passwd)
	for ip in t.findIpcmd(j):
		cmd_1=ip[1].strip().split("/")[:-1]
		cmd_path="/".join(cmd_1)
		cmd_start=ip[1].strip().split("/")[-1]
		cmd_mod=ip[1].strip().split("/")[3]
		print "\033[32;1m%s %s has been started\033[0m"%(ip[0],cmd_mod)
		login.cmd_run("cd "+cmd_path+";/bin/sh "+ cmd_start)

def stopAll(j):
	login = ParamikoClass(j,port,user,passwd)
	for ip in t.findIpname(j):
		print "\033[31;1m%s %s has been killed\033[0m" %(ip[0],ip[1])
		if killforce == True :
			stopforce="-9"
		else:
			stopforce=""
		cmd="ps -ef|grep %s|grep -v grep|awk '{print $2}'|xargs kill %s " %(ip[1],stopforce)
		login.cmd_run(cmd)

def restartAll(j):
	for ip in t.findIpname(j):
		print "\033[31;1m%s %s has been killed\033[0m" %(ip[0],ip[1])
		login = ParamikoClass(ip[0],port,user,passwd)
		cmd="ps -ef|grep  %s|grep -v grep|awk '{print $2}'|xargs kill " %ip[1]
		login.cmd_run(cmd)

	for ip in t.findIpcmd(j):
		cmd_1=ip[1].strip().split("/")[:-1]
		cmd_path="/".join(cmd_1)
		cmd_start=ip[1].strip().split("/")[-1]
		cmd_mod=ip[1].strip().split("/")[3]
		login = ParamikoClass(ip[0],port,user,passwd)
		print "\033[32;1m%s %s has been started\033[0m"%(ip[0],cmd_mod)
		login.cmd_run("cd "+cmd_path+";sh "+ cmd_start)

def  startMod(ip):
	login = ParamikoClass(ip,port,user,passwd)
	for mod in input_mod_list:
		for i in t.findIpAndMod(ip,mod):
			cmd_start=i[1].strip().split("/")[-1]
			cmd_1=i[1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_mod=i[1].strip().split("/")[3]
			print "\033[32;1m%s %s has been started\033[0m" %(ip,cmd_mod)
			login.cmd_run("cd "+cmd_path+";/bin/sh "+ cmd_start)

def  stopMod(ip):
	login = ParamikoClass(ip,port,user,passwd)
	for mod in input_mod_list:
		for i in t.findIpAndMod(ip,mod):
			cmd_1=i[1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_mod=cmd_path.strip().split("/")[3]
			if killforce == True :
				stopforce="-9"
			else:
				stopforce=""
			cmd="ps -ef | grep -w %s | grep -v grep|awk '{print $2}' | xargs kill %s " %(cmd_mod,stopforce)
			#print cmd
			print "\033[31;1m%s %s has been killed\033[0m" %(ip,cmd_mod)
			login.cmd_run(cmd)

def  restartMod(ip):
	login = ParamikoClass(ip,port,user,passwd)
	for mod in input_mod_list:
		for i in t.findIpAndMod(ip,mod):
			cmd_1=i[1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_mod=cmd_path.strip().split("/")[3]
			cmd="ps -ef|grep -w %s|grep -v grep|awk '{print $2}'|xargs kill " %cmd_mod
			print "\033[31;1m%s %s has been killed\033[0m" %(ip,cmd_mod)
			login.cmd_run(cmd)

	for mod in input_mod_list:
		for i in t.findIpAndMod(ip,mod):
			cmd_start=i[1].strip().split("/")[-1]
			cmd_1=i[1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			login.cmd_run("cd "+cmd_path+";sh "+ cmd_start)

def startModAll(mod):
	infolist = t.findIpOnlyMod(mod,orderStr)
	modlen =  len(infolist)
	count = modlen/2
	linfo = modlen%2
	if linfo != 0:
		count = count+1
	if mid == "head":
		i = 0
		while i < count:
			login = ParamikoClass(infolist[i][0],port,user,passwd)
			cmd_1=infolist[i][1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_start=infolist[i][1].strip().split("/")[-1]
			cmd_mod=infolist[i][1].strip().split("/")[3]
			print "\033[32;1m%s %s has been started\033[0m"%(infolist[i][0],cmd_mod)
			login.cmd_run("cd "+cmd_path+";sh "+ cmd_start)
			i = i+1
	elif mid == "tail":
		i = count
		while i < modlen:
			login = ParamikoClass(infolist[i][0],port,user,passwd)
			cmd_1=infolist[i][1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_start=infolist[i][1].strip().split("/")[-1]
			cmd_mod=infolist[i][1].strip().split("/")[3]
			print "\033[32;1m%s %s has been started\033[0m"%(infolist[i][0],cmd_mod)
			login.cmd_run("cd "+cmd_path+";sh "+ cmd_start)
			i = i+1
	else:
		for ip in infolist:
			login = ParamikoClass(ip[0],port,user,passwd)
			cmd_1=ip[1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_start=ip[1].strip().split("/")[-1]
			cmd_mod=ip[1].strip().split("/")[3]
			print "\033[32;1m%s %s has been started\033[0m"%(ip[0],cmd_mod)
			login.cmd_run("cd "+cmd_path+";sh "+ cmd_start)

def stopModAll(mod):
	infolist = t.findIpOnlyMod(mod,orderStr)
	modlen =  len(infolist)
	count = modlen/2
	linfo = modlen%2
	if linfo != 0:
		count = count+1
	if mid == "head":
		i = 0
		while i < count:
			login = ParamikoClass(infolist[i][0],port,user,passwd)
			cmd_1=infolist[i][1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_mod=cmd_path.strip().split("/")[3]
			if killforce == True :
				stopforce="-9"
			else:
				stopforce=""
			cmd="ps -ef | grep -w %s | grep -v grep | awk '{print $2}' | xargs kill %s " %(cmd_mod,stopforce)
			print "\033[31;1m%s %s has been killed\033[0m" %(infolist[i][0],cmd_mod)
			login.cmd_run(cmd)
			i = i+1
	elif mid == "tail":
		i = count
		while i < modlen:
			login = ParamikoClass(infolist[i][0],port,user,passwd)
			cmd_1=infolist[i][1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_mod=cmd_path.strip().split("/")[3]
			if killforce == True :
				stopforce="-9"
			else:
				stopforce=""
			cmd="ps -ef | grep -w %s | grep -v grep | awk '{print $2}' | xargs kill %s " %(cmd_mod,stopforce)
			print "\033[31;1m%s %s has been killed\033[0m" %(infolist[i][0],cmd_mod)
			login.cmd_run(cmd)
			i = i+1
	else:
		for ip in infolist:
			login = ParamikoClass(ip[0],port,user,passwd)
			cmd_1=ip[1].strip().split("/")[:-1]
			cmd_path="/".join(cmd_1)
			cmd_mod=cmd_path.strip().split("/")[3]
			if killforce == True :
				stopforce="-9"
			else:
				stopforce=""
			cmd="ps -ef | grep -w %s | grep -v grep | awk '{print $2}' | xargs kill %s " %(cmd_mod,stopforce)
			print "\033[31;1m%s %s has been killed\033[0m" %(ip,cmd_mod)
			login.cmd_run(cmd)

def restartModAll(mod):
	for ip in  t.findIpOnlyMod(mod,orderStr):
		login = ParamikoClass(ip[0],port,user,passwd)
		cmd_1=ip[1].strip().split("/")[:-1]
		cmd_path="/".join(cmd_1)
		cmd_mod=cmd_path.strip().split("/")[3]
		cmd="ps -ef|grep -w %s|grep -v grep|awk '{print $2}'|xargs kill " %cmd_mod
		print "\033[31;1m%s %s has been killed\033[0m" %(ip[0],cmd_mod)
		login.cmd_run(cmd)

	for ip in  t.findIpOnlyMod(mod,orderStr):
		login = ParamikoClass(ip[0],port,user,passwd)
		cmd_1=ip[1].strip().split("/")[:-1]
		cmd_path="/".join(cmd_1)
		cmd_start=ip[1].strip().split("/")[-1]
		cmd_mod=ip[1].strip().split("/")[3]
		print "\033[32;1m%s %s has been started\033[0m"%(ip[0],cmd_mod)
		login.cmd_run("cd "+cmd_path+";sh "+ cmd_start)

#检查参数:ip,mod,mid是否合法兼容
if input_ip_list != ['']:
	check_Ip(input_ip_list)
if input_mod_list != ['']:
	check_ModName(input_mod_list)
if mid != "":
	if mid != "head" and mid != "tail":
		print "\033[1;31;40mmid not correct,please check!\033[0m"
		sys.exit(3)
if order != ['']:
	order_new = order
	order = ['']
	for i,j in enumerate(order_new):
		j = re.sub(r'[a-zA-Z]*',"",j,0)
		if j.find("-",0,len(j)) != -1:
			# j = j.upper().replace("CP","")
			oj=j.split('-')
			for iobj in range(int(oj[0]),int(oj[1])+1):
				order.append("CP%s"%iobj)
		else:
			order.append("CP%s"%j)
			# order.append(order_new[i].upper())
# if len(input_mod_list) != 1 and mid != "":
	# print "\033[1;31;40mmid and several modules cannot use together,please modify!\033[0m"
	# sys.exit(3)
if len(input_mod_list) != 1 and order != ['']:
	print "\033[1;31;40morder and several modules cannot use together,please modify!\033[0m"
	sys.exit(3)
if order != [''] and mid != "":
	print "\033[1;31;40mmid and order number cannot use together,please modify!\033[0m"
	sys.exit(3)
if order != [''] and input_ip_list != ['']:
	print "\033[1;31;40mip and order number cannot use together,please modify!\033[0m"
	sys.exit(3)
if input_ip_list != [''] and mid != "":
	print "\033[1;31;40mmid and ip cannot use together,please modify!\033[0m"
	sys.exit(3)

#逻辑层
orderStr = ""
if order != ['']:
	orderStr = " and ("
	for n in order:
		orderStr = orderStr + "CPname='%s' or "%n
	orderStr = re.sub(r' or $',")",orderStr,0)
#指定IP和mod名字
if len(input_mod_list[0]) != 0 and  runcmd == "start" and len(input_ip_list[0]) != 0:#模块名字 IP 命令三项同时存在
	pool = multiprocessing.Pool(processes=num)
	for  ip in input_ip_list:
		pool.apply_async(startMod,(ip,))
	pool.close()
	pool.join()

elif len(input_mod_list[0]) != 0 and  runcmd == "stop" and len(input_ip_list[0]) != 0:
	pool = multiprocessing.Pool(processes=num)
	for  ip in input_ip_list:
		pool.apply_async(stopMod,(ip,))
	pool.close()
	pool.join()

elif len(input_mod_list[0]) != 0 and  runcmd == "restart" and len(input_ip_list[0]) != 0:
	pool = multiprocessing.Pool(processes=num)
	for  ip in input_ip_list:
		pool.apply_async(restartMod,(ip,))
	pool.close()
	pool.join()

#指定 IP列表
elif len(input_mod_list[0]) == 0 and runcmd == "start" and len(input_ip_list[0]) != 0:
	pool = multiprocessing.Pool(processes=num)
	for j in input_ip_list:
		pool.apply_async(startAll,(j,))
	pool.close()
	pool.join()

elif len(input_mod_list[0]) == 0 and runcmd == "stop" and len(input_ip_list[0]) != 0:
	pool = multiprocessing.Pool(processes=num)
	for j in input_ip_list:
		pool.apply_async(stopAll,(j,))
	pool.close()
	pool.join()

elif len(input_mod_list[0]) == 0 and runcmd == "restart" and len(input_ip_list[0]) != 0:
	pool = multiprocessing.Pool(processes=num)
	for j in input_ip_list:
		pool.apply_async(restartAll,(j,))
	pool.close()
	pool.join()

#指定 module列表
elif len(input_ip_list[0]) == 0 and runcmd == "start" and len(input_mod_list[0]) != 0:
	pool = multiprocessing.Pool(processes=num)
	for mod in input_mod_list:
		pool.apply_async(startModAll,(mod,))
	pool.close()
	pool.join()

elif len(input_ip_list[0]) == 0 and runcmd == "stop" and len(input_mod_list[0]) != 0:
	pool = multiprocessing.Pool(processes=num)
	for mod in input_mod_list:
		pool.apply_async(stopModAll,(mod,))
	pool.close()
	pool.join()

elif len(input_ip_list[0]) == 0 and runcmd == "restart" and len(input_mod_list[0]) != 0:
	pool = multiprocessing.Pool(processes=num)
	for mod in input_mod_list:
		pool.apply_async(restartModAll,(mod,))
	pool.close()
	pool.join()

#全部模块启停
elif  runcmd == "start":
	pool = multiprocessing.Pool(processes=num)
	for  ip in ip_list:
		pool.apply_async(startAll,(ip,))
	pool.close()
	pool.join()

elif  runcmd == "stop":
	pool = multiprocessing.Pool(processes=num)
	for  ip in ip_list:
		pool.apply_async(stopAll,(ip,))
	pool.close()
	pool.join()

elif  runcmd == "restart":
	pool = multiprocessing.Pool(processes=num)
	for  ip in ip_list:
		pool.apply_async(restartAll,(ip,))
	pool.close()
	pool.join()

else:
	print "wrong args"


