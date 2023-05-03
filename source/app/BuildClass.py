import sys

from utilities.util     import Util
from core.generator     import Generator
from core.linker 		import Linker

ERROR = -1

def main ( commands ):

	arguments = Util.get_commands ( commands )


	if arguments != ERROR:

		if Generator ( arguments ) and arguments [ 'link_files' ]:

			Linker ( arguments )
			

main ( sys.argv )
