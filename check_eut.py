#!/usr/bin/env python
# encoding:utf-8
__author__ = 'sainter'
import syssys.path.append("..")
from lib.LogicSQLClass import *
from lib.ParamikoClass import *
import subprocessimport multiprocessing
from optparse import OptionParser
t = SQLClass()
useUser = 'zhuser'
userInfo = t.findUserPass(useUser)
for i in userInfo: 
	user = i[0] 
	port = i[1] 
	passwd = i[2]
def helpFunc(a,b,c,d): 
	print "USAGE:" 
	print "EXAMPLE: '\033[1;33;40mpython %s -i IpAddr -M ModuleName\033[0m' or '\033[1;33;40mpython %s -a -s\033[0m'" %(sys.argv[0],sys.argv[0]) print "
	-h or --help for help." print "
	-M or --module for modulename,can use ',' example:\033[1;33;40m python %s -M acp,cmp,nav\033[0m" %sys.argv[0] print "
	-m or --mid for mid,can use ',' example:\033[1;33;40m python %s -m head/tail \033[0m" %sys.argv[0] print "
	-i or --ip for ip address,can use ',' example:\033[1;33;40m python %s -i 192.168.199.117,192.168.199.118\033[0m" %sys.argv[0] print "
	-a or --all for all module check',' example:\033[1;33;40m python %s -a\033[0m" %sys.argv[0] print "
	-s or --super yes or not check supervise,default:False. example:\033[1;33;40m python %s -a -s\033[0m" %sys.argv[0] sys.exit(3)def verFunc(a,b,c,d): 
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
mid=options.midip=options.ip.split(',')
all=options.allsuper=options.supercommand
option=args
def check_Ip(ip): 
	hosts = [] 
	hosts_ok = [] 
	iphost = t.findHosts() 
	for h in iphost:  
		hosts.append(str(h[0])) 
		ip = {}.fromkeys(ip).keys() 
		for i in ip:  if i not in hosts:   
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
			print "\033[1;31;40mModName %s not exist,please check!\033[0m" %mn   print 30*'*'   print "\033[1;33;40mInput Reference ModName:\033[0m"    for m in modnames:    print "\033[1;33;40m%s\033[0m" %m,   sys.exit(3)#def check_PingHost(ip):#    hosts = []#    for i in ip:#      if subprocess.call('ping -c2 -W 1 -i 0.2 %s > /dev/null' % i, shell=True) == 0 or subprocess.call('ping -c2 -W 1 -i 0.2 %s > /dev/null' % i, shell=True) == 0:#        #print '%s ping is: \033[32;1m OK \033[0m' % i#        i = ''.join(i)#        hosts.append(i)#      else:#        print '------\033[1;33;40m%s\033[0m \033[31;1mping not connect! \033[0m------' %i#    return hostsdef checkmoduleinfo(moduleinfo): host = moduleinfo[0] moduleport = moduleinfo[1] path = moduleinfo[2] modulerunname = path.split('/')[-1] p = ParamikoClass(host,port,user,passwd) ps = "ps -ef|grep %s.jar|grep -v supervise|grep -v grep > /dev/null && echo '1' || echo '0'" %(modulerunname) result_ps = p.check_cmd(ps).strip() ##add netstat portnumber = len(moduleport.split(";")) if portnumber == 2:  count = 0  for i in moduleport.split(";"):   cmd_netstat = "netstat -an|grep LISTEN|grep tcp|grep -w '%s'|wc -l" %(i)   result_netstat_count = int(p.check_cmd(cmd_netstat).strip())   count = count + result_netstat_count  if count == portnumber and result_ps == '1':   print "%s %s \033[1;32;40mstart OK\033[0m" %(host,modulerunname)  else:   print "%s %s \033[1;31;40mnot start\033[0m" %(host,modulerunname) elif portnumber == 1:  cmd_netstat = "netstat -an|grep LISTEN|grep tcp|grep -w '%s' > /dev/null && echo '1' || echo '0'" %(moduleport)  result_netstat = p.check_cmd(cmd_netstat).strip()  if result_netstat == '1' and result_ps == '1':   print "%s %s \033[1;32;40mstart OK\033[0m" %(host,modulerunname)  else:   print "%s %s \033[1;31;40mnot start\033[0m" %(host,modulerunname)def checkmoduleinfo_super(moduleinfo): host = moduleinfo[0] moduleport = moduleinfo[1] path = moduleinfo[2] modulerunname = path.split('/')[-1] p = ParamikoClass(host,port,user,passwd) ps = "ps -ef|grep %s.jar|grep -v supervise|grep -v grep > /dev/null && echo '1' || echo '0'" %(modulerunname) result_ps = p.check_cmd(ps).strip() super_ps = "ps -ef|grep supervise|grep %s|grep -v grep > /dev/null && echo '1' || echo '0'" %(modulerunname) result_super_ps = p.check_cmd(super_ps).strip() portnumber = len(moduleport.split(";")) if portnumber == 2:  count = 0  for i in moduleport.split(";"):   cmd_netstat = "netstat -an|grep LISTEN|grep tcp|grep -w '%s'|wc -l" %(i)   result_netstat_count = int(p.check_cmd(cmd_netstat).strip())   count = count + result_netstat_count  if count == portnumber and result_ps == '1' and result_super_ps == '1':   print "%s %s \033[1;32;40mprogram and supervise start OK\033[0m" %(host,modulerunname)  elif count == portnumber and result_ps == '1' and result_super_ps == '0':   print "%s %s \033[1;32;40mprogram start OK!\033[0m \033[1;31;40mbut supervise not OK\033[0m" %(host,modulerunname)  elif count == portnumber and result_ps == '0' and result_super_ps == '0':   print "%s %s \033[1;31;40mprogram and supervise not start!\033[0m" %(host,modulerunname)  elif count != portnumber and result_super_ps == '1':   print "%s %s \033[1;31;40mprogram no listen!\033[0m \033[1;32;40mbut supervise start OK!\033[0m" %(host,modulerunname)  else:   print "%s %s \033[1;31;40mprogram and supervise not start!\033[0m" %(host,modulerunname) elif portnumber == 1:  cmd_netstat = "netstat -an|grep LISTEN|grep tcp|grep -w '%s' > /dev/null && echo '1' || echo '0'" %(moduleport)  result_netstat = p.check_cmd(cmd_netstat).strip()  if result_netstat == '1' and result_ps == '1' and result_super_ps == '1':   print "%s %s \033[1;32;40mprogram and supervise start OK\033[0m" %(host,modulerunname)  elif result_netstat == '1' and result_ps == '1' and result_super_ps == '0':   print "%s %s \033[1;32;40mprogram start OK!\033[0m \033[1;31;40mbut supervise not OK\033[0m" %(host,modulerunname)  elif result_netstat == '1' and result_ps == '0' and result_super_ps == '0':   print "%s %s \033[1;31;40mprogram and supervise not start!\033[0m" %(host,modulerunname)  elif result_netstat == '0' and result_super_ps == '1':   print "%s %s \033[1;31;40mprogram no listen!\033[0m \033[1;32;40mbut supervise start OK!\033[0m" %(host,modulerunname)  else:   print "%s %s \033[1;31;40mprogram and supervise not start!\033[0m" %(host,modulerunname)def multipoolcess(moduleinfo): pool = multiprocessing.Pool(processes=8) modlen =  len(moduleinfo) count = modlen/2 linfo = modlen%2 if linfo != 0:  count = count+1 if mid == "head":  i = 0  while i < count:   pool.apply_async(checkmoduleinfo,(moduleinfo[i],))   i = i+1 elif mid == "tail":  i = count  while i < modlen:   pool.apply_async(checkmoduleinfo,(moduleinfo[i],))   i = i+1 else:    for i in moduleinfo:   pool.apply_async(checkmoduleinfo,(i,)) pool.close() pool.join()def multipoolcess_super(moduleinfo): pool = multiprocessing.Pool(processes=8) modlen =  len(moduleinfo) count = modlen/2 linfo = modlen%2 if linfo != 0:  count = count+1 if mid == "head":  i = 0  while i < count:   pool.apply_async(checkmoduleinfo_super,(moduleinfo[i],))   i = i+1 elif mid == "tail":  i = count  while i < modlen:   pool.apply_async(checkmoduleinfo_super,(moduleinfo[i],))   i = i+1 else:    for i in moduleinfo:   pool.apply_async(checkmoduleinfo_super,(i,)) pool.close() pool.join()#检查参数:ip,mod,mid是否合法兼容if ip != ['']: check_Ip(ip)if mod != ['']: check_ModName(mod)if mid != "": if mid != "head" and mid != "tail":  print "\033[1;31;40mmid not correct,please check!\033[0m"  sys.exit(3)if len(mod) != 1 and mid != "": print "\033[1;31;40mmid and several modules cannot use together,please modify!\033[0m" sys.exit(3)if ip != [''] and mid != "": print "\033[1;31;40mmid and ip cannot use together,please modify!\033[0m" sys.exit(3)tmplist = []moduleinfo = []iplist = []def moduleappend(): for i in tmplist:  for n in i:   moduleinfo.append(n)#ip_checkif ip != [''] and mod == [''] and super == False: for i in ip:  tmplist.append(t.findModByIP(i)) moduleappend() multipoolcess(moduleinfo)#ip_check_superviseelif ip != [''] and mod == [''] and super == True: for i in ip:  tmplist.append(t.findModByIP(i)) moduleappend() multipoolcess_super(moduleinfo)#mod_checkelif mod != [''] and ip == [''] and super == False: for m in mod:  tmplist.append(t.findModByModName(m)) moduleappend() multipoolcess(moduleinfo)#mod_check_superviseelif mod != [''] and ip == [''] and super == True: for m in mod:  tmplist.append(t.findModByModName(m)) moduleappend() multipoolcess_super(moduleinfo)##mod_and_ip_checkelif mod != [''] and ip != [''] and super == False: for i in ip:  for m in mod:   tmplist.append(t.findModByModAndIP(i,m)) moduleappend() multipoolcess(moduleinfo)##mod_and_ip_check_superviseelif mod != [''] and ip != [''] and super == True: for i in ip:  for m in mod:   tmplist.append(t.findModByModAndIP(i,m)) moduleappend() multipoolcess_super(moduleinfo)##check_allelif all == True and super == False: ip = t.findHosts() for i in ip:  iplist.append(str(i[0])) for i in iplist:  tmplist.append(t.findModByIP(i)) moduleappend() multipoolcess(moduleinfo)##check_all_superviseelif all == True and super == True: ip = t.findHosts() for i in ip:  iplist.append(str(i[0])) for i in iplist:  tmplist.append(t.findModByIP(i)) moduleappend() multipoolcess_super(moduleinfo)else: print('\033[1;31;40mInput Error!!!please use -h for help!!!\033[0m')
