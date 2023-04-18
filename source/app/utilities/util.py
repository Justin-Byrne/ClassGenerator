# SYSTEM
from .system.validation.is_directory 	import is_directory
from .system.validation.is_file      	import is_file
from .system.validation.is_flag      	import is_flag
from .system.get_command_type        	import get_command_type
from .system.get_commands 			 	import get_commands
from .system.file.get_eof 			 	import get_eof
from .system.string.repeat_character 	import repeat_character
from .system.list.create_2d_list  	 	import create_2d_list
from .system.list.entry_padding 	 	import entry_padding

# CUSTOM
from .custom.validation.is_extension    import is_extension
from .custom.cleanup.clean_properties   import clean_properties

class Util:

	def __init__ (  ): pass

	#### 	SYSTEM 	########################################

	# VALIDATION

	def is_directory 	 ( path ) 				  				: return is_directory     ( path )

	def is_file 	 	 ( path,   type = None )  				: return is_file          ( path, type )

	def is_flag      	 ( string, flag = '-'  )  				: return is_flag 	        ( string, flag )

	# COMMAND

	def get_command_type ( command  ) 		 	  				: return get_command_type ( command  )

	def get_commands     ( commands ) 		 	  				: return get_commands     ( commands )

	# FILE

	def get_eof 		 ( file ) 				  				: return get_eof          ( file )

	# STRING

	def repeat_character ( character, times = 0 ) 				: return repeat_character ( character, times )

	# LIST

	def create_2d_list   ( depth ) 				  				: return create_2d_list   ( depth )

	def entry_padding    ( tuple_list, padding = 3, entry = 0 ) : return entry_padding 	  ( tuple_list, padding, entry )

	#### 	CUSTOM 	########################################

	# VALIDATION

	def is_extension     ( line, list ) 		  				: return is_extension     ( line, list )

	# CLEANUP

	def clean_properties ( properties, substitutions ) 		    : return clean_properties ( properties, substitutions )
