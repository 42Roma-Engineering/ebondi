import sys

def ft_char_count(string):
	c_count = {}
	for c in string:
		ret = c_count.get(c, 0)
		c_count[c]=ret+1
	for key, value in c_count.items():
		print(key, value)

if __name__=="__main__":
	if len(sys.argv) > 1:
		ft_char_count(sys.argv[1])
	else:
		print('Error! No string given')