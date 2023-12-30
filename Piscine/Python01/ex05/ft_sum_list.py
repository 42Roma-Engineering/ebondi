
def sum_list(list = []):
	sum = 0
	for num in list:
		sum += num
	return sum

if __name__=="__main__":
	numbers = []
	try:
		n = int(input('Insert integer: '))
		while n != 0:
			numbers.append(n)
			n = int(input('Insert integer: '))
		print('The sum is:', end=' ')
		print(sum_list(numbers))
	except ValueError:
		pass
