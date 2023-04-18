import os

from .get_command_type import get_command_type

from .validation.is_flag      import is_flag
from .validation.is_file      import is_file
from .validation.is_directory import is_directory

ERROR = -1

def print_command  ( command  ):

	print ( 'command: ', command )

	if is_flag      ( command, '-'  ): print ( '- flag'      )

	if is_file      ( command, None ): print ( '- file'      )

	if is_directory ( command       ): print ( '- directory' )


def parse_commands ( commands ):

	arguments = {
		'flag':        None,
		'source':      None,
		'destination': None
	}

	def set_flag ( value ):

		if get_command_type ( value ) == 'flag':

			if arguments [ 'flag' ] is None:

				arguments [ 'flag' ] = value

	def set_io   ( value ):

		if get_command_type ( value ) == 'file' or get_command_type ( value ) == 'directory':

			if arguments [ 'source' ] is None:

				arguments [ 'source' ] = value

			else:

				if arguments [ 'destination' ] is None:

					arguments [ 'destination' ] = value

	# PRINT COMMAND
	# for command in commands: print_command ( command )

	for i in range ( 1, len ( commands ) ):

		# SET: INPUT & OUTPUT
		if get_command_type ( commands [ i ] ) == 'file' or get_command_type ( commands [ i ] ) == 'directory':

			set_io ( commands [ i ] )

		# SET: FLAG
		if get_command_type ( commands [ i ] ) == 'flag':

			set_flag ( commands [ i ] )


	return arguments

def get_commands   ( commands ):

	arguments = parse_commands ( commands )

	# CHECK WHETHR A SOURCE IS PRESENT
	if arguments [ 'source' ] == None:

		print ( 'BuildClass.py requires a single source... try again !' )

		return ERROR

	# CHECK WHETHER DIRECTORY IS GOING INTO SINGLE FILE
	if arguments [ 'source' ] != None and arguments [ 'destination' ] != None:

		if is_directory ( arguments [ 'source'] ) and is_file ( arguments [ 'destination' ], None ):

			print ( 'BuildClass.py a whole directory cannot be parsed into a single file... try again !' )

			return ERROR

	# IF ONLY SOURCE IS PRESENT MIRROR AS DESTINATION
	if arguments [ 'source' ] != None and arguments [ 'destination' ] == None:

		if is_directory ( arguments [ 'source'] ):

			arguments [ 'destination' ] = arguments [ 'source' ]

		elif is_file ( arguments [ 'source' ], None ):

			arguments [ 'destination' ] = os.path.dirname ( arguments [ 'source' ] )


	return arguments
