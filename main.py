from functions import *
from insertion import *
import sys, json, os, time 

def read_option():
	help_print()
	
	option = ""
	while True:
		sys.stderr.write("\x1b[2J\x1b[H")
		help_print()
		print "Please enter correct option"
		option = raw_input()
		option = option.lower()
		if option == 'c':
			insert_object()
		elif option == 'r':
			break
		elif option == 'u':
			print ""
		elif option == 'd':
			print ""
		elif option == 'e':
			print("Exitting...")
			time.sleep( 1 )
			break
		elif option == 'n':
			x = create_new_object_type()
		else:
			print ""

read_option()