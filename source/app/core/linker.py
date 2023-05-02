import os
import re
import subprocess

from utilities.util 						import Util

class Linker:

	def __init__( self, arguments ):

		#### 	GLOBALS 	################################

		self.file         = ''

		self.files        = [ ]

		self.files_linked = { }

		self.arguments    = arguments

		self.classes      = [ ]

		self.objects      = [ ]

		self.regexes      = [ ]

		#### 	INITIALIZE 	################################

		self.init ( )

	#### 	INITIATORS 	########################################

	def init ( self ):

		self.get_files ( )

		self.process   ( )

	#### 	GETTERS 	########################################

	def get_files     ( self ):

		for ( root, dirs, file ) in os.walk ( self.arguments [ 'destination' ] ):

			for entry in file:

				if '.txt' in entry:

					if '-linked.txt' not in entry:

						self.files.append ( f"{root}/{entry}" )

	def process       ( self ):

		for file in self.files:

			self.read_file   ( file )

			self.match_files ( )

	def read_file     ( self, file ):

		self.file    = file

		data 	     = open ( file, 'r' ).read ( )

		self.objects = set ( re.findall ( r'(\w+)\s{2,}\{([^\}]+)\}', data ) )

	def match_files   ( self ):

		self.find_files    ( )

		self.match_objects ( )

		self.link_objects  ( )

	def find_files    ( self ):

		self.regexes = [ ]


		if self.objects:

			for object in self.objects:

				regex = ''

				object = object [ 1 ]

				object_lo, object_up = object.lower ( ), object.upper ( )


				for i in range ( len ( object ) ):

					regex += f'[{object_lo [ i ]}|{object_up [ i ]}]'


				regex = f'({regex})'


				self.regexes.append ( regex )

	def match_objects ( self ):

		self.classes = [ ]


		if self.files:

			for file in self.files:

				for regex in self.regexes:

					filename = re.findall ( regex, file )


					if filename:

						source = f"{self.arguments [ 'destination' ]}/{filename [ 0 ]}.txt"


						if source == file:

							self.classes.append ( source )

	def link_objects  ( self ):

		#### 	GLOBALS 	################################

		links  = [ ]

		file   = self.file.replace ( '.txt', '-linked.txt' )

		data   = open ( self.file, 'r' ).read ( )

		header = re.findall ( r'class\s*([^\s]+)\s*', data ) [ 0 ]

		#### 	FUNCTIONS 	################################

		def assemble_links ( data ):

			for object in self.objects:

				links.append ( f"{header} *-- {object [ 1 ]}" )


			links.append ( '@enduml\n' )

			data = data.replace ( '@enduml', '\n'.join ( links ) )


			for entry in self.classes:

				CLASS_UML = open ( entry, 'r' ).read ( )

				data     += f'\n{CLASS_UML}\n'


			data = re.sub ( r'@enduml\s*@startuml', '', data )


			with open ( file, 'w' ) as writer:

				writer.write ( data )


			print ( '>> [ output ]\n', file )

		def compose_image  ( file ):

			if 'plant_path' in self.arguments.keys ( ):

				for image_type in self.arguments [ 'make_image' ]:

					output_path = f"{os.path.dirname ( file )}/images"

					command     = f"java -jar {self.arguments [ 'plant_path' ]} \"{file}\" -o \"{output_path}\" -{image_type}"

					filename    = os.path.basename ( file ).replace ( 'txt', image_type )


					if Util.is_directory ( output_path ) is False:

						os.makedirs ( output_path )


					subprocess.run ( command, shell=True )


					print ( f" {output_path}/{filename}\n" )

		#### 	LOGIC	 	################################

		assemble_links ( data )

		compose_image  ( file )
