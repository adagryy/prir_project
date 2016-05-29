import sys,json,os
from pprint import pprint

path = ""
# object_name = ""

def prepare_path(ppath):
	if ppath[len(ppath) - 1] != "/":
		ppath += "/"
	return ppath

def set_path(global_path):
	global path
	path = global_path

def help_print():
	print "C - INSERT new object \n" \
	"R - READ objects... \n" \
	"U - UPDATE objects... \n" \
	"D - DELETE objects... \n" \
	"q - exit database console\n" \
	"n - new object type \n" \
	"xx - expert mode. Managing database"

def error_message():
	sys.stderr.write("\x1b[2J\x1b[H")
	print "Incorect number typed"
	raw_input("Press Enter to continue...")

def create_new_object_type():
	i = -1
	c = 0
	sys.stderr.write("\x1b[2J\x1b[H")
	print "Enter new object name"
	object_name = raw_input()
	while True:
		try:
			sys.stderr.write("\x1b[2J\x1b[H")
			print "Enter the number of objects' attributes (columns):"
			c = raw_input()
			c = int(c)
			if c < 0 or not isinstance( c, int ):
				error_message()
			else:
				i = c
				break
		except ValueError:
			error_message()
	object_properties = {}
	for x in range(i):
		sys.stderr.write("\x1b[2J\x1b[H")
		print "Enter " + str(x + 1) + "'th column name"
		name = raw_input()
		sys.stderr.write("\x1b[2J\x1b[H")
		print "Enter datatype for this column"
		datatype = raw_input()
		object_properties[name] = datatype

	ss = json.dumps(object_properties)

	drs = os.listdir(path)

	for directory in drs:
		full_path = path
		full_path = path + directory
		text_file = open(full_path + "/" + object_name + ".txt", "w")
		text_file.write(ss)
		text_file.close()
		dir_name = full_path + "/" + object_name
		os.mkdir(dir_name)
		text_file = open(dir_name + "/_config_" + object_name + "_config_.txt", "w")
		text_file.write("1")
		text_file.close()
		# print directory
	# for key in sd:
	# 	print key + ": " + sd[key]
	# print sd["1"]
	return True