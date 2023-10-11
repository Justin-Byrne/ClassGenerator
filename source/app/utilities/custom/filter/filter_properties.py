import re

def filter_properties ( list ):

    result = {
        'names': [ ],
        'types': [ ]
    }

    regex  = r'(#?\w+)\s*?=\s*?([^\\]+)'


    for entry in list:

        if re.search ( regex, entry ):

            search = re.search ( regex, entry )

            name   = search.group ( 1 ).strip ( )

            type   = search.group ( 2 ).strip ( ).rstrip ( ';' )


            if type.isdigit ( ):                            type = 'number'

            elif re.search ( r'(\'\w+\'|\"\w+\")', type ):  type = 'string'

            elif re.search ( r'(true|false)', type ):       type = 'boolean'

            elif re.search ( r'new\s*(\w+)', type ):        type = re.search ( r'new\s*(\w+)', type ).group ( 1 )

            else:                                           type = None


            result [ 'names' ].append ( name )

            result [ 'types' ].append ( type )


    return result