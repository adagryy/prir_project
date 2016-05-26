from functions import help_print
import sys

def read_option():
	help_print()
	print "Please enter correct option"
	option = ""
	while True:
		option = sys.stdin.read(1)
		option = option.lower()
		if option == 'c':

			break
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

read_option()