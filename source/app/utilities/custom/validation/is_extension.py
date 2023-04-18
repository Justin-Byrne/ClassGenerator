import re

regex = {
	'property':  r'\[',
	'extension': r'\/\/\/\/\s*\W\s?(\w+(\s?\w+)(\s?\w+)(\s?\w+)(\s?\w+))\s*\/\/\/\/'
}

def is_extension ( line, list ):

	if re.search ( regex [ 'property' ], line ):

		return True

	for entry in list:

		if re.search ( regex [ 'extension' ], line ).group ( 1 ) == entry:

			return True


	return False
