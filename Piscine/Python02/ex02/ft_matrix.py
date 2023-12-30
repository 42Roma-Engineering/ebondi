import sys

def ft_matrix(rows, col): 
	try:
		rows = int(rows)
		col = int(col)
	except TypeError:
		return
	matrix = []
	for i in range(rows):
		a = []
		for j in range(col):
			print('Insert the element in position (', end='')
			print(i, end='')
			print(', ', end='')
			print(j, end='')
			print('): ',end='')
			try:
				a.append(float(input()))
			except ValueError:
				return
		matrix.append(a)
	print('The inserted matrix is:')
	sum_rows = []
	sum_col = [0]*col
	for i in range(rows):
		print(matrix[i])
		row_sum = 0
		for j in range(col):
			row_sum += matrix[i][j]
			sum_col[j] += matrix[i][j]
		sum_rows.append(row_sum)
	print('The sum over rows is:')
	print(sum_rows)
	print('The sum over columns is:')
	print(sum_col)



if __name__=="__main__":
	if len(sys.argv) == 3:
		ft_matrix(sys.argv[1] , sys.argv[2])
	else:
		print('Error! Usage: python3 ft_matrix.py <n> <m>')