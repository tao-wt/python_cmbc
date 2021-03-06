#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'
import paramiko
import os,datetime

class ParamikoClass(object):
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	def __init__(self,host,port,user,password):
		self.host = host
		self.port = port
		self.user = user
		self.password = password

	#执行命令函数
	def cmd_run(self,cmd):
		self.s.connect(self.host,self.port,self.user,self.password,timeout=1)
		stdin,stdout,stderr = self.s.exec_command(cmd)
		cmd_result = stdout.read(),stderr.read()
		self.s.close()


	def cmd_runhost(self,cmd):
		self.s.connect(self.host,self.port,self.user,self.password,timeout=1)
		stdin,stdout,stderr = self.s.exec_command(cmd)
		cmd_result = stdout.read(),stderr.read()
		print('\033[32;1m-------- %s\033[0m \033[31;1m%s\033[0m \033[32;1m--------\033[0m'%(self.host,cmd))
		for line in cmd_result:
			print line,
		self.s.close()
	return True


	def check_cmd(self,cmd):
		self.s.connect(self.host,self.port,self.user,self.password,timeout=1)
		stdin,stdout,stderr = self.s.exec_command(cmd)
		cmd_result = stdout.read(),stderr.read()
		for line in cmd_result:
			return line
		self.s.close()

	#分发文件函数
	def put_file(self,file_path,remote_path):
		file_name = os.path.basename(file_path)
		t = paramiko.Transport((self.host,self.port))
		t.connect(username=self.user,password=self.password)
		sftp = paramiko.SFTPClient.from_transport(t)
		sftp.put(file_path,'%s/%s' %(remote_path,file_name))
		print('\033[31;1msend %s\033[0m to \033[0m\033[32;1m%s\033[0m\033[32;1m %s sucesseful.\033[0m'%(file_name,self.host,remote_path))
		t.close()

	#未测试
	def get_file(self,remotepath,file_name,localpath):
		t = paramiko.Transport((self.host,self.port))
		t.connect(username=self.user,password=self.password)
		sftp = paramiko.SFTPClient.from_transport(t)
		sftp.get('%s/%s'%(remotepath,file_name),'%s/%s'%(localpath,file_name))
		t.close()

	#
	def upload(self,local_dir,remote_dir):
		tmp_list = remote_dir.split('/')
		dir_name = tmp_list[-2]
		try:
			t=paramiko.Transport((self.host,self.port))
			t.connect(username=self.user,password=self.password)
			sftp=paramiko.SFTPClient.from_transport(t)
			#sftp.remove("%s"%remote_dir)
			#sftp.mkdir("%s"%remote_dir)
			#print('=============== %s upload %s ==============='%(self.host,dir_name))
			#print 'upload file start %s ' % datetime.datetime.now()
			for root,dirs,files in os.walk(local_dir):
				for filespath in files:
					local_file = os.path.join(root,filespath)
					a = local_file.replace(local_dir,'')
					remote_file = os.path.join(remote_dir,a)
					try:
						sftp.put(local_file,remote_file)
					except Exception,e:
						sftp.mkdir(os.path.split(remote_file)[0])
						sftp.put(local_file,remote_file)
					#print "upload %s to remote %s" % (local_file,remote_file)
				for name in dirs:
					local_path = os.path.join(root,name)
					a = local_path.replace(local_dir,'')
					remote_path = os.path.join(remote_dir,a)
					try:
						sftp.mkdir(remote_path)
						#print "mkdir path %s" % remote_path
					except Exception,e:
						#print e
						pass
			#print 'upload file success %s ' % datetime.datetime.now()
		   # print('\033[1;32;40m====== %s upload %s ===== OK\033[0m'%(self.host,dir_name))
			t.close()
		except Exception,e:
			print e

