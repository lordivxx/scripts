#!/usr/bin/python
import textwrap
import sys
import subprocess

authon = False
#authon = True
weather_support = False

if weather_support == True:
	print "Weather Support has been turn off."	

class IVXX(object):

	number = 4.2

	def __init__(self,name):
		self.name = name 
		self.output = ""
		return 

	def get_user_input(self,question):
		input = raw_input(question) 
		return input

	def greet(self):
		print "\n" * 10
		print "Welcome " + self.name + " would you like to play a game? "		

	def report_speed(self):
		proc=subprocess.Popen('/home/pi/speedtest/Report_Speed_Test_Results.sh', shell=True, stdout=subprocess.PIPE, )
                p1=proc.communicate()[0]
                print p1
                return p1

	def send_output(self,data):
		self.output = data
		print self.output

	def ask_pass(self,thepass):
		if self.get_user_input("Enter the Passphrase: ") == thepass:
			return True
		else:
			return False

	def count_out_loud(self):
		for i in range(int(self.get_user_input("What is the first number? ")),int(self.get_user_input("What is the last number? ")) + 1):
			print i

	def run_bash_cmd(self,command):
		proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, )
		p1=proc.communicate()[0]
		print p1 
		return p1
		
	def get_weather(self):
		proc=subprocess.Popen('/usr/local/bin/weatherpy', shell=True, stdout=subprocess.PIPE, )
		p1=proc.communicate()[0]
		print p1 
		return p1
		
	def build_positional_argparse(self,input):
                import argparse

                parser = argparse.ArgumentParser()
                parser.add_argument(input, nargs='?', default="check_string_for_empty")
                args = parser.parse_args()
                return args.input
		

	def menu(self):
		print textwrap.dedent("""\
		### Menu ###
		1. Count Out Loud
		2. Ask Pass
		3. Greet
		4. Current Weather
		5. Show Recent Speed Test Results
		q. Quit
		############
		""")
		choice = self.get_user_input("Where to " + self.name + ": ")
		if choice == "1":
			self.count_out_loud()
		elif choice == "2":
			if self.ask_pass("test") == True:
				print "You Pass!" 
			else:
				print "Incorrect Sir!! I bid you Good Day!"
		elif choice == "3":
			self.greet()
		elif choice == "4":
			print "\n" * 20
			print "Gathering data now ..."
			print "\n" * 20
			self.get_weather()	
		elif choice == "5":
			self.report_speed()
		elif choice == "q":
			exit()	
		else:
			x.menu()


	def authcheck(self):
		if authon == True:
		        if self.ask_pass("test") == True:
                		pass
        		else:
                		raise RuntimeError('Failed Auth')

	 

