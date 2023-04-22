import re

ERROR = -1

def is_js_class ( file ):

	metrics = {
		'start'  : None,
		'open'   : None,
		'column' : None
	}


	with open ( file, 'r' ) as reader:

		data = reader.readlines ( )

		for i, line in enumerate ( data ):

			if re.search ( r'class\s*\w+', line ) and metrics [ 'start' ] == None:

				metrics [ 'start' ] = i

				metrics [ 'column' ] = line.find ( 'c' )


			if re.search ( r'{', line  ) and metrics [ 'open' ]  == None:

				metrics [ 'open' ]  = i


			if metrics [ 'start' ] != None and metrics [ 'open' ] != None:

				if ( metrics [ 'start' ] + 1 ) < metrics [ 'open' ]:

					return ERROR


			if metrics [ 'column' ] != None:

				if line.find ( '}' ) == metrics [ 'column' ]:

					return True


	return False
