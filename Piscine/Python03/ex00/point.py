class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

if __name__=="__main__":
	try:
		in1 = input('Insert the coordinates of the first point: ')
		in1 = in1.split(',', 1)
		a = Point(float(in1[0]), float(in1[1]))
		in2 = input('Insert the coordinates of the second point: ')
		in2 = in2.split(',', 1)
		b = Point(float(in2[0]), float(in2[1]))
		print('Their distance is: ', eval(f'(({a.x} - {b.x})**2 + ({a.y} - {b.y})**2)**0.5'))
	except ValueError:
		pass