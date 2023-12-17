import pickle

def dump_word():
	try:
		f = open('words.txt', 'r')
	except FileNotFoundError:
		return
	dump_dict = {}
	max = 0
	for line in f:
		line = line.rstrip('\n')
		if len(line) > max:
			max = len(line)
	i = 1
	while i <= max:
		dump_dict.setdefault(i, 0)
		i += 1
	f = open('words.txt', 'r')	
	for line in f:
		line = line.rstrip('\n')
		size = len(line)
		print(size)
		dump_dict[size] += 1
	to_delete = []
	for key in dump_dict:
		if dump_dict[key] == 0:
			to_delete.append(key)
	for key in to_delete:
		dump_dict.pop(key)
	with open('word_count.pickle', "wb") as f:
		pickle.dump(dump_dict, f)
	print(dump_dict)

if __name__=="__main__":
	dump_word()