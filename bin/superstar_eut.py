#!/usr/bin/env python
# encoding:utf-8


import sys
import os
sys.path.append("..")
from lib.LogicSQLClass import *
from lib.ParamikoClass import *

import multiprocessing
from optparse import OptionParser
import time

def helpFunc(a,b,c,d):
	print "\033[32;1mFor help:"
	print "superstar.py [-a (All ip) -i (IP address,xx1,xx2..) -M (Module name) -s (Super mode) -c (start|stop)]"
	print "superstar.py -a -c start|stop --all --cmd start|stop"
	print "superstar.py -i ipaddr,[xx,xx] -c start|stop --ip x1,x2,.. --cmd start|stop"
	print "superstar.py -M modulename,[xx,xx] -c start|stop --Mod mod1,mod2 --cmd start|stop"
	print "superstar.py -i ipaddr,[xx,xx] -M modulename,[xx,xx] -c start|stop"
	print "superstar.py -s -a -c start|stop --all --cmd start|stop"
	print "superstar.py -s -i ipaddr,[xx,xx] -c start|stop --ip x1,x2,.. --cmd start|stop"
	print "superstar.py -s -M modulename,[xx,xx] -c start|stop --Mod mod1,mod2 --cmd start|stop"
	print "superstar.py -s -i ipaddr,[xx,xx] -M modulename,[xx,xx] -c start|stop"
	print '''---------------------------------------------------------------------------------------
For examples:
1 for general usage:
  python superstar.py -a -c start
  python superstar.py -M log -c start
  python superstar.py -i 192.168.199.117,192.168.199.118 -c start
  python superstar.py -i 192.168.199.117,192.168.199.118 -M log -c start
2 for super usage:
  python superstar.py -s -a -c start
  python superstar.py -s -M log -c start
  python superstar.py -s -i 192.168.199.117,192.168.199.118 -c start
  python superstar.py -s -i 192.168.199.117,192.168.199.118 -M log -c start
---------------------------------------------------------------------------------------\033[0m'''
def check_Ip(ip):
	hosts = []
	hosts_ok = []
	iphost = t.findHosts()
	for h in iphost:
		hosts.append(str(h[0]))
	ip = {}.fromkeys(ip).keys()
	for i in ip:
		if i not in hosts:
			print "\033[1;31;40m%s not exist,please check!\033[0m" %i
			#continue
			sys.exit(3)

def check_ModName(mod):
	modnames = []
	modulename = t.findModName()
	for m in modulename:
		modnames.append(str(m[0]))
	for mn in mod:
		if mn not in modnames:
			print "\033[1;31;40mModName %s not exist,please check!\033[0m" %mn
			print 30*'*'
			print "\033[1;33;40mInput Reference ModName:\033[0m" 
			for m in modnames:
				print "\033[1;33;40m%s\033[0m" %m,
			sys.exit(3)

parser = OptionParser(add_help_option=0)
parser.add_option("-h", "--help", action="callback", callback=helpFunc)
parser.add_option("-c", "--cmd", action="store", type="string", dest="cmd",default="")
parser.add_option("-a", "--all", action="store_true", dest="all")
parser.add_option("-i", "--ip", action="store", type="string", dest="ip", default="")
parser.add_option("-M", "--Mod", action="store", type="string", dest="modname", default="")
parser.add_option("-m", "--mid", action="store", type="string", dest="mid",default="")
parser.add_option("-s", "--super", action="store_true", dest="super")
parser.add_option("-f", "--force", action="store_true", dest="killforce")

(options, args) = parser.parse_args()
runcmd=options.cmd
runall=options.all
runip=options.ip
runmod=options.modname
mid=options.mid
runsuper=options.super
commandoption=args
killforce=options.killforce
num=8

t = SQLClass()

#获取数据库中机器的用户名，端口和密码
userInfo = t.findUserPass('zhuser')
for i in userInfo:
	user = i[0]
	port = int(i[1])
	passwd = i[2]

#启停所有模块函数,传入IP参数启停该机器上所有模块，除supervise进程外。 BEGIN

#启动configcenter模块。
def startAll(ip):
	login = ParamikoClass(ip[0],port,user,passwd)
	for md in t.findipConfPath(ip[0]):
		module=md[0].strip().split("/")[-1]
		cmd="cd %s;bash startAndStop.sh start %s;exit;" %(md[0],module)
		login.cmd_run(cmd)
		print "\033[32;1m%s : %s is ok\033[0m" %(ip[0],module)

#启动除configcenter之外的所有模块
def startAllother(ip):
	 login = ParamikoClass(ip[0],port,user,passwd)
	 for md in t.findipOtherPath(ip[0]):
		module=md[0].strip().split("/")[-1]
		cmd="cd %s;bash startAndStop.sh start %s;exit;" %(md[0],module)
		login.cmd_run(cmd)
		print "\033[32;1m%s : %s is ok\033[0m" %(ip[0],module)

#停掉机器上所有模块
def stopAll(ip):
	login = ParamikoClass(ip[0],port,user,passwd)
	if killforce == True :
		stopforce="-9"
	else:
		stopforce=""
	cmd="ps -ef|grep '/home/zhuser/jdk1.7.0_25/bin/java'|grep -v grep|awk '{print $2}'|xargs kill %s "%stopforce
	login.cmd_run(cmd)
	print "\033[31;1m %s has been killed.\033[0m" %(ip[0])
#启停所有模块函数 END


#启停指定IP地址的函数 BEGIN
def startfor_specified_ip(ip):
	login = ParamikoClass(ip,port,user,passwd)
	for md in t.findipConfPath(ip):
		module=md[0].strip().split("/")[-1]
		cmd="cd %s;bash startAndStop.sh start %s;exit;" %(md[0],module)
		login.cmd_run(cmd)
		print "\033[32;1m%s : %s is ok\033[0m" %(ip,module)
		time.sleep(5)

	for md in t.findipOtherPath(ip):
		module=md[0].strip().split("/")[-1]
		cmd="cd %s;bash startAndStop.sh start %s;exit;" %(md[0],module)
		login.cmd_run(cmd)
		print "\033[32;1m%s : %s is ok\033[0m" %(ip,module)

def stopfor_specified_ip(ip):
	login = ParamikoClass(ip,port,user,passwd)
	if killforce == True :
		stopforce="-9"
	else:
		stopforce=""
	cmd="ps -ef|grep '/home/zhuser/jdk1.7.0_25/bin/java'|grep -v grep|awk '{print $2}'|xargs kill %s "%stopforce
	login.cmd_run(cmd)
	print "\033[31;1m %s has been killed.\033[0m" %(ip)
#启停指定IP地址的函数 BEGIN

#启动指定模块的函数
def startMod(j):
	ip = j[0]
	mod = j[1]
	login = ParamikoClass(ip,port,user,passwd)
	module=mod.strip().split("/")[-1]
	#cmd="cd %s\n/home/zhuser/jdk1.7.0_25/bin/java -jar %s.jar recover > nohup.out 2>&1 &\nexit\n" %(mod,module)
	cmd="cd %s;bash startAndStop.sh start %s;exit;" %(mod,module)
	login.cmd_run(cmd)
	print "\033[32;1m%s : %s is ok\033[0m" %(ip,module)
#停止指定模块的函数
def stopMod(j):
	login = ParamikoClass(j[0],port,user,passwd)
	module=j[1].strip().split("/")[-1]
	if killforce == True :
		stopforce="-9"
	else:
		stopforce=""
	cmd="cd %s;bash startAndStop.sh stop %s %s;exit;" %(j[1],module,stopforce)
	#print cmd
	login.cmd_run(cmd)
	print "\033[31;1m %s:[%s] has been killed.\033[0m" %(j[0],module)
'''
#super 启动configcenter模块。
def superstartAll(ip):
	login = ParamikoClass(ip[0],port,user,passwd)
	for md in t.findipConfPath(ip[0]):
		module=md[0].strip().split("/")[-1]
		cmd="/usr/local/bin/supervise /opt/supervise/%s >/dev/null  &" %(module)
		login.cmd_run(cmd)
		print "\033[32;1m%s :Super %s is ok\033[0m" %(ip[0],module)

def superstartAllother(ip):#super方式启动除configcenter之外的服务
	login = ParamikoClass(ip[0],port,user,passwd)
	for md in t.findipOtherPath(ip[0]):
		module=md[0].strip().split("/")[-1]
		cmd="/usr/local/bin/supervise /opt/supervise/%s >/dev/null  &" %(module)
		login.cmd_run(cmd)
		print "\033[32;1m%s :Super %s is ok\033[0m" %(ip[0],module)

def superstopAll(ip):#super方式停止所有
	login = ParamikoClass(ip[0],port,user,passwd)
	cmd="ps -ef|egrep '(supervise|/home/zhuser/jdk1.7.0_25/bin/java -jar)'|grep -v grep|awk '{print $2}'|xargs kill "
	login.cmd_run(cmd)
	print "\033[31;1m %s has been killed.\033[0m" %(ip[0])

def superstartOnly(ip):#super方式启动指定IP地址
	login = ParamikoClass(ip,port,user,passwd)
	for md in t.findipConfPath(ip):
		module=md[0].strip().split("/")[-1]
		cmd="/usr/local/bin/supervise /opt/supervise/%s >/dev/null  &" %(module)
		login.cmd_run(cmd)
		print "\033[32;1m%s :Super %s is ok\033[0m" %(ip[0],module)
		time.sleep(5)

	for md in t.findipOtherPath(ip):
		module=md[0].strip().split("/")[-1]
		cmd="/usr/local/bin/supervise /opt/supervise/%s >/dev/null  &" %(module)
		login.cmd_run(cmd)
		print "\033[32;1m%s :Super %s is ok\033[0m" %(ip,module)

def superstopOnly(ip):#super方式停止指定IP地址
	login = ParamikoClass(ip,port,user,passwd)
	cmd="ps -ef|egrep '(supervise|/home/zhuser/jdk1.7.0_25/bin/java -jar)'|grep -v grep|awk '{print $2}'|xargs kill "
	login.cmd_run(cmd)
	print "\033[31;1m %s has been killed.\033[0m" %(ip)

def superrunMod(j):#super方式启动模块
	ip = j[0]
	mod = j[1]
	login = ParamikoClass(ip,port,user,passwd)
	module=mod.strip().split("/")[-1]
	#cmd="cd %s\n/home/zhuser/jdk1.7.0_25/bin/java -jar %s.jar > nohup.out 2>&1 &\nexit\n" %(mod,module)
	cmd="/usr/local/bin/supervise /opt/supervise/%s >/dev/null  &" %(module)
	login.cmd_run(cmd)
	print "\033[32;1m%s :Super %s is ok\033[0m" %(ip,module)

def superstopMod(j):#super方式停止模块
	login = ParamikoClass(j[0],port,user,passwd)
	module=j[1].strip().split("/")[-1]
	#cmd="ps -ef|grep '/home/zhuser/jdk1.7.0_25/bin/java -jar'|grep -v grep|awk '{print $2}'|xargs kill "
	cmd="ps -ef|egrep '(supervise|/home/zhuser/jdk1.7.0_25/bin/java -jar %s)'|grep -v grep|awk '{print $2}'|xargs kill " %(module)
	login.cmd_run(cmd)
	print "\033[31;1m %s:Super [%s] has been killed.\033[0m" %(j[0],module)

def superrunApp():#super方式启停所有的服务
	if len(runcmd) == 0:
		print "\033[31;1m Command can't be null\033[0m"
		sys.exit(3)
	elif runcmd == "start":
		for ip in t.findHosts():
			superstartAll(ip)
		time.sleep(6)
		pool = multiprocessing.Pool(processes=num)
		for ip in t.findHosts():
			pool.apply_async(superstartAllother,(ip,))
		pool.close()
		pool.join()

	elif runcmd == "stop":
		pool = multiprocessing.Pool(processes=num)
		for ip in t.findHosts():
			pool.apply_async(superstopAll,(ip,))
		pool.close()
		pool.join()

	else:
		print "wrong args"

def superrunOnlyApp():#super方式启停指定IP地址的服务
	if len(runcmd) == 0:
		print "\033[31;1m Command can't be null\033[0m"
		sys.exit(3)
	elif runcmd == "start":
		pool = multiprocessing.Pool(processes=num)
		for ip in input_ip_list:
			if ip in all_ip_list:
				pool.apply_async(superstartOnly,(ip,))
			else:
				print "[\033[33;1m%s is not exist\033[0m]" %(ip)
		pool.close()
		pool.join()

	elif runcmd == "stop":
		pool = multiprocessing.Pool(processes=num)
		for ip in input_ip_list:
			if ip in all_ip_list:
				pool.apply_async(superstopOnly,(ip,))
			else:
				print "[\033[33;1m%s is not exist\033[0m]" %(ip)
		pool.close()
		pool.join()

	else:
		print "wrong args"
'''

def runApp():#启停所有服务的函数
	if len(runcmd) == 0:
		print "\033[31;1m Command can't be null\033[0m"
		sys.exit(3)
	elif runcmd == "start":
		for ip in t.findHosts():
			startAll(ip)
		time.sleep(6)

		pool = multiprocessing.Pool(processes=num)
		for ip in t.findHosts():
			pool.apply_async(startAllother,(ip,))
		pool.close()
		pool.join()

	elif runcmd == "stop":
		pool = multiprocessing.Pool(processes=num)
		for ip in t.findHosts():
			pool.apply_async(stopAll,(ip,))
		pool.close()
		pool.join()

	else:
		print "wrong args"

def run_some(): #指定IP地址启停的函数
	if len(runcmd) == 0:
		print "\033[31;1m Command can't be null\033[0m"
		sys.exit(3)
	elif runcmd == "start":
		pool = multiprocessing.Pool(processes=num)
		for ip in input_ip_list:
			if ip in all_ip_list:
				pool.apply_async(startfor_specified_ip,(ip,))
			else:
				print "[\033[33;1m%s is not exist\033[0m]" %(ip)
		pool.close()
		pool.join()

	elif runcmd == "stop":
		pool = multiprocessing.Pool(processes=num)
		for ip in input_ip_list:
			if ip in all_ip_list:
				pool.apply_async(stopfor_specified_ip,(ip,))
			else:
				print "[\033[33;1m%s is not exist\033[0m]" %(ip)
		pool.close()
		pool.join()

	else:
		print "wrong args"

pool = multiprocessing.Pool(processes=num)#指定并发进程数量
input_ip_list=runip.strip().split(',') #获取-i给出的IP地址列表
all_ip_list=[]#IP列表
input_mod_list=runmod.strip().split(',')#取出参数中所有的模块
somemod=[]
infolist = []

#检查参数:ip,mod,mid是否合法兼容
if input_ip_list != ['']:
	check_Ip(input_ip_list)
if input_mod_list != ['']:
	check_ModName(input_mod_list)
if mid != "":
	if mid != "head" and mid != "tail":
		print "\033[1;31;40mmid not correct,please check!\033[0m"
		sys.exit(3)
if len(input_mod_list) != 1 and mid != "":
	print "\033[1;31;40mmid and several modules cannot use together,please modify!\033[0m"
	sys.exit(3)

if input_ip_list != [''] and mid != "":
	print "\033[1;31;40mmid and ip cannot use together,please modify!\033[0m"
	sys.exit(3)

#普通模式(不带supervise)
if runsuper != True:
	if len(input_mod_list[0]) != 0 and  runcmd == "start" and len(input_ip_list[0]) != 0:#如果指定了IP地址，命令start和模块名。
		for  ip in input_ip_list:
			for mod in input_mod_list:
				somemod.append(t.QTfindPath(mod,ip))
		for w in somemod:
			for j in w:
				infolist.append(j)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					pool.apply_async(startMod,(infolist[i],))
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					pool.apply_async(startMod,(infolist[i],))
					i = i+1
			else:		
				for i in infolist:
					pool.apply_async(startMod,(i,))
			pool.close()
			pool.join()
		else:
			print('Error!please check db file!!')

	elif len(input_mod_list[0]) != 0 and  runcmd == "stop" and len(input_ip_list[0]) != 0:#如果指定了IP地址，命令stop和模块名。
		for  ip in input_ip_list:
			for mod in input_mod_list:
				somemod.append(t.QTfindPath(mod,ip))
		for w in somemod:
			for j in w:
				infolist.append(j)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					pool.apply_async(stopMod,(infolist[i],))
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					pool.apply_async(stopMod,(infolist[i],))
					i = i+1
			else:		
				for i in infolist:
					pool.apply_async(stopMod,(i,))
			pool.close()
			pool.join()
		else:
			print('Error!please check db file!!')

	elif len(input_mod_list[0]) != 0 and  runcmd == "start":#如果指定了模块名字和命令start。
		for i in input_mod_list:
			for j in t.QTfindIp(i):
				infolist.append(j)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					pool.apply_async(startMod,(infolist[i],))
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					pool.apply_async(startMod,(infolist[i],))
					i = i+1
			else:		
				for i in infolist:
					pool.apply_async(startMod,(i,))
			pool.close()
			pool.join()
		else:
			print('Error!please check db file!!')

	elif len(input_mod_list[0]) != 0 and  runcmd == "stop":#如果指定了模块名字和命令stop。
		for i in input_mod_list:
			for j in t.QTfindIp(i):
				infolist.append(j)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					pool.apply_async(stopMod,(infolist[i],))
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					pool.apply_async(stopMod,(infolist[i],))
					i = i+1
			else:		
				for i in infolist:
					pool.apply_async(stopMod,(i,))
			pool.close()
			pool.join()
		else:
			print('Error!please check db file!!')

	elif len(input_ip_list[0]) != 0 : #只指定IP地址
		for i in t.findHosts():
			all_ip_list.append(str(i[0]))
		run_some()

	elif runall == True:#指定-a，runall为true，执行所有操作
		runApp()

	else:
		helpFunc('a','b','c','d')
"""
else:

#进入supervise 模块式
	if len(input_mod_list[0]) != 0 and  runcmd == "start" and len(input_ip_list[0]) != 0:#如果指定了IP地址，命令start和模块名。
		for  ip in input_ip_list:
			for mod in input_mod_list:
				somemod.append(t.QTfindPath(mod,ip))
		for w in somemod:
			for j in w:
				infolist.append(j)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					pool.apply_async(superrunMod,(infolist[i],))
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					pool.apply_async(superrunMod,(infolist[i],))
					i = i+1
			else:		
				for i in infolist:
					pool.apply_async(superrunMod,(i,))
			pool.close()
			pool.join()
		else:
			print('Error!please check db file!!')

	elif len(input_mod_list[0]) != 0 and  runcmd == "stop" and len(input_ip_list[0]) != 0:#如果指定了IP地址,命令stop和模块名。
		for  ip in input_ip_list:
			for mod in input_mod_list:
				somemod.append(t.QTfindPath(mod,ip))
		for w in somemod:
			for j in w:
				infolist.append(j)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					pool.apply_async(superstopMod,(infolist[i],))
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					pool.apply_async(superstopMod,(infolist[i],))
					i = i+1
			else:		
				for i in infolist:
					pool.apply_async(superstopMod,(i,))
			pool.close()
			pool.join()
		else:
			print('Error!please check db file!!')

	elif len(input_mod_list[0]) != 0 and  runcmd == "start":#只指定了模块名和start命令
		for i in input_mod_list:
			for j in t.QTfindIp(i):
				infolist.append(j)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					pool.apply_async(superrunMod,(infolist[i],))
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					pool.apply_async(superrunMod,(infolist[i],))
					i = i+1
			else:		
				for i in infolist:
					pool.apply_async(superrunMod,(i,))
			pool.close()
			pool.join()
		else:
			print('Error!please check db file!!')

	elif len(input_mod_list[0]) != 0 and  runcmd == "stop":#只指定了模块名和stop命令
		for i in input_mod_list:
			for j in t.QTfindIp(i):
				infolist.append(j)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					pool.apply_async(superstopMod,(infolist[i],))
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					pool.apply_async(superstopMod,(infolist[i],))
					i = i+1
			else:		
				for i in infolist:
					pool.apply_async(superstopMod,(i,))
			pool.close()
			pool.join()
		else:
			print('Error!please check db file!!')


	elif len(input_ip_list[0]) != 0 : #如果只指定IP地址
		for i in t.findHosts():
			all_ip_list.append(str(i[0]))
		superrunOnlyApp()

	elif runall == True:#指定-a runall为true，执行所有操作
		superrunApp()

	else:
		helpFunc('a','b','c','d')
"""
