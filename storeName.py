files = open("s.txt","w")
for  i in range (1,1380):
	line = 'data/obj/' + str(i) + '.jpg'
	files.write(line)
	files.write("\n")

files.close()
