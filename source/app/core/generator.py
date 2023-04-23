import os
import re

from utilities.util 					import Util
from utilities.system.file.get_files 	import get_files

def view_arguments ( arguments ):

	print ( '-' * 100 )

	print ( "Flag: \t\t",      arguments [ 'flag'        ] )

	print ( "Source: \t",      arguments [ 'source'      ] )

	print ( "Destination: \t", arguments [ 'destination' ] )

	print ( '. ' * 50 )

	for i, argument in enumerate ( arguments ):

		print ( f"{i}: ", argument )

	print ( '-' * 100 )

def view_files ( files ):

	print ( '-' * 100 )

	print ( '>>> FILES' )

	for file in files:

		print ( file )

	print ( '-' * 100 )

class Generator:

	def __init__( self, arguments ):

		#### 	GLOBALS 	################################

		self.arguments = arguments

		self.files     = [ ]

		self.doc_brief = None

		self.diagram = {
			'class':      None,
			'properties': [ ],
			'setters':    [ ],
			'getters':    [ ],
			'extra':      [ ],
			'master':     None
		}

		self.tags    = {
      		'start':      '@startuml',
	  		'properties': '',
	  		'setters':    '__ Setter __',
	  		'getters':    '__ Getter __',
	  		'end':        '@enduml'
		}

		#### 	INITIALIZE 	################################

		view_arguments ( arguments )

		self.init ( )

	#### 	INITIATORS 	########################################

	def init ( self ):

		self.get_files  ( )

		self.load_files ( )

	#### 	GETTERS 	########################################

	def get_files ( self ):

		if ( Util.is_file ( self.arguments [ 'source' ] ) ): 					# If: source is file

			self.files.append ( self.arguments [ 'source' ] )

		elif ( Util.is_directory ( self.arguments [ 'source' ] ) ): 			# If: source is directory

			self.files = Util.get_files ( self.arguments [ 'source' ], '.js', self.arguments [ 'omit_files' ] if 'omit_files' in self.arguments.keys ( ) else '' )

	def load_files ( self ):

		for file in self.files:

			self.process ( file )

	def process ( self, file ):

		# print ( ">>> processing \n", file )

		self.get_class   ( file )

		self.get_members ( file )

	#### 	GETTERS 	########################################

	def get_header     ( self, file ):

		regex = {
			'header': r'(\/\*\*[^@]+@class[^\/]+\/)',
			'class':  r'@class\s*{.+}\s*(\w+)'
		}

		with open ( file, 'r' ) as reader:

			data = reader.read ( )

			if re.search ( regex [ 'header' ], data ):

				self.doc_brief = re.search ( regex [ 'header' ], data ).group ( 1 )

				self.diagram   [ 'class'  ] = re.search ( regex [ 'class'  ], data ).group ( 1 )

	def get_class      ( self, file ):

		self.get_header ( file )


		if self.diagram [ 'class' ] is None:

			with open ( file, 'r' ) as reader:

				data = reader.read ( )

				self.diagram [ 'class' ] = re.search ( r'class\s*(\w+)[^{]+{', data ).group ( 1 )

	def get_members    ( self, file ):

		self.get_properties ( file )

		# for line in self.diagram [ 'properties' ]: print ( line )

		self.get_setters    ( file )

		# for line in self.diagram [ 'setters' ]: print ( line )

		self.get_getters    ( file )

		# for line in self.diagram [ 'getters' ]: print ( line )

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

		if self.doc_brief:

			list = [ ]

			self.diagram [ 'properties' ] = re.findall ( regex [ 'docstring' ], self.doc_brief )


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

	# ........................................................ #

	def get_extras ( self, file ):

		with open ( file, 'r' ) as reader:

			amount = len ( re.findall ( regex [ 'extras' ], reader.read ( ) ) ) - 1


		self.diagram [ 'extra' ] = self.create_2d_list ( amount )

		extra = [ ]


		with open ( self.file, 'r' ) as reader:

			lines = reader.readlines ( );

			for line in lines:

				self.counters.line += 1


				if re.search ( self.regex [ 'extras' ], line ):

					if self.omit_types ( line, self.extras_to_ignore, 'extras' ):

						continue


					if ( len ( extra ) > 1 ):

						self.diagram [ 'extra' ] [ self.counters.count ] = extra

						self.counters.count += 1

						extra = [ ]


					extra.append ( line )

				else:

					if ( len ( extra ) > 0 ):

						extra.append ( line )


				if self.counters.line > self.counters.EOF:

					self.diagram [ 'extra' ] [ self.counters.count ] = extra


		self.cleanup_extras ( )

	#### 	RENDERERS 	########################################

	def render_header ( self ):

		diagram  = f"{self.tags [ 'start' ]}\n\n"

		diagram += "left to right direction\n"


		if len ( self.skinparam ) > 0:

			for param in self.skinparam:

				diagram += f"skinparam {param}\n"


		diagram += f"\nclass {self.diagram [ 'class' ]} {{"


		self.diagram [ 'master' ] = diagram

	def render_member ( self, member ):

		diagram = f"{self.tags [ member ]}\n"

		grid    = self.grid_spacing ( self.diagram [ member ] )

		padding = 3

		i       = 0


		for entry in self.diagram [ member ]:

			length  = ( max ( grid ) + padding ) - grid [ i ]

			spacing = self.repeat_character ( ' ', length )


			if entry [ 0 ] == 'number' or entry [ 0 ] == 'string' or entry [ 0 ] == 'boolean':

				diagram += f"{entry [ 1 ]}{spacing}<color:gray>{{{entry [ 0 ]}}}</color>\n"

			else:

				diagram += f"{entry [ 1 ]}{spacing}{{{entry [ 0 ]}}}\n"


			i += 1


		self.diagram [ 'master' ] += diagram

	def render_extras ( self ):

		diagram = ''

		padding = 3


		for i in range ( len ( self.diagram [ 'extra' ] ) ):

			extra_title  = re.search ( self.regex [ 'extras' ], self.diagram [ 'extra' ] [ i ] [ 0 ] ).group ( 1 )

			diagram     += f"__ {extra_title} __\n"


			if extra_title == 'PRIVATE':

				methods = re.findall ( self.regex [ 'private' ], '\n'.join ( self.diagram [ 'extra' ] [ i ] ) )

			else:

				methods = re.findall ( self.regex [ 'methods' ], '\n'.join ( self.diagram [ 'extra' ] [ i ] ) )


			for method in methods:

				diagram += f"{method}\n"


		self.diagram [ 'master' ] += diagram

	def render_footer ( self ):

		self.diagram [ 'master' ] += f"}}\n@enduml"

	def render_output ( self ):

		file = re.findall ( r'(\w+)\.js', self.file )

		output_directory = f"../docs/PlantUml/raw/_originals/{file [ 0 ]}.txt"

		with open ( output_directory, 'w' ) as writer:

			writer.write ( self.diagram [ 'master' ] )

			print ( '>>  [ output ] ', output_directory )
