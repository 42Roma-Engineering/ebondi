import sys

def ft_ext_pos():
	if (len(sys.argv) != 1):
		try:
			max = int(sys.argv[1])
			min = max
			max_pos = 1
			min_pos = 1
			i = 1
			while i < len(sys.argv):
				n = int(sys.argv[i])
				if n > max:
					max = n
					max_pos = i
				elif n < min:
					min = n
					min_pos = i
				i += 1
		except (IndexError, ValueError) as e:
			return
		min_pos -= 1
		max_pos -= 1
		print('The min is:', end=' ')
		print(min, end=' ')
		print('and its position is', end=' ')
		print(min_pos)
		print('The max is:', end=' ')
		print(max, end=' ')
		print('and its position is', end=' ')
		print(max_pos)
	else:
		print('Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>')

if __name__=="__main__":
	ft_ext_pos()