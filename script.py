import sys, os, json

# for arg in sys.argv[1:]:
# 	print arg

amount = len(sys.argv)

flag = False

basic_path = "/home/adam/Desktop/database/"

def create_dict():
	i = 2 # we are skipping some args in argv before exact json object arguments
	dictionary = {}
	while i <= (len(sys.argv) - 1):
		dictionary[sys.argv[i]] = sys.argv[i + 1]
		i += 2
	return dictionary

if amount == 2:
	print(os.path.exists(basic_path + sys.argv[1])) # during creating new type of object we are checking, if there already exists one or not
else:
	path = basic_path +  sys.argv[1]
	files = os.walk(path).next()[2]
	for file in files:
		if file.find("_config_") != -1:
			continue
		else:
			compare_dict = create_dict()
			with open(path + "/" + file) as json_file:
				json_data = json.load(json_file)
			del json_data["id"]
			if compare_dict == json_data:
				flag = True
				break
	print flag