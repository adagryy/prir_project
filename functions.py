import sys,json,os,paramiko,threading,time
from pprint import pprint

path = ""

hostnames = []

results = []

object_name = ""

lock = threading.Lock()

class myThread(threading.Thread):
	def __init__(self, host):
		threading.Thread.__init__(self)
		self.host = host
	def run(self):
		search_for_duplicates(self.host)

def search_for_duplicates(host):
	global results
	myuser   = 'adam'
	mySSHK   = '/home/adam/.ssh/id_rsa.pub'
	sshcon   = paramiko.SSHClient()  # will create the object
	sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())# no known_hosts error
	sshcon.connect(host, username=myuser, key_filename=mySSHK) # no passwd needed
	i, o, e  = sshcon.exec_command('python /home/adam/Desktop/database/script.py ' + object_name)
	# print o.read()
	lock.acquire()
	results.append(o.read())
	lock.release()

def prepare_hosts(hosts):
	global hostnames
	hostnames = hosts

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

	threads = []


	sys.stderr.write("\x1b[2J\x1b[H")
	print "Enter new object name"
	global object_name
	global results

	del results[:]

	object_name = ""

	object_name = raw_input()

	for host in hostnames: # starting threads to search if there is a type of object in the database, ehich user has typed
		try:
		   t = myThread(host)
		   threads.append(t)
		   t.start()
		except:
		   print "Error: unable to start thread"

	for t in threads:
		t.join()

	# for r in results:
	# 	print r

	# raw_input()
	if "True" in results:
		print ("Duplicate type(s) found. Terminating...")
		time.sleep(1)
		return

	# raw_input("Done")

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
		# search_object[name] = datatype

	data = json.dumps(object_properties)
	# json_search_object = json.dumps(search_object)

	drs = os.listdir(path)

	for directory in drs:
		full_path = path
		full_path = path + directory
		search_object_path = full_path # <-------------------------

		# search_file = open(search_object_path + "/search.txt")
		# search_file.write(json_search_object)
		# search_file.close()

		text_file = open(full_path + "/" + object_name + ".txt", "w")
		text_file.write(data)
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