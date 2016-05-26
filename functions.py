import sys,json,os
from pprint import pprint
path = '/home/adam/Desktop/nfsy/'
object_name = ""
def help_print():
	print "C - INSERT new object \n" \
	"R - READ objects... \n" \
	"U - UPDATE objects... \n" \
	"D - DELETE objects... \n" \
	"e - exit database console\n" \
	"n - new object type"

def error_message():
	print "Incorect number typed"
	raw_input("Press Enter to continue...")

def create_new_object_type():
	i = -1
	c = 0
	while True:
		try:
			print "Enter the number of objects' attributes:"
			c = raw_input()
			c = int(c)
			if c < 0 or not isinstance( c, int ):
				error_message()
			else:
				i = c
				break
		except ValueError:
			error_message()
	print "Enter new object name"
	object_name = raw_input()
	object_properties = {}
	for x in range(i):
		print "Enter " + str(x) + "'th column name"
		name = raw_input()
		print "Enter datatype for this column"
		datatype = raw_input()
		object_properties[name] = datatype

	ss = json.dumps(object_properties)
	# # print ss
	# sd = json.loads(ss)
	# full_path = path + object_name + ".txt"


	drs = os.listdir(path)

	for directory in drs:
		full_path = path
		full_path = path + directory
		text_file = open(full_path + "/" + object_name + ".txt", "w")
		text_file.write(ss)
		text_file.close()
		os.mkdir(full_path + "/" + object_name)
		print directory
	# for key in sd:
	# 	print key + ": " + sd[key]
	# print sd["1"]
	return True