from functions import error_message
import os, sys, json
import threading
import paramiko, time

hostnames = ['192.168.0.1', '192.168.0.2', '192.168.0.4']
# hostnames = ['192.168.0.4']
results = []
search_object = []

query = ""

lock = threading.Lock()

class myThread(threading.Thread):
	def __init__(self, host):
		threading.Thread.__init__(self)
		self.host = host
		# self.name = name
		# self.counter = counter
	def run(self):
		# print "Starting " + self.name
		# print_time(self.name, self.counter, 5)
		search_for_duplicates(self.host)
		# print "Exiting " + self.name

def search_for_duplicates(host):
	global results
	myuser   = 'adam'
	mySSHK   = '/home/adam/.ssh/id_rsa.pub'
	sshcon   = paramiko.SSHClient()  # will create the object
	sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())# no known_hosts error
	sshcon.connect(host, username=myuser, key_filename=mySSHK) # no passwd needed
	i, o, e  = sshcon.exec_command('python /home/adam/Desktop/database/script.py ' + query)
	print 'python /home/adam/Desktop/database/script.py ' + query
	lock.acquire()
	results.append(o.read())
	lock.release()

def insert_object(main_path_of_all_servers, main_server):
	global query

	query = ""

	global results

	del results[:]

	global search_object

	del search_object[:]

	object_contents = {}

	threads = []



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
	# print server
	fline=open(main_server + dirs[number - 1] + "/_config_" + dirs[number - 1] + "_config_.txt").readline().rstrip()


	query += dirs[number - 1] + " "
	# print fline
	# print server
	intfline = int(fline)

	

	object_contents["id"] = fline

	global search_object

	for key in json_data:
		print "Please enter '" + key +"':"
		object_contents[key] = raw_input()
		if key == "id":
			continue
		search_object.append(key)
		search_object.append(object_contents[key])

	create_query_string(search_object)

	#MMMMMMMMMMMMMMMMMMMMMMMMMMMMM
	global hostnames

	for host in hostnames:
		try:
		   t = myThread(host)
		   threads.append(t)
		   t.start()
		except:
		   print "Error: unable to start thread"


	for t in threads:
		t.join()

	global results
	
	for r in results:
		print r

	raw_input("Done!")
	#MMMMMMMMMMMMMMMMMMMMMMMMMMMMM

	exact_object = json.dumps(object_contents)

	text_file = open(server + "_" + dirs[number - 1].lower() + "_" + fline + ".txt", "w")
	text_file.write(exact_object)
	text_file.close()

	text_file = open(main_server + dirs[number - 1] + "/_config_" + dirs[number - 1] + "_config_.txt", "w")
	text_file.write(str(intfline + 1))
	text_file.close()
	raw_input("Object saved to database. Press enter...")
	return

def create_query_string(s):
	global query 
	# query += " "
	for sstr in s:
		query += sstr + " "
	return query

def find_optimal_server(server_path, object_name):
	dirs = os.walk(server_path).next()[1]
	wanted_server = ""
	minimum = -1
	for directory in dirs:
		if directory == "db":
			continue
		path = server_path + "" + directory + "/" + object_name # <-- BUG CAN BE HERE path = server_path + "/" + directory + "/" + object_name
		files = os.walk(path).next()[2]
		files_amount = len(files)
		if minimum == -1:
			minimum = files_amount
			wanted_server = path
		elif files_amount < minimum:
			wanted_server = path
	return wanted_server + "/"
