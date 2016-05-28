from functions import error_message
import os, sys, json

def insert_object(main_path_of_all_servers, main_server):
	object_contents = {}

	dirs = os.walk(main_server).next()[1]

	if len(dirs) == 0:
		print "Warning. You have to specify the object structure. Press 'h' for help"
		raw_input()
		return

	while True:
		pass
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			i = 1
			for x in dirs:
				print str(i) + " " + x
				i += 1
			print "Please select, what type of object you want to insert into database:"
			number = int(raw_input())
			if number < 1 or number > len(dirs):
				error_message()
			else:
				break
		except ValueError:
			error_message()
	with open(main_server + dirs[number - 1] + ".txt") as json_file:
		json_data = json.load(json_file)
	server = find_optimal_server(main_path_of_all_servers, dirs[number - 1])
	fline=open(main_server + dirs[number - 1] + "/_config_" + dirs[number - 1] + "_config_.txt").readline().rstrip()

	print fline
	print server
	intfline = int(fline)

	object_contents["id"] = fline
	for key in json_data:
		print "Please enter '" + key +"':"
		object_contents[key] = raw_input()

	exact_object = json.dumps(object_contents)

	text_file = open(server + "_" + dirs[number - 1].lower() + "_" + fline + ".txt", "w")
	text_file.write(exact_object)
	text_file.close()

	text_file = open(main_server + dirs[number - 1] + "/_config_" + dirs[number - 1] + "_config_.txt", "w")
	text_file.write(str(intfline + 1))
	text_file.close()
	raw_input("Object saved to database. Press enter...")
	return

def find_optimal_server(server_path, object_name):
	dirs = os.walk(server_path).next()[1]
	wanted_server = ""
	minimum = -1
	for directory in dirs:
		path = server_path + "/" + directory + "/" + object_name
		files = os.walk(path).next()[2]
		files_amount = len(files)
		if minimum == -1:
			minimum = files_amount
			wanted_server = path
		elif files_amount < minimum:
			wanted_server = path
	return wanted_server + "/"
