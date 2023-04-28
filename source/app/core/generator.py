import os
import re

from utilities.util 					import Util
from utilities.system.file.get_files 	import get_files

class Generator:

	def __init__( self, arguments ):

		#### 	GLOBALS 	################################

		self.arguments   = arguments

		self.files       = [ ]

		self.output_path = None

		self.diagram     = { }

		self.tags = {
	  		'properties': '',
	  		'setters':    '__ Setter __',
	  		'getters':    '__ Getter __',
	  		'utilities':  '__ Utility __'
		}

		#### 	INITIALIZE 	################################

		self.init ( )

	#### 	INITIATORS 	########################################

	def init ( self ):

		self.get_files ( )

		self.compile   ( )

	#### 	GETTERS 	########################################

	def get_files ( self ):

		if ( Util.is_file ( self.arguments [ 'source' ] ) ): 					# If: source is file

			self.files.append ( self.arguments [ 'source' ] )

		elif ( Util.is_directory ( self.arguments [ 'source' ] ) ): 			# If: source is directory

			omissions = self.arguments [ 'omit_files' ] if 'omit_files' in self.arguments.keys ( ) else ''

			self.files = Util.get_files ( self.arguments [ 'source' ], '.js', omissions )

	def compile   ( self ):

		for file in self.files:

			self.process ( file )

			self.render  ( file )

	def process   ( self, file ):

		self.diagram = {
			'class':      None,
			'brief': 	  None,
			'properties': [ ],
			'setters':    [ ],
			'getters':    [ ],
			'utilities':  [ ],
			'master':     None
		}

		self.get_class      ( file )

		self.get_properties ( file )

		self.get_setters    ( file )

		self.get_getters    ( file )

		self.get_utilities  ( file )

	def render    ( self, file ):

		self.prepare_file    ( file )

		self.compose_header  ( )

		self.compose_members ( )

		self.compose_footer  ( )

		self.save_output     ( )

	#### 	GETTERS 	########################################

	def get_header     ( self, file ):

		regex = {
			'header': r'(\/\*\*[^@]+@class[^\/]+\/)',
			'class':  r'@class\s*{.+}\s*(\w+)'
		}

		with open ( file, 'r' ) as reader:

			data = reader.read ( )

			if re.search ( regex [ 'header' ], data ):

				self.diagram [ 'brief' ] = re.search ( regex [ 'header' ], data ).group ( 1 )

				self.diagram [ 'class' ] = re.search ( regex [ 'class'  ], data ).group ( 1 )

	def get_class      ( self, file ):

		self.get_header ( file )


		if self.diagram [ 'class' ] == None:

			with open ( file, 'r' ) as reader:

				data = reader.read ( )

				self.diagram [ 'class' ] = re.search ( r'class\s*(\w+)[^{]+{', data ).group ( 1 )

	def get_properties ( self, file ):

		regex = {
			'docstring': r'@property\s*{(.+)}\s*((\w+)|\[(\w+)=(\w+)\]?)',
			'typical':   r'((#?)\w+)(\s*?)=(\s*?)(((new\s?)\w+)|\w+|\'\w+\'|\"\w+\");'
		}

		#### 	FUNCTIONS 	################################

		def filter_tuples ( list ):

			result = [ ]

			list   = re.findall ( regex [ 'typical' ], ( ' ' ).join ( list ) )


			for entry in list:

				entry = [ entry for entry in entry if entry != ' ' and entry != '' ] [ 0:2 ]


				if entry [ 1 ].isdigit ( ): 						 entry [ 1 ] = 'number'

				if re.search ( r'(\'\w+\'|\"\w+\")', entry [ 1 ] ):  entry [ 1 ] = 'string'

				if re.search ( r'(true|false)', entry [ 1 ] ): 		 entry [ 1 ] = 'boolean'

				if re.search ( r'new ', entry [ 1 ] ): 				 entry [ 1 ] = 'Object'


				result.append ( tuple ( entry ) )


			return result

		#### 	FUNCTIONS 	################################

		if self.diagram [ 'brief' ]:

			list = [ ]

			self.diagram [ 'properties' ] = re.findall ( regex [ 'docstring' ], self.diagram [ 'brief' ] )


			for property in self.diagram [ 'properties' ]:

				list += [ ( property [ 1 ], property [ 0 ] ) ]


			self.diagram [ 'properties' ] = list

		else:

			list = [ ]

			construct = {
				'start': False,
				'open':  False
			}

			for i, line in enumerate ( open ( file, 'r' ).readlines ( ) ):

				if re.search ( r'class\s*\w+', line ):

					construct [ 'start' ] = True

					continue


				if construct [ 'start' ] is True  and \
				   construct [ 'open'  ] is False and \
				   line.find ( '{' ):

					construct [ 'open' ] = True


				if re.search ( r'\s{2,4}constructor\s*\(',  line ) or \
				   re.search ( r'\s{2,4}set\s*\w+(\s*?)\(', line ) or \
				   re.search ( r'\s{2,4}get\s*\w+(\s*?)\(', line ):

					break


				if construct [ 'open' ]:

					list.append ( line )


			self.diagram [ 'properties' ] = filter_tuples ( list )

	def get_setters    ( self, file ):

		regex = {
			'docstring': r'@param\s*\{(\w+)\}[^\/]+\/[^s]+set\s(\w+)',
			'typical':   r'\s{2,4}set(\s*)(\w+)\s*\([^\)]+\)'
		}

		data  = open ( file, 'r' ).read ( )


		self.diagram [ 'setters' ] = re.findall ( regex [ 'docstring' ], data )

		self.diagram [ 'setters' ] = [ tuple[::-1] for tuple in self.diagram [ 'setters' ] ]


		if not self.diagram [ 'setters' ]:

			list = [ ]


			self.diagram [ 'setters' ] = re.findall ( regex [ 'typical' ], data )


			for tuple in self.diagram [ 'setters' ]:

				list.append ( tuple [ 1 ] )


			self.diagram [ 'setters' ] = list

	def get_getters    ( self, file ):

		regex = {
			'docstring': r'@return\s*{(\w+)}[^\/]+\/[^g]+get\s(\w+)',
			'typical':   r'\s{2,4}get(\s*)(\w+)\s*\([^\)]+\)'
		}

		data  = open ( file, 'r' ).read ( )


		self.diagram [ 'getters' ] = re.findall ( regex [ 'docstring' ], data )

		self.diagram [ 'getters' ] = [ tuple[::-1] for tuple in self.diagram [ 'getters' ] ]


		if not self.diagram [ 'getters' ]:

			list = [ ]


			self.diagram [ 'getters' ] = re.findall ( regex [ 'typical' ], data )


			for tuple in self.diagram [ 'getters' ]:

				list.append ( tuple [ 1 ] )


			self.diagram [ 'getters' ] = list

	def get_utilities  ( self, file ):

		list  = [ ]

		temp  = [ ]

		regex = {
			'docstring': r'@return\s*{(\w+)}[^\/]+\/\s*\b(?!return\b|let\b|this\b|if\b|switch\b|for\b)(\w+)\s*\([^\)]+\)',
			'typical':   r'\s{2,4}\b(?!constructor\b|return\b|let\b|this\b|if\b|switch\b|for\b)(\w+)\s*\([^\)]+\)'
		}

		list  = re.findall ( regex [ 'docstring' ], open ( file, 'r' ).read ( ) )

		temp  = re.findall ( regex [ 'typical'   ], open ( file, 'r' ).read ( ) )


		if list:

			list = [ tuple[::-1] for tuple in list ]


		if len ( temp ) > len ( list ):

			for i in range ( len ( list ), -1, -1 ):

				try:

					if list [ i ] [ 0 ] == temp [ i ]:

						del temp [ i ]

				except IndexError:

					pass


		self.diagram [ 'utilities' ] = ( list + temp )

	#### 	RENDERERS 	########################################

	def prepare_file    ( self, file ):

		if re.search ( r'\w.+\.txt', self.arguments [ 'destination' ] ):

			directory = os.path.dirname ( self.arguments [ 'destination' ] )

			self.output_path = f"{self.arguments [ 'destination' ]}"


			if Util.is_directory ( directory ) is False:

				os.makedirs ( directory )

		else:

			filename = os.path.basename ( file ).split ( '/' ) [ -1 ].replace ( '.js', '' )

			self.output_path = f"{self.arguments [ 'destination' ]}/{filename}.txt"


			if Util.is_directory ( self.arguments [ 'destination' ] ) is False:

				os.makedirs ( self.arguments [ 'destination' ] )


		open ( self.output_path, 'w+' )

	def compose_header  ( self ):

		data = f"@startuml\n\n"


		if 'skin_param' in self.arguments.keys ( ):

			for skin in self.arguments [ 'skin_param' ]:

				data += f"{skin}\n"

			data += "\n"


		data += f"class {self.diagram [ 'class' ]} {{"


		self.diagram [ 'master' ] = data

	def compose_members ( self ):

		data = ''


		for tag in self.tags:

			if self.diagram [ tag ]:

				data += f"{self.tags [ tag ]}\n"

				grid = Util.entry_padding ( self.diagram [ tag ] )


				for i, entry in enumerate ( self.diagram [ tag ] ):

					if isinstance ( entry, tuple ):

						spacing = Util.repeat_character ( ' ', grid [ i ] )

						if entry [ 1 ] == 'number'  or \
						   entry [ 1 ] == 'string'  or \
						   entry [ 1 ] == 'boolean' or \
						   entry [ 1 ] == 'Object':

							data += f"{entry [ 0 ]}{spacing}<color:gray>{{{entry [ 1 ]}}}</color>\n"

						else:

							data += f"{entry [ 0 ]}{spacing}{{{entry [ 1 ]}}}\n"

					else:

						data += f"{entry}\n"


		self.diagram [ 'master' ] += data

	def compose_footer  ( self ):

		self.diagram [ 'master' ] += f"}}\n@enduml"

	def save_output     ( self ):

		with open ( self.output_path, 'w' ) as writer:

			writer.write ( self.diagram [ 'master' ] )

			print ( ">>  [ output ] \n", f"{self.output_path}\n" )
