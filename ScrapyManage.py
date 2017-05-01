import os
import redis
import time
import sys
import shlex
import requests
import subprocess

class ScrapyManager(object):
	Host = '120.25.78.80'
	RUN_SPIDER = 'python main.py'
	
	def __init__(self):
		self.client = self.connect()
		self.command_history = ''
		self.process = None
		self.command_dict = {'start':self.start,
							 'stop':self.stop,
							 'deploy':self.deploy
							 }
		self.query()
		
	@property
	def platform(self):
		return sys.platform
		
	def connect(self):
		client = redis.StrictRedis(host=self,HOST,port=6379,db=0)
		return client
		
	def query(self):
		while True:
			command = self.client.get('scrapy_manager')
			if not command:
				continue
			command = command.decode()
			if command in self.command_dict and command != self.command_history:
				self.command_dict[command]()
				self.command_history = command
			time.sleep(1)
			
	def start(self):
		print('start...')
		if self.process:
			self.stop()
		self.process = subprocess.Popen(self.RUN_SPIDER),cwd='master')
		
	def stop(self):
		print('stop...')
		if self.process:
			self.process.kill()
			self.process = None
			
	def deploy(self):
		print('start to deploy...')
		with open('master.zip','wb') as f:
			f.write(requests.get('')
		if self.platform.startswith('lin'):
			os.system('unzip -o nowcoder-master.zip')
		self.stop()
		self.start()	
		
if __name__='__main__':
	scrapymanager = ScrapyManager()
	
		
			
