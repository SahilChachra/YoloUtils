import os 


def main(): 

	for count, filename in enumerate(os.listdir("./input/")): 
		dst =str(count) + ".txt"
		src ='./input/'+ filename 
		dst ='./output/'+ dst 
		
		
		os.rename(src, dst) 


if __name__ == '__main__': 
	
	
	main() 

