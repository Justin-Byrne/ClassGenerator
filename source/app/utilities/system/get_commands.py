import os

from .parse_commands 			import parse_commands

from .validation.is_file      	import is_file
from .validation.is_directory 	import is_directory

ERROR = -1

def get_commands   ( commands ):

	arguments = parse_commands ( commands )


	if arguments [ 'help_menu' ]:

		menu = [
			'PlantUML class generator for JavaScript\n\n'
			'python3 BuildClass.py {<source>} [<destination>] [flags] [args[|args...]]\n\n'
			'PATHS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n\n'
			'source\t\t\t\tFile or directory location of javascript file(s) to convert\n\n'
			'\t\t\t\tusage: \n'
			'\t\t\t\t\t(single)    "/javascript/classes/one.js"\n'
			'\t\t\t\t\t(multiple)  "/javascript/classes"\n\n'
			'destination\t\t\tFile or directory location to save class diagrams\n\n'
			'\t\t\t\tusage: \n'
			'\t\t\t\t\t(single)    "/javascript/classes/output/one.txt"\n'
			'\t\t\t\t\t(multiple)  "/javascript/classes/output"\n\n'
			'FLAGS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\n\n'
			'-o, --omit "<filename>"\t\tOmit the following filenames from the source directory\n\n'
			'\t\t\t\tusage: \n'
			'\t\t\t\t\t(single)   	--omit "file1"\n'
			'\t\t\t\t\t(multiple) 	--omit "file1|file2|file3"\n\n'
			'-s, --skin "<skinparam>"\tEmbed skin parameters within the class uml generated\n\n'
			'\t\t\t\tusage: \n'
			'\t\t\t\t\t(single)     --skin "skinparam+one+1"\n'
			'\t\t\t\t\t(multiple)   --skin "skinparam+one+1|skinparam+two+2"\n\n'
			'-m, --make "<image_type>"\tMake the class generated diagram into an image\n\n'
			'\t\t\t\tusage: \n'
			'\t\t\t\t\t(single) 	--make "png"\n'
			'\t\t\t\t\t(multiple)	--make "png|svg|eps"\n\n'
			'-l, --link\t\t\tLink available classes to generated class diagrams\n\n'
			'\t\t\t\tusage: --link\n\n'
			'-h, --help\t\t\tDisplay this help menu\n\n'
			'\t\t\t\tusage: --help'
		]

		for line in menu:

			print ( line )


		return ERROR;


	if arguments [ 'source' ] == None: 																# CHECK WHETHR A SOURCE IS PRESENT

		print ( ' >> [ERROR] BuildClass.py\n\t~ Requires a single source !' )

		return ERROR


	if arguments [ 'source' ] != None and arguments [ 'destination' ] != None: 						# CHECK WHETHER DIRECTORY IS GOING INTO SINGLE FILE

		if is_directory ( arguments [ 'source'] ) and is_file ( arguments [ 'destination' ], None ):

			print ( ' >> [ERROR] BuildClass.py\n\t~ A whole directory cannot be parsed into a single file !' )

			return ERROR


	if arguments [ 'source' ] != None and arguments [ 'destination' ] == None: 						# IF ONLY SOURCE IS PRESENT MIRROR AS DESTINATION

		if arguments [ 'source' ] [ len ( arguments [ 'source' ] ) - 1 ] == '/':

			arguments [ 'source' ] = arguments [ 'source' ] [ :-1 ]


		if is_directory ( arguments [ 'source'] ):

			arguments [ 'destination' ] = f"{arguments [ 'source' ]}/output"

		elif is_file ( arguments [ 'source' ], None ):

			arguments [ 'destination' ] = f"{os.path.dirname ( arguments [ 'source' ] )}/output"


	return arguments
