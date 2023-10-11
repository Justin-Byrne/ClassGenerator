def get_keys ( dictionary ):

    keys = [ ]


    for id in dictionary:

        if isinstance ( dictionary [ id ], dict ):

            if dictionary [ id ]:

                keys.append ( id )


    return keys


def get_column_max ( dictionary ):

    length = 0

    keys   = get_keys ( dictionary )


    for key in keys:

        for value in dictionary [ key ] [ 'names' ]:

            value_length = len ( value )


            if length < value_length:

                length = value_length


    return length