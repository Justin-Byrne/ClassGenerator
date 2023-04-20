import os

def get_files ( path, type, omissions = '' ):

	result = [ ]

	#### 	FUNCTIONS 	####################################

	def filter_omissions ( ):

		# for omission in self.arguments [ 'omit_files' ].split ( '|' ):

		for omission in omissions.split ( '|' ):

			entry_no_suffix = os.path.splitext ( entry ) [ 0 ]


			if omission == entry_no_suffix:

				return True


		return False

	#### 	LOGIC 	########################################

	for ( root, dirs, file ) in os.walk ( path ):

		for entry in file:

			if type in entry:

				print ( 'omissions: ', omissions )

				if omissions:

					if filter_omissions ( ):

						continue

					else:

						result.append ( f"{root}/{entry}" )

				else:

					result.append ( f"{root}/{entry}" )

	# for item in result:

		# print ( item )

	return result
