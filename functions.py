from main import read_option
def help_print():
	print "C - INSERT new object \n" \
	"R - READ objects... \n" \
	"U - UPDATE objects... \n" \
	"D - DELETE objects... \n" \
	"e - exit database console\n" \
	"n - new object type"

def error_message():
	print "Incorect number typed"

def create_new_object():
	i = -1
	print "Enter the number of objects' attributes:"
	while True:
		try:
			c = int(sys.stdin.read(1))
			if c < 0 || !isinstance( c, int ):
				error_message()
			else:
				i = c
				break:
		except ValueError:
			error_message()
	read_option()