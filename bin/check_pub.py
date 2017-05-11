#!/usr/bin/env python
# encoding:utf-8
__author__ = 'sainter'

import sys
sys.path.append("..")
from lib.ParamikoClass import *
from lib.PublicSQLClass import *
import subprocess
import multiprocessing
from optparse import OptionParser
import re

t = SQLClass()
user = 'zhuser'
userInfo = t.findUserPass(user)
for i in userInfo:
	port = int(i[0])
	passwd = str(i[1])

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass

	try:
		import unicodedata
		unicodedata.numeric(s)
		return True
	except (TypeError, ValueError):
		pass

	return False

def helpFunc(a,b,c,d):
	print "USAGE:"
	print "EXAMPLE: '\033[1;33;40mpython %s -i IpAddr -M ModuleName\033[0m' or '\033[1;33;40mpython %s -a -s\033[0m'" %(sys.argv[0],sys.argv[0])
	print "-h or --help for help."
	print "-M or --module for modulename,can use ',' example:\033[1;33;40m python %s -M acp,cmp,nav\033[0m" %sys.argv[0]
	print "-m or --mid for mid,can use ',' example:\033[1;33;40m python %s -m head/tail \033[0m" %sys.argv[0]
	print "-i or --ip for ip address,can use ',' example:\033[1;33;40m python %s -i 192.168.199.117,192.168.199.118\033[0m" %sys.argv[0]
	print "-a or --all for all module check',' example:\033[1;33;40m python %s -a\033[0m" %sys.argv[0]
	sys.exit(3)

def verFunc(a,b,c,d):
	print "Version 2.0"
	sys.exit(0)

parser = OptionParser(add_help_option=0)
parser.add_option("-h", "--help", action="callback", callback=helpFunc)
parser.add_option("-v", "-V", "--version", action="callback", callback=verFunc)
parser.add_option("-M", "--module", action="store", type="string", dest="module",default="")
parser.add_option("-m", "--mid", action="store", type="string", dest="mid",default="")
parser.add_option("-i", "--ip", action="store", type="string", dest="ip",default="")
parser.add_option("-a", "--all", action="store_true", dest="all",default=False)
parser.add_option("-n", "--number", action="store", type="string", dest="number",default="")
(options, args) = parser.parse_args()
mod=options.module.split(',')
mid=options.mid
ip=options.ip.split(',')
all=options.all
order=options.number.split(',')
commandoption=args

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
				print "\033[1;33;40m%s\033[0m" %m,
			sys.exit(3)

def checkmoduleinfo(moduleinfo):
	host = moduleinfo[0]
	publicname = moduleinfo[1]
	startcmd = moduleinfo[2]
	moduleport = moduleinfo[3]
	startcmd4word = startcmd.split('/')[3]
	tailstring = startcmd4word.split('_')[-1]
	p = ParamikoClass(host,port,user,passwd)
	ps = "ps -ef|grep -w %s|grep -v supervise|grep -v grep|grep -v python > /dev/null && echo '1' || echo '0'" %(startcmd4word)
	result_ps = p.check_cmd(ps).strip()
	##add netstat
	portnumber = len(moduleport.split(';'))
	if publicname == 'pub_message_server' or publicname == 'message_redis':
		if is_number(tailstring):
			publicname = '%s_%s'%(publicname,tailstring)
		if result_ps == '1':
			print "%s %s %s \033[1;32;40mstart OK\033[0m" %(host,publicname,moduleinfo[4])
		else:
			print "%s %s %s \033[1;31;40mnot start\033[0m" %(host,publicname,moduleinfo[4])
	else:
		if is_number(tailstring):
			publicname = '%s_%s'%(publicname,tailstring)
		cmd_netstat = "netstat -an|grep LISTEN|grep tcp|grep -w '%s'|wc -l" %(moduleport)
		result_netstat_count = int(p.check_cmd(cmd_netstat).strip())
		if result_netstat_count != 0 and result_ps == '1':
			print "%s %s %s \033[1;32;40mstart OK\033[0m" %(host,publicname,moduleinfo[4])
		else:
			print "%s %s %s \033[1;31;40mnot start\033[0m" %(host,publicname,moduleinfo[4])

def multipoolcess(moduleinfo):
	pool = multiprocessing.Pool(processes=8)
	# modlen =  len(moduleinfo)
	# count = modlen/2
	# linfo = modlen%2
	# if linfo != 0:
		# count = count+1
	# if mid == "head":
		# i = 0
		# while i < count:
			# pool.apply_async(checkmoduleinfo,(moduleinfo[i],))
			# i = i+1
	# elif mid == "tail":
		# i = count
		# while i < modlen:
			# pool.apply_async(checkmoduleinfo,(moduleinfo[i],))
			# i = i+1
	# else:		
	for i in moduleinfo:
		pool.apply_async(checkmoduleinfo,(i,))
	pool.close()
	pool.join()

#检查参数:ip,mod,mid是否合法兼容
if ip != ['']:
	check_Ip(ip)
if mod != ['']:
	check_ModName(mod)
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
# if len(mod) != 1 and mid != "":
	# print "\033[1;31;40mmid and several modules cannot use together,please modify!\033[0m"
	# sys.exit(3)
if len(mod) != 1 and order != ['']:
	print "\033[1;31;40morder and several modules cannot use together,please modify!\033[0m"
	sys.exit(3)
if order != [''] and mid != "":
	print "\033[1;31;40mmid and order number cannot use together,please modify!\033[0m"
	sys.exit(3)
if order != [''] and ip != ['']:
	print "\033[1;31;40mip and order number cannot use together,please modify!\033[0m"
	sys.exit(3)
if ip != [''] and mid != "":
	print "\033[1;31;40mmid and ip cannot use together,please modify!\033[0m"
	sys.exit(3)
if order != [''] and all == True:
	print "\033[1;31;40m-a and order number cannot use together,please modify!\033[0m"
	sys.exit(3)

tmplist = []
moduleinfo = []
iplist = []
def moduleappend(list):
	newList = []
	for i in list:
		for n in i:
			newList.append(n)
	return newList

if ip != [''] and mod == ['']:
	for i in ip:
		tmplist.append(t.findModByIP(i))
	moduleinfo = moduleappend(tmplist)
	multipoolcess(moduleinfo)
#mod_check
elif mod != [''] and ip == ['']:
	orderStr = ""
	if order != ['']:
		orderStr = " and ("
		for n in order:
			orderStr = orderStr + "CPname='%s' or "%n
		orderStr = re.sub(r' or $',")",orderStr,0)
	for m in mod:
		getList = []
		getList.append(t.findModByModName(m,orderStr))
		list = moduleappend(getList)
		modlen =  len(list)
		count = modlen/2
		linfo = modlen%2
		if linfo != 0:
			count = count+1
		if mid == "head":
			i = 0
			while i < count:
				moduleinfo.append(list[i])
				i = i+1
		elif mid == "tail":
			i = count
			while i < modlen:
				moduleinfo.append(list[i])
				i = i+1
		else:
			for i in list:
				moduleinfo.append(i)
	# moduleinfo = moduleappend(tmplist)
	multipoolcess(moduleinfo)
##mod_and_ip_check
elif mod != [''] and ip != ['']:
	for i in ip:
		for m in mod:
			tmplist.append(t.findModByModAndIP(i,m))
	moduleinfo = moduleappend(tmplist)
	multipoolcess(moduleinfo)
##check_all
elif all == True:
	ip = t.findHosts()
	for i in ip:
		iplist.append(str(i[0]))
	for i in iplist:
		tmplist.append(t.findModByIP(i))
	moduleinfo = moduleappend(tmplist)
	multipoolcess(moduleinfo)
else:
	print('\033[1;31;40mInput Error!!!please use -h for help!!!\033[0m')

