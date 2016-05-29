import sys, os, json
from functions import error_message
# from __future__ import print_function

def update_object(main_server_path, main_server_name):
	sys.stderr.write("\x1b[2J\x1b[H")
	dirs = os.walk(main_server_path).next()[1]
	flag = False

	object_types = os.walk(main_server_name).next()[1]

	while True: # this loop fetches number of option from user. The option is which type of object is to be updated. Loop is built for 
		pass # infinte checking, when user type incorrect option (infinite quering user for correct option [while True:])
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			i = 1
			for ot in object_types:
				print str(i) + " " + ot
				i += 1
			print "Please select, what type of object you want to update in the database:"
			number = int(raw_input())
			if number < 1 or number > len(object_types):
				error_message()
			else:
				break
		except ValueError:
			error_message()

	configs = main_server_name + object_types[number - 1] + ".txt"

	with open(configs) as json_file:
		json_data = json.load(json_file)

	access_keys = ["" for x in range (len(json_data))]
	a = -1	
	a = count_objects(object_types[number - 1], main_server_path)
	data_for_change = ["" for y in range (a)]
	specified_value = -1
	item = ""

	while True: # this loop is similar to previous one - fetches number of attribute to be updated
		pass
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			i = 1
			for j in json_data:
				print str(i) + ". " + j + " --> " + json_data[j]
				access_keys[i - 1] = j
				i += 1
			print "Please select, which attribute you want to update in the database:"
			number_2 = int(raw_input())
			if number_2 < 1 or number_2 > len(json_data):
				error_message()
			else:
				access_key = access_keys[number_2 - 1]
				break
		except ValueError:
			error_message()

	# 
	# print access_keys[number_2 - 1]
	
	i = 1
	for directory in dirs:
		working_path = main_server_path + directory + "/" + object_types[number - 1] + "/"
		files = os.walk(working_path).next()[2]

		for file in files:
			if file.find("_config_") != -1:
				continue
			with open(working_path + file) as json_file:
				json_data = json.load(json_file)
			print str(i) + ". " + json_data[access_keys[number_2 - 1]]
			data_for_change[i - 1] = json_data[access_keys[number_2 - 1]]
			i += 1
	# print len(access_keys)
	while True: # fetches for specific attribute value (it determines specific value from database set (for instance specific surname from People set) )
		pass
		try:
			if flag == True:
				surname_index = 1
				for surname in data_for_change:
					print str(surname_index) + ". " + surname
					surname_index += 1
			flag = True
			print "Type, which " + access_keys[number_2 - 1] +"s should I have change?"
			specified_value = int(raw_input())
			if specified_value < 1 or specified_value > len(data_for_change):
				error_message()
			else:
				item = data_for_change[specified_value - 1]
				break
		except ValueError:
			error_message()

	print "Enter new " + access_keys[number_2 - 1]
	new_value = raw_input()

	# for xx in data_for_change:
	# 	print xx + "<-- access_keys"

	for directory in dirs:
		working_path = main_server_path + directory + "/" + object_types[number - 1] + "/"
		files = os.walk(working_path).next()[2]

		for file in files:
			if file.find("_config_") != -1:
				continue
			with open(working_path + file) as json_file:
				json_data = json.load(json_file)
			if item == json_data[access_keys[number_2 - 1]]:
				json_data[access_keys[number_2 - 1]] = new_value
				# print json_data[access_keys[number_2 - 1]]
				text_file = open(working_path + file, "w")
				text_file.write(json.dumps(json_data))
				text_file.close()
	raw_input("Press enter to continue...")
	return

def read_data(main_server_path, main_server_name):
	sys.stderr.write("\x1b[2J\x1b[H")
	dirs = os.walk(main_server_path).next()[1]	# list of all mounted servers

	object_types = os.walk(main_server_name).next()[1] 

	while True:
		pass
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			i = 1
			for ot in object_types:
				print str(i) + " " + ot
				i += 1
			print "Please select, what type of object you want to read from the database:"
			number = int(raw_input())
			if number < 1 or number > len(object_types):
				error_message()
			else:
				break
		except ValueError:
			error_message()

	# for directory in dirs:
	# 	files = main_server_path + directory + "/" + object_types[number - 1] + "/" # access path to database objects

	# 	print files

	configs = main_server_name + object_types[number - 1] + ".txt"
	with open(configs) as json_file:
		json_data = json.load(json_file)

	access_keys = ["" for x in range (len(json_data) + 1)]

	print ("Enter one of the following: ")
	access_key = ""
	while True:
		pass
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			i = 1
			for jd in json_data:
				print(str(i) + " - " + jd)
				access_keys[i - 1] = jd
				i += 1

			# access_keys[i - 1] = "id" - adds support for id searching <------------------------------
			print("a - list all")
			number_2 = raw_input()
			if number_2 == "a":
				list_all_objects(main_server_path, object_types[number - 1])
			else: 
				number_2 = int(number_2)
			if number_2 < 1 or number_2 > len(access_keys):
				error_message()
			else:
				access_key = access_keys[number_2 - 1] # <------------------------------------access_key = access_keys[number - 2]
				break
		except ValueError:
			error_message()

	print "Enter value you are searching in database: "
	item = raw_input()
	# for ir in access_keys:
	# 	print ir

	# print access_key

	for directory in dirs:
		working_path = main_server_path + directory + "/" + object_types[number - 1] + "/"
		files = os.walk(working_path).next()[2]
		for file in files:
			if file.find("_config_") != -1:
				continue
			with open(working_path + file) as json_filee:
				json_dataa = json.load(json_filee)
			# print json_dataa["id"]
			if item == json_dataa[access_key]:
				for jd2 in json_dataa:
					print jd2 + ": " + json_dataa[jd2]
	raw_input("Press enter to continue")

	return 

def delete_objects(main_server_path, main_server_name):
	sys.stderr.write("\x1b[2J\x1b[H")
	dirs = os.walk(main_server_path).next()[1]	# list of all mounted servers

	object_types = os.walk(main_server_name).next()[1] 

	while True:
		pass
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			i = 1
			for ot in object_types:
				print str(i) + " " + ot
				i += 1
			print "Please select, what type of object you want to delete from the database:"
			number = int(raw_input())
			if number < 1 or number > len(object_types):
				error_message()
			else:
				break
		except ValueError:
			error_message()
	# print object_types[number - 1]

	configs = main_server_name + object_types[number - 1] + ".txt"
	with open(configs) as json_file:
		json_data = json.load(json_file)

	access_keys = ["" for x in range (len(json_data) + 1)]
	
	print ("Enter one of the following: ")
	access_key = ""
	while True:
		pass
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			i = 1
			for jd in json_data:
				print(str(i) + " - " + jd)
				access_keys[i - 1] = jd
				i += 1
			number_2 = int(raw_input())
			if number_2 < 1 or number_2 > len(access_keys):
				error_message()
			else:
				access_key = access_keys[number_2 - 1]
				break
		except ValueError:
			error_message()

	print "Enter value you wish to delete from database: "
	item = raw_input()

	for directory in dirs:
		working_path = main_server_path + directory + "/" + object_types[number - 1] + "/"
		files = os.walk(working_path).next()[2]
		for file in files:
			if file.find("_config_") != -1:
				continue
			with open(working_path + file) as json_filee: # "working_path + file" - is path to a file (object). Two loops above allow (using this path) to iterate throuhg all objects of a type specified.
				json_dataa = json.load(json_filee)
			if item == json_dataa[access_key]:
				print file
				# os.remove(working_path + file)
	print access_keys
	print access_key

	raw_input("Object(s) deleted successfully. Press enter to continue")
	return

def count_objects(object_type, main_server_path):
	dirs = os.walk(main_server_path).next()[1]

	x = 0

	for directory in dirs:
		path_to_check = main_server_path + directory + "/" + object_type + "/"
		x += len(os.walk(path_to_check).next()[2])
		x -= 1 # skips one file in counting (config file)
	return x

def list_all_objects(main_server_path, object_type):
	dirs = os.walk(main_server_path).next()[1]	# list of all mounted servers

	for directory in dirs:
		working_path = main_server_path + directory + "/" + object_type + "/"
		files = os.walk(working_path).next()[2]
		for file in files:
			if file.find("_config_") != -1:
				continue
			# print working_path + file
			with open(working_path + file) as json_filee:
				json_dataa = json.load(json_filee)
			for jd in json_dataa:
				print jd + ": " + json_dataa[jd]
	raw_input("Listed")
	return