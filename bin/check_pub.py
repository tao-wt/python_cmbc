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
	#print "-m or --mid for mid,can use ',' example:python %s -m 1035001,1038001." %sys.argv[0]
	print "-i or --ip for ip address,can use ',' example:\033[1;33;40m python %s -i 192.168.199.117,192.168.199.118\033[0m" %sys.argv[0]
	print "-a or --all for all module check',' example:\033[1;33;40m python %s -a\033[0m" %sys.argv[0]
	#print "-s or --super yes or not check supervise,default:False. example:python %s -a -s." %sys.argv[0]
	sys.exit(3)

def verFunc(a,b,c,d):
	print "Version 0.1.2"
	sys.exit(3)

parser = OptionParser(add_help_option=0)
parser.add_option("-h", "--help", action="callback", callback=helpFunc)
parser.add_option("-v", "-V", "--version", action="callback", callback=verFunc)
parser.add_option("-M", "--module", action="store", type="string", dest="module",default="")
parser.add_option("-m", "--mid", action="store", type="string", dest="mid",default="")
parser.add_option("-i", "--ip", action="store", type="string", dest="ip",default="")
parser.add_option("-a", "--all", action="store_true", dest="all",default=False)
parser.add_option("-s", "--super", action="store_true", dest="super",default=False)
(options, args) = parser.parse_args()
mod=options.module.split(',')
mid=options.mid
ip=options.ip.split(',')
all=options.all
super=options.super
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
			print "%s %s \033[1;32;40mstart OK\033[0m" %(host,publicname)
		else:
			print "%s %s \033[1;31;40mnot start\033[0m" %(host,publicname)
	else:
		if is_number(tailstring):
			publicname = '%s_%s'%(publicname,tailstring)
		cmd_netstat = "netstat -an|grep LISTEN|grep tcp|grep -w '%s'|wc -l" %(moduleport)
		result_netstat_count = int(p.check_cmd(cmd_netstat).strip())
		if result_netstat_count == 1 and result_ps == '1':
			print "%s %s \033[1;32;40mstart OK\033[0m" %(host,publicname)
		else:
			print "%s %s \033[1;31;40mnot start\033[0m" %(host,publicname)

    #if portnumber == 2:
    #  count = 0
    #  for i in moduleport.split(";"):
    #    cmd_netstat = "netstat -an|grep LISTEN|grep tcp|grep '%s'|wc -l" %(i)
    #    result_netstat_count = int(p.check_cmd(cmd_netstat).strip())
    #    count = count + result_netstat_count
    #  if count == portnumber and result_ps == '1':
    #    print "%s %s \033[1;32;40mstart OK\033[0m" %(host,modulerunname)
    #  else:
    #    print "%s %s \033[1;31;40mnot start\033[0m" %(host,modulerunname)
    #elif portnumber == 1:
    #  cmd_netstat = "netstat -an|grep LISTEN|grep tcp|grep '%s' > /dev/null && echo '1' || echo '0'" %(moduleport)
    #  result_netstat = p.check_cmd(cmd_netstat).strip()
    #  if result_netstat == '1' and result_ps == '1':
    #    print "%s %s \033[1;32;40mstart OK\033[0m" %(host,modulerunname)
    #  else:
    #    print "%s %s \033[1;31;40mnot start\033[0m" %(host,modulerunname)


def multipoolcess(moduleinfo):
	pool = multiprocessing.Pool(processes=8)
	modlen =  len(moduleinfo)
	count = modlen/2
	linfo = modlen%2
	if linfo != 0:
		count = count+1
	if mid == "head":
		i = 0
		while i < count:
			pool.apply_async(checkmoduleinfo,(moduleinfo[i],))
			i = i+1
	elif mid == "tail":
		i = count
		while i < modlen:
			pool.apply_async(checkmoduleinfo,(moduleinfo[i],))
			i = i+1
	else:		
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
if len(mod) != 1 and mid != "":
	print "\033[1;31;40mmid and several modules cannot use together,please modify!\033[0m"
	sys.exit(3)
if ip != [''] and mid != "":
	print "\033[1;31;40mmid and ip cannot use together,please modify!\033[0m"
	sys.exit(3)

tmplist = []
moduleinfo = []
iplist = []
def moduleappend():
	for i in tmplist:
		for n in i:
			moduleinfo.append(n)

if ip != [''] and mod == [''] and super == False:
	for i in ip:
		tmplist.append(t.findModByIP(i))
	moduleappend()
	multipoolcess(moduleinfo)
#mod_check
elif mod != [''] and ip == [''] and super == False:
	for m in mod:
		tmplist.append(t.findModByModName(m))
	moduleappend()
	multipoolcess(moduleinfo)
##mod_and_ip_check
elif mod != [''] and ip != [''] and super == False:
	for i in ip:
		for m in mod:
			tmplist.append(t.findModByModAndIP(i,m))
	moduleappend()
	multipoolcess(moduleinfo)
##check_all
elif all == True and super == False:
	ip = t.findHosts()
	for i in ip:
		iplist.append(str(i[0]))
	for i in iplist:
		tmplist.append(t.findModByIP(i))
	moduleappend()
	multipoolcess(moduleinfo)
else:
	print('\033[1;31;40mInput Error!!!please use -h for help!!!\033[0m')

