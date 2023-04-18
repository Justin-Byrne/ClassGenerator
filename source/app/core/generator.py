class ClassGenerator:

	def __init__( self, arguments ):

		#### 	GLOBALS 	################################

		# code ...

		#### 	INITIALIZE 	################################

		# init ...

	#### 	CLEANUP 	########################################

	def cleanup_properties ( self ):

		result = self.create_2d_list ( len ( self.diagram [ 'properties' ] ) )

		prop   = [ ]

		i      = 0


		for property in self.diagram [ 'properties' ]:

			property = property [ 0:2 ] 										# Trim: property


			if property [ 0 ] == 'HTMLCanvasElement': 							# Replace: 'HTMLCanvasElement' -> 'HTMLCE'

				prop       = list ( property )

				prop [ 0 ] = 'HTMLCE'

				property   = tuple ( prop )


			if re.search ( self.regex [ 'default' ], property [ 1 ] ): 			# Locate: Default values & modify

				temp = re.search ( self.regex [ 'default' ], property [ 1 ] )

				prop       = list ( property )

				prop [ 1 ] = f"{temp [ 1 ]}[<color:orangered>{temp [ 2 ]}</color>]"

				property   = tuple ( prop )


			result [ i ] = list ( property )

			i += 1


		self.diagram [ 'properties' ] = result 									# Populate: properties in diagram

	def cleanup_extras ( self ):

		self.diagram [ 'extra' ] = [ x for x in self.diagram [ 'extra' ] if x != [] ]

	#### 	INITIATORS 	########################################

	def remove_elements ( self ):

		self.remove_class  ( )

		self.remove_member ( 'properties' )

		self.remove_member ( 'setters' )

		self.remove_member ( 'getters' )

		self.remove_extras ( )

	def render_elements ( self ):

		self.render_header ( )

		self.render_member ( 'properties' )

		self.render_member ( 'setters' )

		self.render_member ( 'getters' )

		self.render_extras ( )

		self.render_footer ( )

	#### 	REMOVERS 	########################################

	def remove_class ( self ):

		with open ( self.file, 'r' ) as reader:

			data   = reader.read ( )

			header = re.search ( self.regex [ 'header' ], data ).group ( 1 )

			self.diagram [   'class'    ] = re.search  ( self.regex [   'class'    ], data ).group ( 1 )

	def remove_member ( self, member ):

		with open ( self.file, 'r' ) as reader:

			data = reader.read ( )

			self.diagram [ member ] = re.findall ( self.regex [ member ], data )


			if member == 'properties':

				self.diagram [ member ] = self.diagram [ member ] [ 0:int ( len ( self.diagram [ member ] ) / 2 ) ]

	def remove_extras ( self ):

		with open ( self.file, 'r' ) as reader:

			amount = len ( re.findall ( self.regex [ 'extras' ], reader.read ( ) ) ) - 1


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