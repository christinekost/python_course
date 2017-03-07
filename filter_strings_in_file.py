

# cannot really run it via terminal for some reasons


limit = 10

with open('/Users/UniQue/Desktop/t1.txt') as input_file,\
     open('/Users/UniQue/Desktop/t111.txt') as output_file:
		for line in input_file:
			if len(line) > limit:
				output_file.write(line)

