#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'
import sys
sys.path.append("..")
from lib.LogicSQLClass import *
from lib.ParamikoClass import *
from optparse import OptionParser
import multiprocessing
import re,time

t = SQLClass()
#申明使用哪个用户操作远程设备
useUser = 'zhuser'
appSourcePath = '/home/zhuser/innerapp'
processNum=10
userInfo = t.findUserPass(useUser)
for i in userInfo:
	user = i[0]
	port = i[1]
	passwd = i[2]

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

#创建程序目录
def mkWebappDir(host):
	p = ParamikoClass(host,port,user,passwd)
	p.cmd_run('mkdir -p /opt/innerapp')

def mkSupDir(host):
	p = ParamikoClass(host,port,user,passwd)
	p.cmd_run('mkdir -p /opt/supervise')

#帮助信息
def helpFunc(a,b,c,d):
	print "USAGE:"
	print "-h or --help for help."
	print "-M or --module for modulename,can use ',' example:acp,cmp,nav."
	print "-i or --ip for ip address,can use ',' example:192.168.199.11,10.10.10.10."
	print "-a or --all for all ip address,list of db."
	print "-D or --deployapp for deploy all app,use this option must be careful!"
	print "-n or --number for CPname."
	print "EXAMPLE: 'python %s -i 10.10.10.10 -M acp'" %sys.argv[0]
	sys.exit(3)

#远程推送配置文件
def sendAndConf(infoList):
	host = infoList[0]
	mname = infoList[1]
	path = infoList[2]
	cpname = infoList[3]
	#tmp = path.split('/')
	filename = path.split('/')[-1]
	p = ParamikoClass(host,port,user,passwd)
	local_dir = '%s/%s/' %(appSourcePath,mname)
	remote_dir = '%s/' %path
	dircmd= "rm -rf %s%s*"%(remote_dir,mname)
	p.cmd_run(dircmd)
	p.upload(local_dir,remote_dir)
	if mname=="djob":
		cmd = "cd %s;sed -i '/ComputerName/ s#CP01#%s#g' servicesetting.properties;sed -i 's/^\(org.quartz.scheduler.instanceId:\).*/\\1instance_%s/' quartz.properties;mv %s.jar %s.jar;" %(path,cpname,path.split('_')[-1],mname,filename)
	elif mname=="live" or mname=="apigateway" or mname=="oauth" or mname=="servicecenter":
		cmd = "cd %s;sed -i 's/^\(server.port=\).*/\\1%s/g' application.properties;mv %s.jar %s.jar;"%(path,infoList[4],mname,filename)
	else:
		cmd = "cd %s;sed -i 's/^\(ComputerName=\).*/\\1%s/g' servicesetting.properties;mv %s.jar %s.jar;" %(path,cpname,mname,filename)
	p.cmd_run(cmd)
	print('%s :upload %s \033[1;32;40mOK\033[0m'%(host,filename))

def mkdirWebapp():
	pool = multiprocessing.Pool(processes=processNum)
	hostlist = t.findHosts()
	for i in hostlist:
		pool.apply_async(mkWebappDir,(i[0],))
	pool.close()
	pool.join()

#部署模块
def deployRun():
	pool = multiprocessing.Pool(processes=processNum)
	listinfo = t.sendFileInfo()
	for i in listinfo:
		pool.apply_async(sendAndConf,(i,))
	pool.close()
	pool.join()

#申明帮助参数属性
parser = OptionParser(add_help_option=0)
parser.add_option("-h", "--help", action="callback", callback=helpFunc)
parser.add_option("-M", "--module", action="store", type="string", dest="module",default="")
parser.add_option("-m", "--mid", action="store", type="string", dest="mid",default="")
parser.add_option("-i", "--ip", action="store", type="string", dest="ip",default="")
parser.add_option("-a", "--all", action="store_true", dest="all")
parser.add_option("-D", "--deployapp", action="store_true", dest="deployapp")
parser.add_option("-n", "--number", action="store", type="string", dest="number",default="")
parser.add_option("-C", "--changefile", action="store", type="string", dest="cfilename",default="")
parser.add_option("-R", "--runcmd", action="store", type="string", dest="runcmd",default="")
(options, args) = parser.parse_args()
ip = options.ip.split(',')
mod = options.module.split(',')
mid=options.mid
allip = options.all
deployapp = options.deployapp
order=options.number.split(',')
cfilename = options.cfilename
runcmd = options.runcmd
commandoption=args

def multipoolcess(infolist):
	pool = multiprocessing.Pool(processes=processNum)
	for i in infolist:
		pool.apply_async(sendAndConf,(i,))
	pool.close()
	pool.join()

def moduleappend(list):
	newList = []
	for i in list:
		for n in i:
			newList.append(n)
	return newList
	
if __name__ == '__main__':
	if len(sys.argv) == 1:
		helpFunc('a','b','c','d')
	#获取模块列表和ip列表
	modulelist = []
	iplist = []
	tmp = t.findModName()
	for i in tmp:
		modulelist.append(str(i[0]))
	tmp = t.findHosts()
	for i in tmp:
		iplist.append(str(i[0]))
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
	if len(mod) != 1 and order != ['']:
		print "\033[1;31;40morder and several modules cannot use together,please modify!\033[0m"
		sys.exit(3)
	# if len(mod) != 1 and mid != "":
		# print "\033[1;31;40mmid and several modules cannot use together,please modify!\033[0m"
		# sys.exit(3)
	if ip != [''] and mid != "":
		print "\033[1;31;40mmid and ip cannot use together,please modify!\033[0m"
		sys.exit(3)
	if order != [''] and mid != "":
		print "\033[1;31;40mmid and order number cannot use together,please modify!\033[0m"
		sys.exit(3)
	if order != [''] and ip != ['']:
		print "\033[1;31;40mip and order number cannot use together,please modify!\033[0m"
		sys.exit(3)
	
#判断输入的ip及模块名称是否合法，是否存在在配置文件中。
	if mod != [''] and ip != ['']:
		tmplist = []
		infolist = []
		for i in mod:
			for n in ip:
				tmplist.append(t.findIpModInfo(n,i))
		while [] in tmplist:
			tmplist.remove([])
		infolist = moduleappend(tmplist)
		if infolist != []:
			multipoolcess(infolist)
		else:
			print('Error!please check db file!!')
#对模块进行批量部署，更新模块也是这一判断
	elif mod != [''] and allip == True:
		orderStr = ""
		if order != ['']:
			orderStr = " and ("
			for n in order:
				orderStr = orderStr + "CPname='%s' or "%n
			orderStr = re.sub(r' or $',"",orderStr,0) + ")"
		tmplist = []
		infolist = []
		for i in mod:
			getList = []
			getList.append(t.findIPInfo(i,orderStr))
			list = moduleappend(getList)
			modlen =  len(list)
			count = modlen/2
			linfo = modlen%2
			if linfo != 0:
				count = count+1
			if mid == "head":
				i = 0
				while i < count:
					infolist.append(list[i])
					i = i+1
			elif mid == "tail":
				i = count
				while i < modlen:
					infolist.append(list[i])
					i = i+1
			else:
				for i in list:
					infolist.append(i)
		if infolist != []:
			multipoolcess(infolist)
		else:
			print('Error!please check db file!!')
	elif cfilename:
		slen = cfilename.find("->",0,len(cfilename))
		if slen == -1:
			AllIpPath=t.FindAllIpPath()
			theIp=AllIpPath[1][1]
			Cp = ParamikoClass(theIp,port,user,passwd)
			for i in AllIpPath:
				if theIp != i[0]:
					print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
					theIp = i[0]
					Cp = ParamikoClass(theIp,port,user,passwd)
				Cp.put_file(cfilename,i[1])
		else:
			fileName = cfilename[0:slen]
			dstpath = cfilename[slen+2:len(cfilename)]
			aIp = t.findHosts()
			for i in aIp:
				Cp = ParamikoClass(i[0],port,user,passwd)
				Cp.put_file(fileName,dstpath)
	elif runcmd:
		aIp = t.findHosts()
		for i in aIp:
			Cp = ParamikoClass(i[0],port,user,passwd)
			Cp.cmd_runhost(runcmd)
#部署所有模块
	elif deployapp:
		info = raw_input('Are you sure use this option(yes/no):')
		if info == 'yes':
			mkdirWebapp()
			deployRun()
		elif info == 'no':
			sys.exit(3)
		else:
			print 'Sorry,must choice yes or no.'
	else:
		print('syntax error!Please use -h for help!')

