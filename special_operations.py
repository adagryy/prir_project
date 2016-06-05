import sys, os
import shutil
from functions import error_message

def print_special_menu(main_server_path, main_server_name):
	sys.stderr.write("\x1b[2J\x1b[H")
	while True:
		print "'DROP DATABASE' - drop whole database \n" \
		"'DROP OBJECT' - drop specific object \n" \
		" b - back to main menu \n" \
		"If you really really know, what are you doing, type whole formula now, confirm, and requested removal task will be executed"
		print ""
		option = raw_input("Now enter valid option:")
		if option == "DROP DATABASE":
			drop_database(main_server_path)
		elif option == "DROP OBJECT":
			drop_object(main_server_path, main_server_name)
		elif option == "b":
			return
		else: 
			sys.stderr.write("\x1b[2J\x1b[H")
			print "Incorrect option. Hit enter and try again..."
			raw_input()

def drop_object(main_server_path, main_server_name):
	print "Confirm, you want to drop database. Type this code and hit enter:"
	print "YeSDROBJ"

	code = raw_input()

	if code != "YeSDROBJ":
		print "Incorrect confirmation code. Interrupting..."
		raw_input("Press enter...")
		return
	dirs = os.walk(main_server_path).next()[1]
	objects = os.walk(main_server_name).next()[1]

	if len(objects) == 0:
		print "No objects in database. Hit enter to continue."
		raw_input()
		return

	while True:
		pass
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			i = 1
			for x in objects:
				print str(i) + " " + x
				i += 1
			print "Please select, what type of object you want to insert into database:"
			number = int(raw_input())
			if number < 1 or number > len(objects):
				error_message()
			else:
				break
		except ValueError:
			error_message()

	# print objects[number - 1]

	for directory in dirs:
		working_path = main_server_path + directory + "/" + objects[number - 1]
		config_file = main_server_path + directory + "/" + objects[number - 1] + ".txt"
		shutil.rmtree(working_path, ignore_errors=True)
		os.remove(config_file)
	raw_input("Object has been dropped. Hit enter to continue")
	return

def drop_database(main_server_path):
	print "Confirm, you want to drop database. Type this code and hit enter:"
	print "YeSDRDB"

	code = raw_input()

	if code != "YeSDRDB":
		print "Incorrect confirmation code. Interrupting..."
		raw_input("Press enter...")
		return

	dirs = os.walk(main_server_path).next()[1]	# list of all mounted servers
	
	for directory in dirs:
		working_path = main_server_path + directory + "/"
		objects = os. walk(working_path).next()[1]
		files = os.walk(working_path).next()[2]
		for obj in objects:
			shutil.rmtree(working_path + obj + "/", ignore_errors=True)
			# print working_path + obj + "/"
		for f in files:
			if f == "script.py":
				continue
			os.remove(working_path + f)
			# print working_path + f
	raw_input("Database has been dropped. Hit enter to continue")
	return