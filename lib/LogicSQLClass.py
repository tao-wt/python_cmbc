#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'
from SqliteClass import *

class SQLClass(object):
    s = SqliteClass('../conf/tsck.db')

    def sendFileInfo(self):
        sql = 'select ip,modulename,path,CPname from module;'
        return self.s.queryAll(sql)

    def findIpModInfo(self,ip,modname):
        sql = "select ip,modulename,path,CPname from module \
        where ip = '%s' and modulename = '%s';" %(ip,modname)
        return self.s.queryAll(sql)

    #def findIPInfo(self,modname):
    #    sql = "select ip,modulename,path,CPname from module where modulename = '%s'" %modname
    #    return self.s.queryAll(sql)

    def findIPInfo(self,modname,cpname):
        sql = "select ip,modulename,path,CPname from module where modulename = '%s'%s" %(modname,cpname)
        return self.s.queryAll(sql)

    def findUserPass(self,user):
        sql = "select user,port,password from user where user = '%s'" %user
        return self.s.queryAll(sql)

    def findHosts(self):
        sql = "select distinct ip from module;"
        return self.s.queryAll(sql)

    def findipConfPath(self,host):
        sql = "select path from module where ip = '%s' and modulename = 'configcenter'" %host
        return self.s.queryAll(sql)

    def findipOtherPath(self,host):
        sql = "select path from module where ip = '%s' and modulename != 'configcenter'" %host
        return self.s.queryAll(sql)
    
    #sainter_add_start
    def findModuleInfo(self):
        sql = "select ip,port,path from module;"
        return self.s.queryAll(sql)

    def findIPByModName(self,modname):
        sql = "select distinct ip from module where modulename = '%s';" %modname
        return self.s.queryAll(sql)

    def findModByModName(self,modname,cpname):
        sql = "select ip,port,path,CPname from module where modulename = '%s'%s;" %(modname,cpname)
        return self.s.queryAll(sql)

    #def findModByModCpName(self,modname,cpname):
    #    sql = "select ip,port,path from module where modulename = '%s' and CPname = '%s';" %(modname,cpname)
    #    return self.s.queryAll(sql)

    def findModByIP(self,host):
        sql = "select ip,port,path,CPname from module where ip = '%s';" %host
        return self.s.queryAll(sql)

    def findModByModAndIP(self,host,modname):
        sql = "select ip,port,path,CPname from module where ip = '%s' and modulename = '%s';" %(host,modname)
        return self.s.queryAll(sql)
    #sainter_add_end

    def findModName(self):
        sql = "select distinct modulename from module;"
        return self.s.queryAll(sql)

    #def QTfindIp(self,mod):
    #    sql = "select ip,path from module where modulename = '%s'" %mod
    #    return self.s.queryAll(sql)
    def QTfindIp(self,mod,cpname):
        sql = "select ip,path from module where modulename = '%s'%s" %(mod,cpname)
        return self.s.queryAll(sql)
    def QTfindPath(self,mod,ip):
        sql = "select ip,path from module where ip = '%s' and modulename = '%s'" %(ip,mod)
        return self.s.queryAll(sql)

    def findHostsName(self):
        sql = "select distinct ip,hostname from module;"
        return self.s.queryAll(sql)

    def onlyFindHostsName(self,ip):
        sql = "select distinct hostname from module where ip = '%s';"%ip
        return self.s.queryAll(sql)
		
    def FindAllIpPath(self):
        sql = "select ip,path from module order by ip ASC;"
        return self.s.queryAll(sql)

