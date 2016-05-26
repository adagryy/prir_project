from functions import *
import sys, json, os

def read_option():
	help_print()
	
	option = ""
	while True:
		print "Please enter correct option"
		option = raw_input()
		option = option.lower()
		if option == 'c':
			x = create_new_object_type()
			# break
		elif option == 'r':

			break
		elif option == 'u':

			break
		elif option == 'd':

			break
		elif option == 'e':

			break
		elif option == 'n':

			break
		else:
			break;



# for dirname, dirnames, filenames in os.walk(path):
#     for subdirname in dirnames:
#     	print subdirname
read_option()
