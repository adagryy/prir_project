import os, sys, json

def insert_object():
	path, dirs, files = os.walk("/home/adam/Desktop/nfsy/db1").next()
	sys.stderr.write("\x1b[2J\x1b[H")
	i = 1
	for x in dirs:
		print str(i) + " " + x
		i += 1
	print "Please select, what type of object you want to insert to database:"
	number = int(raw_input())
	with open("/home/adam/Desktop/nfsy/db1/" + dirs[number - 1] + ".txt") as json_file:
	    json_data = json.load(json_file)
	for key in json_data:
		print key + ": " + json_data[key]
	raw_input("Press enter...")










# basepath = '/home/adam/Desktop/nfsy/db1'
# for fname in os.listdir(basepath):
#     path = os.path.join(basepath, fname)
#     if not os.path.isdir(path):
#         print fname
        

