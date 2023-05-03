import os.path
import re

def is_file ( path, type ):

	if os.path.isfile ( path ):

		if type == None:

			return True

		else:

			if re.search ( r'\.\w+', type ):

				return path.lower ( ).endswith ( type )

			else:

				print ( ' >> [ERROR] is_file.py\n', f'\t~ Type: "{type}", is not a valid file type !' )

				return False

	else:

		return False
