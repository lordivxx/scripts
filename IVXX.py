#!/usr/bin/python
import textwrap

#authon = False
authon = True



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

	def send_output(self,data):
		self.output = data
		print self.output

	def ask_pass(self,thepass):
		if x.get_user_input("Enter the Passphrase: ") == thepass:
			return True
		else:
			return False
	def count_out_loud(self):
		for i in range(int(x.get_user_input("What is the first number? ")), int(x.get_user_input("What is the last number? ")) + 1):
			print i
	def menu(self):
		print textwrap.dedent("""\
		### Menu ###
		1. Count Out Loud
		2. Ask Pass
		3. Greet
		4. Quit
		############
		""")
		choice = x.get_user_input("Where to Sir: ")
		if choice == "1":
			x.count_out_loud()
		elif choice == "2":
			if x.ask_pass("test") == True:
				print "You Pass!" 
			else:
				print "Incorrect Sir!! I bid you Good Day!"
		elif choice == "3":
			x.greet()
		elif choice == "4":
			exit()	
		else:
			x.menu()


	def authcheck(self):
		if authon == True:
		        if x.ask_pass("test") == True:
                		pass
        		else:
                		raise RuntimeError('Failed Auth')

	 

x=IVXX('chuck')
x.authcheck()
x.menu()
