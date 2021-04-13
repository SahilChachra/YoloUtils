import os 


def main(): 

	input_dir = './input/'
	labels = os.listdir(input_dir)
	for i in labels: 
		
		dst = "3_"+str(int(i[:-4]))+i[-4:] 
		src = input_dir + i
		dst ='./output/'+ dst 

		os.rename(src, dst) 


if __name__ == '__main__': 
	
	main() 

