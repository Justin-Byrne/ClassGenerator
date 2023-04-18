from .validation.is_flag 	  import is_flag
from .validation.is_file 	  import is_file
from .validation.is_directory import is_directory

def get_command_type ( command ):

	if is_flag      ( command, '-'  ): return 'flag'

	if is_file      ( command, None ): return 'file'

	if is_directory ( command       ): return 'directory'
