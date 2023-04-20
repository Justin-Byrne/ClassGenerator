import os

from .parse_commands 			import parse_commands

from .validation.is_file      	import is_file
from .validation.is_directory 	import is_directory

ERROR = -1

def get_commands   ( commands ):

	arguments = parse_commands ( commands )


	if arguments [ 'source' ] == None: 																# CHECK WHETHR A SOURCE IS PRESENT

		print ( 'BuildClass.py requires a single source... try again !' )

		return ERROR


	if arguments [ 'source' ] != None and arguments [ 'destination' ] != None: 						# CHECK WHETHER DIRECTORY IS GOING INTO SINGLE FILE

		if is_directory ( arguments [ 'source'] ) and is_file ( arguments [ 'destination' ], None ):

			print ( 'BuildClass.py a whole directory cannot be parsed into a single file... try again !' )

			return ERROR


	if arguments [ 'source' ] != None and arguments [ 'destination' ] == None: 						# IF ONLY SOURCE IS PRESENT MIRROR AS DESTINATION

		if is_directory ( arguments [ 'source'] ):

			arguments [ 'destination' ] = arguments [ 'source' ]

		elif is_file ( arguments [ 'source' ], None ):

			arguments [ 'destination' ] = os.path.dirname ( arguments [ 'source' ] )


	return arguments
