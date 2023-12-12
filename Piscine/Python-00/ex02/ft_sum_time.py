def converter(str):
	n = 0	
	for i in str:
		n *= 10
		n += dict_var[i]
	return n


dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

h = converter(input('Insert hours: '))
h = h * 60 * 60
m = converter(input('Insert minutes: '))
m *= 60
s = converter(input('Insert seconds: '))

print('Total seconds:', end=' ')
print (h+m+s)