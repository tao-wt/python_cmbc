#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'
import sys
import multiprocessing
import pexpect
import traceback
sys.path.append("..")
from lib.PublicSQLClass import *
from lib.ParamikoClass import *
from optparse import OptionParser
import re

t = SQLClass()
#全局变量，获取登陆用户属性
tomcatlist = ['pub_platform','pub_system','webmanager','pub_oauth_interface','pub_cmbc_interface','pub_wcmp','pub_crash_system','pub_es_interface','liveroom','liveinterface','livecontrol']
jbosslist = ['pub_authorization','pub_groupmsg']
homePath = '/home/zhuser/webhome/'
appPath = '/home/zhuser/webapp/'
user = 'zhuser'
userInfo = t.findUserPass(user)
for i in userInfo:
	port = i[0]
	passwd = str(i[1]) 

#申明帮助信息
def helpFunc(a,b,c,d):
	print "USAGE:"
	print "-h or --help for help."
	print "-M or --module for modulename,can use ',' example:pub_message"
	print "-i or --ip for ip address,can use ',' example:192.168.199.11,10.10.10.10."
	print "-a or --all for all ip address,list of db."
	print "-D or --deploy for deploy all app,use this option must be careful!"
	print "PUBLIST:pub_interface pub_message pub_message_server pub_platform pub_system webmanager"
	print "EXAMPLE: 'python %s -i 10.10.10.10 -M pub_platform'" %sys.argv[0]
	sys.exit(3)

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

#创建程序目录
def mkWebappDir(host):
	p = ParamikoClass(host,port,user,passwd)
	p.cmd_run('mkdir -p /opt/webhome')
	p.cmd_run('mkdir -p /opt/webapp')

#执行创建程序目录
def mkdirWebapp():
	pool = multiprocessing.Pool(processes=10)
	iplist = t.findAllHosts()
	for i in iplist:
		pool.apply_async(mkWebappDir,(i[0],))
	pool.close()
	pool.join()

#主进程，通过pexpect远程执行命令
def pexRun(host,cmd,password):
	try:
		child = pexpect.spawn(cmd)
		index = child.expect(['password:','continue connecting (yes/no)?',pexpect.EOF, pexpect.TIMEOUT])
		if index == 0:
			child.sendline(password)
			child.interact()
		elif index == 1:
			child.sendline('yes')
			child.expect(['password:'])
			child.sendline(password)
			child.interact()
		elif index == 2:
			print " %s 子程序异常，退出!" %host
			child.close()
		elif index == 3:
			print "%s 连接超时" %host
	except:
		traceback.print_exec()

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

#全量部署模块函数
def PublicDeploy(info):
	host = str(info[0])
	pubName = str(info[1])
	pubPath = str(info[2])
	cpName = str(info[3])
	tailstring = pubPath.strip().split("_")[-1]
	localHomeDir = '%s%s' %(homePath,pubName)
	localTomcatDir = '%stomcat_%s' %(appPath,pubName)
	remoteHomeDir = pubPath
	confDir = '%s' %remoteHomeDir
	cmdHome = 'rsync -arvz -e "ssh -p %s" %s/ %s@%s:%s' %(port,localHomeDir,user,host,remoteHomeDir)
	p = ParamikoClass(host,port,user,passwd)
	if pubName in tomcatlist:
		if is_number(tailstring):
			remoteTomcatDir = '/opt/webapp/tomcat_%s_%s'%(pubName,tailstring)
		else:
			remoteTomcatDir = '/opt/webapp/tomcat_%s'%pubName
		cmdApp = 'rsync -arvz -e "ssh -p %s" %s/ %s@%s:%s' %(port,localTomcatDir,user,host,remoteTomcatDir)
		pexRun(host,cmdApp,passwd)
		pexRun(host,cmdHome,passwd)
		cmd = 'find %s -name "servicesetting.properties"|xargs sed -i "/ComputerName/ s#CP01#%s#g"'\
		%(confDir,cpName)
		p.cmd_run(cmd)
		print('%s :upload \033[1;31;40m%s\033[0m \033[1;32;40mOK\033[0m'%(host,pubName))
	else:
		pexRun(host,cmdHome,passwd)
		cmd = 'find %s -name "servicesetting.properties"|xargs sed -i "/ComputerName/ s#CP01#%s#g"'\
		%(confDir,cpName)
		p.cmd_run(cmd)
		print('%s :upload \033[1;31;40m%s\033[0m \033[1;32;40mOK\033[0m'%(host,pubName))

#模块更新函数
def PublicDeployUpdate(info):
	host = str(info[0])
	pubName = str(info[1])
	pubPath = str(info[2])
	cpName = str(info[3])
	if pubName in tomcatlist:
		localHomeDir = '%s%s' %(homePath,pubName)
		localTomcatDir = '%stomcat_%s' %(appPath,pubName)
	elif pubName in jbosslist:
		localHomeDir = '%s%s_jboss' %(homePath,pubName)
		localTomcatDir = '%sjboss_%s' %(appPath,pubName)
	else:
		localHomeDir = '%s%s' %(homePath,pubName)
	remoteHomeDir = pubPath
	confDir = '%s' %remoteHomeDir
	cmdHome = 'rsync -arvz --exclude-from="exclude_file.txt" --delete -e "ssh -p %s" %s/ %s@%s:%s' %(port,localHomeDir,user,host,remoteHomeDir)
	p = ParamikoClass(host,port,user,passwd)
	if pubName in tomcatlist:
		remoteTomcatDir = '/opt/webapp/' 
		cmdApp = 'rsync -arvz -e "ssh -p %s" %s %s@%s:%s' %(port,localTomcatDir,user,host,remoteTomcatDir)
		#pexRun(host,cmdApp,passwd)
		pexRun(host,cmdHome,passwd)
		cmd = 'find %s -name "servicesetting.properties"|xargs sed -i "/ComputerName/ s#CP01#%s#g"'\
		%(confDir,cpName)
		p.cmd_run(cmd)
		print('%s :upload \033[1;31;40m%s\033[0m \033[1;32;40mOK\033[0m'%(host,pubName))
	elif pubName in jbosslist:
		remoteTomcatDir = '/opt/webapp/'
		cmdApp = 'rsync -arvz -e "ssh -p %s" %s %s@%s:%s' %(port,localTomcatDir,user,host,remoteTomcatDir)
		cmdHome = 'rsync -arvz --exclude-from="exclude_file.txt"  -e "ssh -p %s" %s %s@%s:%s' %(port,localHomeDir,user,host,remoteHomeDir)
		pexRun(host,cmdApp,passwd)
		pexRun(host,cmdHome,passwd)
		print('%s :upload \033[1;31;40m%s\033[0m \033[1;32;40mOK\033[0m'%(host,pubName))
	else:
		pexRun(host,cmdHome,passwd)
		cmd = 'find %s -name "servicesetting.properties"|xargs sed -i "/ComputerName/ s#CP01#%s#g"'\
		%(confDir,cpName)
		p.cmd_run(cmd)
		print('%s :upload \033[1;31;40m%s\033[0m \033[1;32;40mOK\033[0m'%(host,pubName))

#部署计数器
def PublicDeployRun():
	listinfo = t.findALLInfo()
	n = 0
	for i in listinfo:
		PublicDeploy(i)
		n += 1
		print '\033[1;33;40mcount:%s\033[0m' %n

#帮助参数配置
parser = OptionParser(add_help_option=0)
parser.add_option("-h", "--help", action="callback", callback=helpFunc)
parser.add_option("-M", "--module", action="store", type="string", dest="module",default="")
parser.add_option("-m", "--mid", action="store", type="string", dest="mid",default="")
parser.add_option("-i", "--ip", action="store", type="string", dest="ip",default="")
parser.add_option("-a", "--all", action="store_true", dest="all")
parser.add_option("-D", "--deploy", action="store_true", dest="deploy")
parser.add_option("-n", "--number", action="store", type="string", dest="number",default="")
(options, args) = parser.parse_args()
ip = options.ip.split(',')
mod = options.module.split(',')
mid=options.mid
allip = options.all
deploy = options.deploy
order=options.number.split(',')
commandoption=args

if __name__ == '__main__':
	if len(sys.argv) == 1:
		helpFunc('a','b','c','d')
	modulelist = []
	iplist = []
	if ip != ['']:
		check_Ip(ip)
	if mod != ['']:
		check_ModName(mod)
	if order != ['']:
		allip = True
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
	if mid != "":
		if mid != "head" and mid != "tail":
			print "\033[1;31;40mmid not correct,please check!\033[0m"
			sys.exit(3)
		else:
			allip = True
	if len(mod) != 1 and mid != "":
		print "\033[1;31;40mmid and several modules cannot use together,please modify!\033[0m"
		sys.exit(3)
	if ip != [''] and mid != "":
		print "\033[1;31;40mmid and ip cannot use together,please modify!\033[0m"
		sys.exit(3)
	if len(mod) != 1 and order != ['']:
		print "\033[1;31;40morder and several modules cannot use together,please modify!\033[0m"
		sys.exit(3)
	if order != [''] and mid != "":
		print "\033[1;31;40mmid and order number cannot use together,please modify!\033[0m"
		sys.exit(3)
	if order != [''] and ip != ['']:
		print "\033[1;31;40mip and order number cannot use together,please modify!\033[0m"
		sys.exit(3)

#判断模块名和ip地址是否合法
	if mod != [''] and ip != ['']:
		tmplist = []
		infolist = []
		for i in mod:
			for n in ip:
				tmplist.append(t.findIpModInfo(n,i))
		while [] in tmplist:
			tmplist.remove([])
		for i in tmplist:
			for n in i:
				infolist.append(n)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					PublicDeployUpdate(infolist[i])
					i = i+1
				print '\033[1;33;40mcount:%s\033[0m' %i
			elif mid == "tail":
				i = count
				while i < modlen:
					PublicDeployUpdate(infolist[i])
					i = i+1
				i = modlen-count
				print '\033[1;33;40mcount:%s\033[0m' %i
			else:		
				for i in infolist:
					PublicDeployUpdate(i)
				print '\033[1;33;40mcount:%s\033[0m' %modlen
		else:
			print('Error!please check db file!!')
#按照模块进行部署及更新
	elif mod != [''] and allip == True:
		orderStr = ""
		if order != ['']:
			orderStr = " and ("
			for n in order:
				orderStr = orderStr + "CPname='%s' or "%n
			orderStr = re.sub(r' or $',")",orderStr,0)
		tmplist = []
		infolist = []
		for i in mod:
			tmplist.append(t.findIPInfo(i,orderStr))
		for i in tmplist:
			for n in i:
				infolist.append(n)
		if infolist != []:
			modlen =  len(infolist)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					PublicDeployUpdate(infolist[i])
					i = i+1
				print '\033[1;33;40mcount:%s\033[0m' %i
			elif mid == "tail":
				i = count
				while i < modlen:
					PublicDeployUpdate(infolist[i])
					i = i+1
				print '\033[1;33;40mcount:%s\033[0m' %(modlen-count)
			else:		
				for i in infolist:
					PublicDeployUpdate(i)
				print '\033[1;33;40mcount:%s\033[0m' %modlen
		else:
			print('Error!please check db file!!')
#全量部署模块
	elif deploy:
		info = raw_input('Are you sure use this option(yes/no):')
		if info == 'yes':
			mkdirWebapp()
			PublicDeployRun()
		elif info == 'no':
			sys.exit(3)
		else:
			print 'Sorry,must choice yes or no.'
	else:
		print('syntax error!Please use -h for help!')

