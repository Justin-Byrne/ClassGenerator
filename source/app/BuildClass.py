import sys
from utilities.util import Util

ERROR = -1

def print_arguments ( arguments ):

	print ( '-' * 100 )
	print ( "Flag: \t\t",      arguments [ 'flag'        ] )
	print ( "Source: \t",      arguments [ 'source'      ] )
	print ( "Destination: \t", arguments [ 'destination' ] )
	print ( '-' * 100 )


def main ( commands ):

	arguments = Util.get_commands ( commands )

	if arguments != ERROR:

		print_arguments ( arguments )


main ( sys.argv )
