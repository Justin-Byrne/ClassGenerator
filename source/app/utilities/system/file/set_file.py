import re
import os

def set_file ( source, destination ):

    if re.search ( r'\w.+\.txt', destination ):

        directory   = os.path.dirname ( destination )

        output_path = destination


        if os.path.isdir ( directory ) is False:

            os.makedirs ( directory )

    else:

        filename    = os.path.basename ( source ).split ( '/' ) [ -1 ].replace ( '.js', '' )

        output_path = f"{destination}/{filename}.txt"


        if os.path.isdir ( destination ) is False:

            os.makedirs ( destination )


    return output_path