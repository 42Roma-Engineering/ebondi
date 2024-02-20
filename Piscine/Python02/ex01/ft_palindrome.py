import sys

def is_palindrome(word): 
	word = word.replace(" ", "")
	try:
		size = len(word)
	except TypeError:
		return
	i = 0
	while i < size:
		if word[i] != word[(i * -1) -1]:
			return False
		i += 1
	return True

if __name__=="__main__":
	if len(sys.argv) == 2:
		if is_palindrome(sys.argv[1]) == True:
			print('The string ' + sys.argv[1] + ' is palindrome')
		else:
			print('The string ' + sys.argv[1] + ' is not palindrome')
	else:
		print('Error! Insert just 1 string!')