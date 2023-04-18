import os.path

ERROR = -1

def get_eof ( file ):

	if os.path.isfile ( file ):

		with open ( file, 'r' ) as reader:

			return len ( reader.readlines ( ) ) - 1

	else:

		return ERROR
