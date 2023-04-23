import sys

from utilities.util    import Util
from core.generator    import Generator

ERROR = -1

def main ( commands ):

	arguments = Util.get_commands ( commands )


	if arguments != ERROR:

		Generator ( arguments )


main ( sys.argv )
