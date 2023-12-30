class Person:
	def __init__(self, first, last):
		self.first_name = first
		self.last_name = last

	def __str__(self):
		return self.first_name+' '+self.last_name
	

class Student(Person):
	def __init__(self, first, last, course = None):
		Person.__init__(self, first, last)
		self.course = course

	def __str__(self):
		if self.course == None:
			return self.first_name+' '+self.last_name+' is not registered to any course'
		else:
			return self.first_name+' '+self.last_name+' is registered to '+self.course

		
if __name__=="__main__":
	first_name = input('Insert first name:')
	last_name = input('Insert last name:')
	course = input('Are you a student? (y/n)')

	while course != 'y' and course != 'n':
		course = input('Please type "y" or "n": ')

	if course == 'y':
		course = input('Please insert your degree course: ')
		stud = Student(first_name, last_name, course)
		print(stud)
	elif course == 'n':
		pers = Person(first_name, last_name)
		print(pers)
