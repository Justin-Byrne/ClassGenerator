import re

from .list.list_to_string 	  import list_to_string

from .get_command_type 		  import get_command_type

def parse_commands ( commands ):

	arguments = {
		'flag':        None,
		'source':      None,
		'destination': None
	}

	regex_flags = {
		'omit_files': r'-o\s*([^\s]+)|--omit\s*([^\s]+)',
		'skin_param': r'-s\s*([^\s]+)|--skin\s*([^\s]+)'
	}

	#### 	FUNCTIONS 	####################################

	def get_special_flags ( ):

		command_string = list_to_string ( commands )


		for flag in regex_flags:

			list = [ ]

			if re.search ( regex_flags [ flag ], command_string ):

				flag_commands = re.findall ( regex_flags [ flag ], command_string ) [ 0 ]

				flag_commands = [    entry for entry in flag_commands if entry != ''    ]


				for command in flag_commands:

					list.append ( command.replace ( '/', ' ' ) )


				arguments.update ( { flag: list [ 0 ].split ( '|' ) } )

			else:

				config_regex = {
					'omit_files': r'FILE OMISSIONS',
					'skin_param': r'SKIN PARAM'
				}

				lines   = open ( './config/config.txt', 'r' ).readlines ( )

				capture = False


				for line in lines:

					if capture and line [ 0 ] == '\n':

						break


					if re.search ( config_regex [ flag ], line ):

						capture = True

						continue


					if capture:

						if line [ 0 ] == '#': continue

						else: list.append ( line.replace ( '\n', '' ) )


					if len ( list ) > 0:

						arguments.update ( { flag: list } )

	#### 	LOGIC	########################################

	get_special_flags ( )


	for i in range ( 1, len ( commands ) ):

		command = commands [ i ]

		# SET: INPUT & OUTPUT
		if arguments [ 'source' ] is None:

			if get_command_type ( command ) == 'file' or \
			   get_command_type ( command ) == 'directory':

			   arguments [ 'source' ] = command

		else:

			if re.search ( r'(\/\w+){1,}', command ):

				arguments [ 'destination' ] = command

		# SET: FLAG
		if get_command_type ( command ) == 'flag':

			if arguments [ 'flag' ] is None:

				arguments [ 'flag' ] = command


	return arguments
