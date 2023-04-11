from .get_command_type import get_command_type

from .validation.is_flag      import is_flag
from .validation.is_file      import is_file
from .validation.is_directory import is_directory

def print_command ( command ):

	print ( 'command: ', command )

	if is_flag      ( command, '-'  ): print ( '- flag'      )

	if is_file      ( command, None ): print ( '- file'      )

	if is_directory ( command       ): print ( '- directory' )


def get_commands ( commands ):

	arguments = parse_commands ( commands )

	# CHECK WHETHR A SOURCE IS PRESENT
	if arguments [ 'source' ] == None:

		print ( 'BuildClass.py requires a single source... try again !' )

		return -1

	# CHECK WHETHER DIRECTORY IS GOING INTO SINGLE FILE
	if arguments [ 'source' ] != None and arguments [ 'destination' ] != None:

		if is_directory ( arguments [ 'source'] ) and is_file ( arguments [ 'destination' ], None ):

			print ( 'BuildClass.py a whole directory cannot be parsed into a single file... try again !' )

			return -1

	return arguments


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

	match len ( commands ) - 1:

		case 1: 	# Command 1

			# 1
			if get_command_type ( commands [ 1 ] ) == 'file' or get_command_type ( commands [ 1 ] ) == 'directory':

				set_io ( commands [ 1 ] )

			if get_command_type ( commands [ 1 ] ) == 'flag':

				set_flag ( commands [ 1 ] )

		case 2: 	# Command 1 & 2

			# 1
			if get_command_type ( commands [ 1 ] ) == 'file' or get_command_type ( commands [ 1 ] ) == 'directory':

				set_io ( commands [ 1 ] )

			if get_command_type ( commands [ 1 ] ) == 'flag':

				set_flag ( commands [ 1 ] )


			# 2
			if get_command_type ( commands [ 2 ] ) == 'file' or get_command_type ( commands [ 2 ] ) == 'directory':

				set_io ( commands [ 2 ] )

			if get_command_type ( commands [ 2 ] ) == 'flag':

				set_flag ( commands [ 2 ] )


			pass

		case 3: 	# Command 1, 2, & 3

			# 1
			if get_command_type ( commands [ 1 ] ) == 'file' or get_command_type ( commands [ 1 ] ) == 'directory':

				set_io ( commands [ 1 ] )

			if get_command_type ( commands [ 1 ] ) == 'flag':

				set_flag ( commands [ 1 ] )


			# 2
			if get_command_type ( commands [ 2 ] ) == 'file' or get_command_type ( commands [ 2 ] ) == 'directory':

				set_io ( commands [ 2 ] )

			if get_command_type ( commands [ 2 ] ) == 'flag':

				set_flag ( commands [ 2 ] )


			# 3
			if get_command_type ( commands [ 3 ] ) == 'file' or get_command_type ( commands [ 3 ] ) == 'directory':

				set_io ( commands [ 3 ] )

			if get_command_type ( commands [ 3 ] ) == 'flag':

				set_flag ( commands [ 3 ] )

		case _:

			print ( 'BuildClass.py requires at least one, and no more than 3, arguments !' )

	return arguments
