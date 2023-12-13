import sys

def ft_sorted(args):
	list = []
	try:
		for arg in args[1:]:
			list.append(int(arg))
	except ValueError:
		return
	ordered = sorted(list, reverse=True)
	if list == ordered:
		print('The inserted sequence is sorted!')
	else:
		print('The inserted sequence is not sorted!')
		print('The correct order is ', end='')
		print(ordered)


if __name__=="__main__":
	if len(sys.argv) >= 3:
		ft_sorted(sys.argv)
	else:
		print('Error! You must insert at least 2 numbers')