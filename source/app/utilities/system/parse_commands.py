import re

from os.path 					import dirname

from .list.list_to_string 		import list_to_string
from .get_command_type 			import get_command_type
from .validation.is_program 	import is_program

def parse_commands ( commands ):

	#### 	GLOBALS 	####################################

	arguments = {
		'flag':        None,
		'source':      None,
		'destination': None
	}

	regexes = {
		'locations':  r'(\/\w+[^\s*]+)',
		'omit_files': r'\s*-o\s*|\s*--omit\s*',
		'skin_param': r'\s*-s\s*|\s*--skin\s*',
		'link_files': r'\s*-l\s*|\s*--link\s*',
		'make_image': r'\s*-m\s*|\s*--make\s*'
	}

	image_types = [
		'png',
		'svg',
		'eps',
		'eps:text',
		'pdf',
		'vdx',
		'xmi',
		'scxml',
		'html',
		'txt',
		'utxt',
		'latex',
		'latex:nopreamble',
		'braille'
	]

	#### 	FUNCTIONS 	####################################

	def check_command_line ( ):

		for i in range ( 1, len ( commands ) ):

			command = commands [ i ]


			for regex in regexes:

				if ( re.search ( regexes [ regex ], command ) ):

					match regex:

						case 'locations':

							if arguments [ 'source' ] == None:

								arguments [ 'source' ] = command

							elif arguments [ 'destination' ] == None:

								arguments [ 'destination' ] = command

						case 'omit_files':

							if regex != arguments.keys ( ):

								value = commands [ i + 1 ].split ( '|' )

								arguments.update ( { regex: value } )

						case 'skin_param':

							if regex != arguments.keys ( ):

								value = commands [ i + 1 ].split ( '|' )

								value = [ v.replace ( '+', ' ' ) for v in value ]

								arguments.update ( { regex: value } )

						case 'link_files':

							if regex != arguments.keys ( ):

								arguments.update ( { regex: True } )

						case 'make_image':

							if regex != arguments.keys ( ):

								value = commands [ i + 1 ].split ( '|' )


								if set ( value ).issubset ( image_types ):

									arguments.update ( { regex: value } )

								else:

									print ( 'parse_commands.py received an inaccurate image-type !' )

	def check_config_file  ( ):

		config_regex = {
			'omit_files': r'FILE OMISSIONS',
			'skin_param': r'SKIN PARAM',
			'make_image': r'IMAGE OUTPUT'
		}

		for regex in config_regex:

			if regex != arguments.keys ( ):

				list    = [ ]

				lines   = open ( './config/config.txt', 'r' ).readlines ( )

				capture = False


				for line in lines:

					if capture and line [ 0 ] == '\n':

						break


					if re.search ( config_regex [ regex ], line ):

						capture = True

						continue


					if capture:

						if line [ 0 ] == '#': continue

						else: list.append ( line.replace ( '\n', '' ) )


					if len ( list ) > 0:

						arguments.update ( { regex: list } )

	def check_plant_uml    ( ):

		if 'make_image' in arguments.keys ( ):

			if is_program ( 'java' ):

				data = open ( './config/config.txt', 'r' ).read ( )

				path = re.search ( r'PLANTUML PATH\s*path=([^\s]+)', data ).group ( 1 )


				if re.search ( r'plantuml\.jar', path ) == None:

					path = f"{path.rstrip ( '/' )}/plantuml.jar"


				arguments.update ( { 'plant_path': path } )

	#### 	LOGIC 		####################################

	check_command_line ( )

	check_config_file  ( )

	check_plant_uml    ( )


	return arguments
