import os
def rename_files():
	#1 get images names from the dirctory
	file_list= os.listdir(r"C:\Users\Sara\Documents\GitHub\udacity-full-stack-python-mini-projects\secret message\alphabet\secret message")
	print(file_list)
	path= os.getcwd()
	print("current working dir :"+path)
	os.chdir(r"C:\Users\Sara\Documents\GitHub\udacity-full-stack-python-mini-projects\secret message\alphabet\secret message")
	print(path)
	#2 rename every file by removing numbers
	for name in file_list:
		text = name.translate(str.maketrans('','','1234567890'))
		print("text :"+text)
		os.rename(name, text)

	print(file_list)	
rename_files()