import os
import re

# from utilities.custom.validation.is_js_class 	import is_js_class

#### 	TEMPORARY DUPLICATION ##############################

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

				metrics [ 'start'  ] = i

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

#### 	TEMPORARY DUPLICATION ##############################

def get_files ( path, type, omissions = '' ):

	result = [ ]

	#### 	FUNCTIONS 	####################################

	def filter_omissions ( omissions ):

		for omission in omissions:

			entry_no_suffix = os.path.splitext ( entry ) [ 0 ]


			if omission == entry_no_suffix:

				return True


		return False

	#### 	LOGIC 	########################################

	for ( root, dirs, file ) in os.walk ( path ):

		for entry in file:

			record = f"{root}/{entry}"


			if type in entry:

				if omissions:

					if filter_omissions ( omissions ):

						continue

					else:

						if is_js_class ( record ):

							result.append ( record )

						else:

							continue
				else:

					if is_js_class ( record ):

						result.append ( record )

					else:

						continue


	return result
