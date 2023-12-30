def ft_abs():
	try:
		r = eval(input('Insert an expression: '))
	except (NameError) as e:
		return
	if (r < 0):
		r *= -1
	print('The result is:', end=' ')
	print(r)

if __name__=="__main__":
	ft_abs()