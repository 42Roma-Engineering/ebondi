import sys

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circle:
	def __init__(self, x_y, r):
		self.center = Point(x_y[0], x_y[1])
		self.radius = r

	def __str__(self):
		return (f'Circle of center ({self.center.x}, {self.center.y}) and radius {self.radius}')
	
	def contains(self, point):
		dist = ((self.center.x - point.x)**2 + (self.center.y - point.y)**2)**0.5
		if (dist > self.radius):
			return False
		return True

def float_convert(string):
	try:
		if (string[0]):
			pass
	except TypeError:
		return string
	dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	i = 0
	n = 0
	sign = 1
	try:
		while string[i] == '-' or string[i] == '+':
			if string[i] == '-':
				sign *= -1
			i += 1
		while string[i]:
			n *= 10
			n += dict_var[string[i]]
			i += 1
			if string[i] == '.':
				i += 1
				div = 10
				while string[i]:
					n += dict_var[string[i]] / div
					div *= 10
					i += 1
				break
	except IndexError:
		pass
	n *= sign
	return n

if __name__=="__main__":
	try:
		check_args = sys.argv[3]
	except IndexError:

		circle = Circle((0, 0), 1)
		
		try:
			point = Point(float_convert(sys.argv[1]), float_convert(sys.argv[2]))
			v_dict = {True:'in', False:'out of'}
			print(f'The Point ({point.x}, {point.y}) lies {v_dict[circle.contains(point)]} the Circle of center ({circle.center.x}, {circle.center.y}) and radius {circle.radius}')
		except (KeyError, IndexError):
			pass	