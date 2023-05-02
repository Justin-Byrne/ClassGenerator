from distutils.spawn 	import find_executable

def is_program ( program ):

    return find_executable ( program ) is not None
