from functions import *
from insertion import *
import sys, json, os, time 

def read_option(msp, msn):
	help_print()
	
	option = ""
	while True:
		sys.stderr.write("\x1b[2J\x1b[H")
		help_print()
		print "Please enter correct option"
		option = raw_input()
		option = option.lower()
		if option == 'c':
			insert_object(msp, msn)
		elif option == 'r':
			break
		elif option == 'u':
			print ""
		elif option == 'd':
			print ""
		elif option == 'q':
			print("Exitting...")
			time.sleep( .5 )
			break
		elif option == 'n':
			x = create_new_object_type()
		else:
			sys.stderr.write("\x1b[2J\x1b[H")
			print "Incorrect option. Hit enter and try again..."
			raw_input()


if len(sys.argv) < 3:
	print("Not enough run arguments. Exitting...")
	time.sleep( .5 )
main_server_path = prepare_path(sys.argv[1])
main_server_name = prepare_path(sys.argv[2])
set_path(main_server_path)
read_option(main_server_path, main_server_name)

# print len(sys.argv)
# print str(sys.argv[1])
