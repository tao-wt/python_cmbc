#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'
import sqlite3

class SqliteClass(object):
	def __init__(self,dbname):
		self.dbname = dbname
		self.conn = sqlite3.connect(self.dbname)
		self.cur = self.conn.cursor()

	def query(self,sql):
		try:
			n=self.cur.execute(sql)
			return n
		except sqlite3.Error,e:
			print "sqlite Error:%s\nSQL:%s" %(e,sql)

	def queryRow(self,sql):
		self.query(sql)
		result = self.cur.fetchone()
		return result

	def queryAll(self,sql):
		self.query(sql)
		result = self.cur.fetchall()
		new_list =[]
		for inv in result:
			d = []
			for i in range(0,len(inv)):
				d.append(inv[i])
			new_list.append(d)
		return new_list

	def commit(self):
		self.conn.commit()

	def close(self):
		self.cur.close()
		self.conn.close()

