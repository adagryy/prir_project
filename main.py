from functions import *
from insertion import *
from RUD_operations import *
from special_operations import *
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
			read_data(main_server_path, main_server_name)
		elif option == 'u':
			update_object(main_server_path, main_server_name)
		elif option == 'd':
			delete_objects(main_server_path, main_server_name)
		elif option == 'n':
			x = create_new_object_type()
		elif option == 'q':
			print("Exitting...")
			time.sleep( .1 )
			break
		elif option == 'xx':
			print_special_menu(main_server_path, main_server_name)
		else:
			sys.stderr.write("\x1b[2J\x1b[H")
			print "Incorrect option. Hit enter and try again..."
			raw_input()


if len(sys.argv) < 3:
	print("Not enough run arguments. Exitting...")
	time.sleep( .5 )
else:
	main_server_path = prepare_path(sys.argv[1])
	main_server_name = prepare_path(sys.argv[2])
	set_path(main_server_path)
	read_option(main_server_path, main_server_name)

# print len(sys.argv)
# print str(sys.argv[1])
