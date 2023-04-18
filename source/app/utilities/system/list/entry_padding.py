import re

ERROR = -1

def get_max_tuple_length ( tuple_list ):

	result = 0


	for tuple in tuple_list:

		tuple_length = len ( tuple )


		if ( tuple_length ) > result:

			result = tuple_length


	return result - 1


def entry_padding ( tuple_list, padding = 3, entry = 0 ):

	#### 	ERROR HABDLING 	########

	if padding < 1:

		print ( 'entry_padding.py requires a padding param value of at least 1 !')

		return ERROR


	if entry > get_max_tuple_length ( tuple_list ) or entry < 0:

		print ( 'entry_padding.py entry param value is not uniformly accessible through tuple_list param value !')

		return ERROR

	#### 	ERROR HABDLING 	########


	spacing = [ ]


	for tuple in tuple_list:

		result = len ( tuple [ entry ] )

		spacing.append ( result )


	max_length = max ( spacing ) + padding


	for i, space in enumerate ( spacing ):

		spacing [ i ] = max_length - space


	return spacing
