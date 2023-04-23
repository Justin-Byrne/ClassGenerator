import sys
import re

# from utilities.system.list.create_2d_list    import create_2d_list

#### 	TEMPORARY DUPLICATION ##############################

ERROR = -1

def create_2d_list ( depth ):

	#### 	ERROR HABDLING 	########

	if depth < 1 or depth == None:

		print ( 'create_2d_list.py requires a depth value param of at least 1 !' )

		return ERROR

	#### 	ERROR HABDLING 	########


	return [ [ ] for i in range ( depth ) ]

#### 	TEMPORARY DUPLICATION ##############################

def clean_properties ( properties, substitutions ):

	regex  = r'\[(\w+=)(\w+)\]'

	result = create_2d_list ( len ( properties ) )

	props  = [ ]


	for i, property in enumerate ( properties ):

		property = property [ 0:2 ] 							# Trim: property


		# property [ 0 ] : check substitutions
		for substitution in substitutions:

			if property [ 0 ] == substitution [ 0 ]:

				props       = list ( property )

				props [ 0 ] = substitution [ 1 ]

				property    = tuple ( props )


		# property [ 1 ] : Check and modify default values
		if re.search ( regex, property [ 1 ] ):

			temp        = re.search ( regex, property [ 1 ] )

			props       = list ( property )

			props [ 1 ] = f"{temp [ 1 ]}[<color:orangered>{temp [ 2 ]}</color>]"

			property    = tuple ( props )


		result [ i ] = list ( property )


	return result 												# Populate: properties in diagram
