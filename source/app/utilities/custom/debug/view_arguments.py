def view_arguments ( arguments ):

	print ( '-' * 100 )

	print ( "Source: \t",      arguments [ 'source'      ] )

	print ( "Destination: \t", arguments [ 'destination' ] )

	print ( '. ' * 50 )

	for i, argument in enumerate ( arguments ):

		print ( f'{argument}\n', arguments [ argument ], f'\n' )

	print ( '-' * 100 )
