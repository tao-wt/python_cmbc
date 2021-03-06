#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'
from SqliteClass import *

class SQLClass(object):
	s = SqliteClass('../conf/tsck.db')

	def AllIpList(self):
		sql = "select distinct ip from module union select distinct ip from public\
union select ip from hadoop union select ip from redis\
union select ip from fastdfs union select ip from mysql; " 
		return self.s.queryAll(sql)

	def FindRoleIp(self,role):
		sql = "select distinct ip from %s;" %role
		return self.s.queryAll(sql)

	def findUserPass(self,user):
		sql = "select user,port,password from user where user = '%s'" %user
		return self.s.queryAll(sql)

	def FindTeatalkIp(self,mod):
		sql = "select distinct ip from module where modulename='%s';" %mod
		return self.s.queryAll(sql)

	def FindPubIp(self,mod):
		sql = "select distinct ip from public where modulename='%s';" %mod
		return self.s.queryAll(sql)

	def FindMod(self):
		sql = "select distinct modulename from module;"
		return self.s.queryAll(sql)

	def findIPByModName(self,modname):
		sql = "select distinct ip from module where modulename = '%s'\
union select distinct ip from public where publicname = '%s';" %(modname,modname)
		return self.s.queryAll(sql)

