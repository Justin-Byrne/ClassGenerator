import os
import re
import subprocess

from utilities.util                         import Util

from .linker                                import Linker

class Generator:

    def __init__( self, arguments ):

        ####    GLOBALS     ################################

        self.arguments       = arguments

        self.files           = [ ]

        self.output_path     = None

        ########################################

        self.class_header    = None

        self.template        = { }

        self.plantuml_script = None

        self.tags = {
            'properties': '',
            'setters':    '__ Setter __',
            'getters':    '__ Getter __',
            'utilities':  '__ Utility __'
        }

        ####    INITIALIZATION    ##########################

        self.init ( )

    ####    INITIATORS  ########################################################

    def init    ( self ):

        self.get_files ( )

        self.compile   ( )


    def compile ( self ):

        for file in self.files:

            self.process ( file )

            self.render  ( file )


    def process ( self, file ):

        self.template = {
            'class': None,
            'properties':
            {
                'names': [ ],
                'types': [ ]
            },
            'setters':
            {
                'names': [ ],
                'types': [ ]
            },
            'getters':
            {
                'names': [ ],
                'types': [ ]
            },
            'utilities':
            {
                'names': [ ],
                'types': [ ]
            }
        }

        self.get_header     ( file )

        self.get_class      ( file )

        self.get_properties ( file )

        self.get_mutators   ( file )

        self.get_utilities  ( file )


    def render  ( self, file ):

        self.prepare_file    ( file )

        self.compose_header  ( )

        self.compose_members ( )

        self.compose_footer  ( )

        self.save_output     ( )

        self.compose_image   ( )

    ####    GETTERS     ########################################################

    def get_files      ( self ):

        source = self.arguments [ 'source' ];


        if ( Util.is_file ( source ) ):                     # If: file

            self.files.append ( source )


        if ( Util.is_directory ( source ) ):                # If: directory

            omissions  = Util.get_file_omissions ( self.arguments )

            self.files = Util.get_files ( source, '.js', omissions )


    def get_header     ( self, file ):

        regex = r'(\/\*\*[^@]+@class[^\/]+\/)'


        with open ( file, 'r' ) as reader:

            data = reader.read ( )


            if re.search ( regex, data ):

                self.class_header = re.search ( regex, data ).group ( 1 )


    def get_class      ( self, file ):

        regex = r'class\s*(\w+)[^{]+{'


        with open ( file, 'r' ) as reader:

            data = reader.read ( )

            self.template [ 'class' ] = re.search ( regex, data ).group ( 1 )


    def get_properties ( self, file ):

        if self.class_header:

            regex = r'@property\s*{(.+)}\s*((\w+)|\[(\w+)=(\w+)\]?)'

            temp  = re.findall ( regex, self.class_header )


            for value in temp:

                self.template [ 'properties' ] [ 'names' ].append ( value [ 1 ] )

                self.template [ 'properties' ] [ 'types' ].append ( value [ 0 ] )

        else:

            regexes = {
                'start':
                [
                    r'class\s*\w+'
                ],
                'close':
                [
                    r'\s{2,4}constructor\s*\(',
                    r'\s{2,4}set\s*\w+(\s*?)\(',
                    r'\s{2,4}get\s*\w+(\s*?)\('
                ]
            }

            bounds = Util.get_file_bounds ( file, regexes )

            lines  = open ( file ).readlines ( )

            lines  = lines [ bounds [ 'start' ] : bounds [ 'close' ] ]


            self.template [ 'properties' ] = Util.filter_properties ( lines )


    def get_mutators   ( self, file ):

        data  = open ( file, 'r' ).read ( )


        for mutator in [ 'set', 'get' ]:

            mutator_type = mutator + 'ters'


            # Docstring

            regex    = r'@param\s*\{(\w+)\}[^\/]+\/[^s]+set\s(\w+)' if mutator == 'set' else r'@return\s*{(\w+)}[^\/]+\/[^g]+get\s(\w+)'

            mutators = re.findall ( regex, data )


            for value in mutators:

                self.template [ mutator_type ] [ 'names' ].append ( value [ 1 ] )

                self.template [ mutator_type ] [ 'types' ].append ( value [ 0 ] )


            # Vanilla

            regex    = r'\s{2,4}' + mutator + r'\s*(\w+)\s*\([^\)]+\)'

            mutators = re.findall ( regex, data )


            for value in mutators:

                if value not in self.template [ mutator_type ] [ 'names' ]:

                    self.template [ mutator_type ] [ 'names' ].append ( value )

                    self.template [ mutator_type ] [ 'types' ].append ( None  )


    def get_utilities  ( self, file ):

        data  = open ( file, 'r' ).read ( )


        # Docstring

        regex     = r'@return\s*{(\w+)}[^\/]+\/\s*\b(?!return\b|let\b|this\b|if\b|switch\b|for\b)(\w+)\s*\([^\)]+\)'

        utilities = re.findall ( regex, data )


        for value in utilities:

            self.template [ 'utilities' ] [ 'names' ].append ( value [ 1 ] )

            self.template [ 'utilities' ] [ 'types' ].append ( value [ 0 ] )


        # Vanilla

        regex     = r'\s{2,4}\b(?!constructor\b|return\b|let\b|this\b|if\b|switch\b|for\b)(\w+)\s*\([^\)]+\)'

        utilities = re.findall ( regex, data )


        for value in utilities:

            if value not in self.template [ 'utilities' ] [ 'names' ]:

                self.template [ 'utilities' ] [ 'names' ].append ( value )

                self.template [ 'utilities' ] [ 'types' ].append ( None  )

    ####    RENDERERS   ########################################################

    def prepare_file    ( self, file ):

        self.output_path = Util.set_file ( file, self.arguments [ 'destination'] )

        open ( self.output_path, 'w+' )


    def compose_header  ( self ):

        header = f"@startuml\n\n"


        if 'skin_param' in self.arguments.keys ( ):

            for skin_param in self.arguments [ 'skin_param' ]:

                header += f"{skin_param}\n"


            header += "\n"


        header += f"class {self.template [ 'class' ]} {{\n"


        self.plantuml_script = header


    def compose_members ( self ):

        members = ''

        pad     = 3

        column_max = Util.get_column_max ( self.template ) + pad


        for tag_type in self.tags:

            if self.template [ tag_type ] [ 'names' ]:

                members += f"{self.tags [ tag_type ]}\n".lstrip (  )


                for i, name in enumerate ( self.template [ tag_type ] [ 'names' ] ):


                    if self.template [ tag_type ] [ 'types' ]:

                        padding  = column_max - len ( name )

                        type     = Util.filter_type ( self.template [ tag_type ] [ 'types' ] [ i ] )

                        members += f"{name}{' ' * padding}{type}\n" if type else f"{name}\n"


        self.plantuml_script += members


    def compose_footer  ( self ):

        self.plantuml_script += f"}}\n\n@enduml"


    def save_output     ( self ):

        with open ( self.output_path, 'w' ) as writer:

            writer.write ( self.plantuml_script )

            print ( ">>  [ output ] \n", f"{self.output_path}" )


    def compose_image   ( self ):

        if 'plant_path' in self.arguments.keys ( ):

            for image_type in self.arguments [ 'make_image' ]:

                output_path = f"{os.path.dirname ( self.output_path )}/images"

                command     = f"java -jar {self.arguments [ 'plant_path' ]} \"{self.output_path}\" -o \"{output_path}\" -{image_type}"

                filename    = os.path.basename ( self.output_path ).replace ( 'txt', image_type )


                if Util.is_directory ( output_path ) is False:

                    os.makedirs ( output_path )


                subprocess.run ( command, shell=True )


                print ( f" {output_path}/{filename}\n" )
