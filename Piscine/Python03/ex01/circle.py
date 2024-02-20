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

if __name__=="__main__":
	circle = Circle((150, 100), 75)
	print(circle)