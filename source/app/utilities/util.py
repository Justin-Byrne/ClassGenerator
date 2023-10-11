# SYSTEM
from .system.validation.is_directory    import is_directory
from .system.validation.is_file         import is_file
from .system.validation.is_flag         import is_flag
from .system.validation.is_program      import is_program
from .system.get_command_type           import get_command_type
from .system.get_commands               import get_commands
from .system.file.get_files             import get_files
from .system.file.get_file_omissions    import get_file_omissions
from .system.file.get_file_bounds       import get_file_bounds
from .system.file.set_file              import set_file

# CUSTOM
from .custom.validation.is_extension    import is_extension
from .custom.validation.is_js_class     import is_js_class
from .custom.debug.view_arguments       import view_arguments
from .custom.filter.filter_properties   import filter_properties
from .custom.filter.filter_type         import filter_type
from .custom.list.get_column_max        import get_column_max

class Util:

    def __init__ (  ): pass

    ####    SYSTEM  ########################################

    # VALIDATION

    def is_directory       ( path )                                 : return is_directory       ( path )

    def is_file            ( path,   type = None )                  : return is_file            ( path, type )

    def is_flag            ( string, flag = '-'  )                  : return is_flag            ( string, flag )

    def is_program         ( program )                              : return is_program         ( program )

    # COMMAND

    def get_command_type   ( command  )                             : return get_command_type   ( command  )

    def get_commands       ( commands )                             : return get_commands       ( commands )

    # FILE

    def get_files          ( path, type, omissions = '' )           : return get_files          ( path, type, omissions )

    def get_file_omissions ( arguments )                            : return get_file_omissions ( arguments )

    def get_file_bounds    ( file, regexes )                        : return get_file_bounds    ( file, regexes )

    def set_file           ( source, destination )                  : return set_file           ( source, destination )

    ####    CUSTOM  ########################################

    # VALIDATION

    def is_extension       ( line, list )                           : return is_extension       ( line, list )

    def is_js_class        ( file )                                 : return is_js_class        ( file )

    # DEBUG

    def view_arguments     ( arguments )                            : return view_arguments     ( arguments )

    # FILTER

    def filter_properties  ( list )                                 : return filter_properties  ( list )

    def filter_type        ( type )                                 : return filter_type        ( type )

    # LIST

    def get_column_max     ( dictionary )                           : return get_column_max     ( dictionary )