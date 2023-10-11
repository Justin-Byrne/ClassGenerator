import os.path
import re

def get_file_bounds ( file, regexes ):

    bounds = {
        'start': None,
        'close': None
    }


    if os.path.isfile ( file ):

        for number, line in enumerate ( open ( file, 'r' ).readlines ( ) ):

            for regex in regexes [ 'start' ]:

                if re.search ( regex, line ):

                    bounds [ 'start' ] = number

                    break


            for regex in regexes [ 'close' ]:

                if re.search ( regex, line ):

                    bounds [ 'close' ] = number

                    return bounds

    else:

        print ( ' >> [ERROR] get_file_bounds.py\n', f'\t~ File: "{file}", is not a valid file !' )