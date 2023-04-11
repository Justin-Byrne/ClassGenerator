import sys
from utilities.util import Util

ERROR = -1

def main ( commands ):

	arguments = Util.get_commands ( commands )

	if arguments != ERROR:

		print ( 'arguments: ', arguments )


main ( sys.argv )
