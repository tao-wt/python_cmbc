#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'
from SqliteClass import *

class SQLClass(object):
	s = SqliteClass('../conf/tsck.db')

	def findUserPass(self,user):
		sql = "select port,password from user where user='%s'" %user
		return self.s.queryAll(sql)

	def findAllHosts(self):
		sql = "select distinct ip from public"
		return self.s.queryAll(sql)

	def findALLInfo(self):
		sql = "select ip,publicname,publicpath,cpname from public"
		return self.s.queryAll(sql)

	def findAllPubName(self):
		sql = "select distinct publicname from public"
		return self.s.queryAll(sql)

	def findIpModInfo(self,ip,modname):
		sql = "select ip,publicname,publicpath,cpname from public " \
			  "where ip = '%s' and publicname = '%s'" %(ip,modname)
		return self.s.queryAll(sql)

	def findIPInfo(self,modname,cpname):
		sql = "select ip,publicname,publicpath,cpname from public where publicname = '%s'%s" %(modname,cpname)
		return self.s.queryAll(sql)

	def findPublicTable(self):
		sql = 'select * from public;'
		return self.s.queryAll(sql)

	def findHosts(self):
		sql='select distinct ip,hostname from public;'
		return self.s.queryAll(sql)

	def findModByIP(self,host):
		sql = "select ip,publicname,startcmd,port,CPname from PUBLIC where ip = '%s';" %host
		return self.s.queryAll(sql)

	def findModName(self):
		sql = "select distinct publicname from public;"
		return self.s.queryAll(sql)

	def findIPByModName(self,publicname):
		sql = "select distinct ip from public where publicname = '%s';" %publicname
		return self.s.queryAll(sql)

	def findModByModName(self,publicname,cpname):
		sql = "select ip,publicname,startcmd,port,CPname from public where publicname = '%s'%s;" %(publicname,cpname)
		return self.s.queryAll(sql)

	def findModByModAndIP(self,host,publicname):
		sql = "select ip,publicname,startcmd,port,CPname from public where ip = '%s' and publicname = '%s';" %(host,publicname)
		return self.s.queryAll(sql)

	def sendFileInfo(self):
		sql = 'select ip,modulename,path,CPname from module;'
		return self.s.queryAll(sql)

	def findAllIp(self):
		sql = 'select  distinct ip from public;'
		return self.s.queryAll(sql)

	def findIpcmd(self,ip):
		sql = "select ip,startcmd from public where ip = '%s';" %ip
		return self.s.queryAll(sql)

	def findIpname(self,ip):
		sql = "select ip,publicname from public where ip = '%s';" %ip
		return self.s.queryAll(sql)

	def findIpAndMod(self,ip,mod):
		sql = "select ip,startcmd from public where ip = '%s' and publicname = '%s';" %(ip,mod)
		return self.s.queryAll(sql)

	def findIpOnlyMod(self,mod,cpname):
		sql = "select ip,startcmd from public where publicname = '%s'%s;" %(mod,cpname)
		return self.s.queryAll(sql)

	def FindAllIpPath(self,modStr,orderStr):
		sql = "select ip,publicpath from public %s%s order by ip ASC;"%(modStr,orderStr)
		return self.s.queryAll(sql)

	def FindAllIpPathD(self,modStr,orderStr):
		sql = "select distinct ip from public %s%s order by ip ASC;" %(modStr,orderStr)
		return self.s.queryAll(sql)

