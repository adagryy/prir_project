import sys, os, json
from functions import error_message

def update_object(main_server_path, main_server_name):
	sys.stderr.write("\x1b[2J\x1b[H")
	dirs = os.walk(main_server_path).next()[1]

	object_types = os.walk(main_server_name).next()[1]
	# for directory in dirs:
	# i = 1

	# for ot in object_types:
	# 	print str(i) + ". " + ot
	# 	i += 1
	# print object_types
	while True:
		pass
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

	while True:
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
	while True:
		pass
		try:
			# surname_index = 1
			# for surname in data_for_change:
			# 	print str(surname_index) + ". " + surname
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

	# print item + "<-- item"
	# for xx in data_for_change:
	# 	print xx + "<-- dataforChange"
	for xx in data_for_change:
		print xx + "<-- access_keys"

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
				print json_data[access_keys[number_2 - 1]]
				text_file = open(working_path + file, "w")
				text_file.write(json.dumps(json_data))
				text_file.close()
	raw_input("Press enter to continue...")
	return

def count_objects(object_type, main_server_path):
	dirs = os.walk(main_server_path).next()[1]

	x = 0

	for directory in dirs:
		path_to_check = main_server_path + directory + "/" + object_type + "/"
		x += len(os.walk(path_to_check).next()[2])
		x -= 1
	print  "X wynosi:" + str(x)
	raw_input()
	return x