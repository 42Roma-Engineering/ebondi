import sys

def trim(args):
	args[:] = args[1:-1]

if __name__=="__main__":
	if len(sys.argv) >= 3:
		args = sys.argv[1:]
		trim(args)
		print('The new list is: ', end='')
		print(args)
	else:
		print('Error! You must insert at least 2 values')