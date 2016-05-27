#!/usr/bin/python

class IVXX(object):
	number = 4.20
	def __init__(self,name):
		self.name = name 
		self.output = ""
		return 
	def get_user_input(self):
		input = raw_input("Enter the info: ") 
		return input
	def greet(self):
		print "Welcome " + self.name + " would you like to play a game "		
	def send_output(self,data):
		self.output = data
		print self.output
	def ask_pass(self,thepass):
		if x.get_user_input() == thepass:
			return True
		else:
			return False
	 

x=IVXX('chuck')
if x.ask_pass("test") == True:
	print "nice"

