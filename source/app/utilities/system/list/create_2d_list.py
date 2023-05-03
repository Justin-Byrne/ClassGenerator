ERROR = -1

def create_2d_list ( depth ):

	#### 	ERROR HABDLING 	########

	if depth < 1 or depth == None:

		print ( ' >> [ERROR] create_2d_list.py\n\t~ Requires a depth value param of at least 1 !' )

		return ERROR

	#### 	ERROR HABDLING 	########


	return [ [ ] for i in range ( depth ) ]
