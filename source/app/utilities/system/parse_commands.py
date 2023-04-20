import re

from .list.list_to_string 	  import list_to_string

from .get_command_type 		  import get_command_type

def parse_commands ( commands ):

	arguments = {
		'flag':        None,
		'source':      None,
		'destination': None
	}

	special_flags = {
		'omit_files': r'-o\s*([^\s]+)'
	}

	#### 	FUNCTIONS 	####################################

	def get_special_flags (       ):

		command_string = list_to_string ( commands )


		for flag in special_flags:

			if re.search ( special_flags [ flag ], command_string ):

				arguments.update ( { flag: re.findall ( special_flags [ flag ], command_string ) [ 0 ] } )

	def set_flag          ( value ):

		if get_command_type ( value ) == 'flag':

			if arguments [ 'flag' ] is None:

				arguments [ 'flag' ] = value

	def set_io            ( value ):

		if get_command_type ( value ) == 'file' or get_command_type ( value ) == 'directory':

			if arguments [ 'source' ] is None:

				arguments [ 'source' ] = value

			else:

				if arguments [ 'destination' ] is None:

					arguments [ 'destination' ] = value

	#### 	LOGIC	########################################

	get_special_flags ( )


	for i in range ( 1, len ( commands ) ):

		# SET: INPUT & OUTPUT
		if get_command_type ( commands [ i ] ) == 'file' or get_command_type ( commands [ i ] ) == 'directory':

			set_io ( commands [ i ] )

		# SET: FLAG
		if get_command_type ( commands [ i ] ) == 'flag':

			set_flag ( commands [ i ] )


	return arguments
