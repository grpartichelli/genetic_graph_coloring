import sys

def main():

	NUM_ARGUMENTS = 2

	# total arguments
	if(len(sys.argv)-1 != NUM_ARGUMENTS):
		print("ERROR: Please use the command: python main.py <pathToInputFile> <population>")
		exit(1);

	pathToInputFile = sys.argv[1]
	population = sys.argv[2]
	 




if __name__ == "__main__":
    main()