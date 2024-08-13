import os
import re
import subprocess

from utilities.util 						import Util

class Linker:

	def __init__( self, arguments ):

		#### 	GLOBALS 	################################

		self.arguments    = arguments

		self.file         = ''

		self.files        = [ ]

		self.files_linked = { }

		########################################

		self.classSources = [ ]

		self.objects      = [ ]

		self.regexes      = [ ]

		####    INITIALIZATION    ##########################

		self.init ( )

	####    INITIATORS  ########################################################

	def init    ( self ):

		self.get_files ( )

		self.process   ( )


	def process ( self ):

		for file in self.files:

			self.get_objects ( file )

			self.match_files ( )

	####    GETTERS     ########################################################

	def get_files   ( self ):

		for ( root, dirs, file ) in os.walk ( f"{self.arguments [ 'destination' ]}/text" ):

			for entry in file:

				if '.txt' in entry:

					if '-linked.txt' not in entry:

						self.files.append ( f"{root}/{entry}" )


	def get_objects ( self, file ):

		self.objects = [ ] 									# clear self.objects


		data       = open ( file, 'r' ).read ( )

		objects    = re.findall ( r'(\w+)\s{2,}\{([^\}]+)\}', data )

		arrow_type = r'.<([^>]+)>'


		for object in objects: 								# Filter objects

			object_type = re.search ( arrow_type, object [ 1 ] )


			if object_type:

				object_type = object_type.group ( 1 );

			else:

				object_type = object [ 1 ];


			if object_type not in self.objects:

				self.objects.append ( object_type )


		if self.objects: 									# If objects, store present file

			self.file = file


	def get_classes ( self ):

		self.classSources = [ ] 							# clear self.classSources


		if self.files:

			for regex in self.regexes:

				if '|||' in regex:

					regex = regex.replace ( '|||', '|' )


				files = ''.join ( self.files )

				file  = re.search ( regex, files )


				if file:

					file   = file.group ( 0 ).lstrip ( '/' )

					source = f"{self.arguments [ 'destination' ]}/text/{file}"

					self.classSources.append ( source )

	####    SETTERS     ########################################################

	def set_regexes ( self ):

		self.regexes = [ ] 									# clear self.regexes

		arrow_type   = r'.<([^>]+)>'


		if self.objects:

			for object in self.objects:

				regex   = ''

				arrowed = re.search ( arrow_type, object )


				if arrowed:

					group = arrowed.group ( 1 );

					group = re.sub ( r'.+<([^>]+)>', r'\1', group )

					object_lo, object_up = group.lower ( ), group.upper ( )

				else:

					object_lo, object_up = object.lower ( ), object.upper ( )



				for i in range ( len ( object_lo ) ):

					regex += f'[{object_lo [ i ]}|{object_up [ i ]}]'



				self.regexes.append ( f"\/{regex}\.txt" )

	####    UTILITIES   ########################################################

	def match_files  ( self ):

		self.set_regexes ( )

		self.get_classes ( )

		self.link_objects  ( )


	def link_objects ( self ):

		links = [ ]


		if self.classSources:

			destination = f"{self.arguments [ 'destination' ]}/text/linked"

			filename    = os.path.basename ( self.file ).replace ( '.txt', '-linked.txt' )

			data        = open ( self.file, 'r' ).read ( )

			thisClass   = re.findall ( r'class\s*([^\s]+)\s*', data ) [ 0 ]


			for object in self.objects:

				linked_object = object


				if '|' in object:

					linked_object = linked_object.replace ( '|', ' : ' )


				if '<' in object:

					linked_object = re.sub ( r'.+<([^>]+)>', r'\1', object )


				links.append ( f"{thisClass} o-- {linked_object}" )


			data = data.replace ( '@enduml', '\n'.join ( links ) ) + '\n\n@enduml'


			for classSource in self.classSources:

				CLASS_UML = open ( classSource, 'r' ).read ( )

				data     += f'\n{CLASS_UML}\n'


			data = re.sub ( r'@enduml\s*@startuml', '', data ) 					# clean penultimate '@enduml' tags

			file = Util.set_file ( filename.rstrip ( '.txt' ), destination )


			with open ( file, 'w' ) as writer: 									# write file

				writer.write ( data )

				print ( '>> [ output ] Linker\n', file )


			if 'plant_path' in self.arguments.keys ( ):

				self.compose_image ( destination )

	####    RENDERERS   ########################################################

	def compose_image ( self, file ):

		for image_type in self.arguments [ 'make_image' ]:

			output_path = f"{self.arguments [ 'destination' ]}/image/linked"

			command     = f"java -jar {self.arguments [ 'plant_path' ]} \"{file}\" -o \"{output_path}\" -{image_type}"

			filename    = os.path.basename ( self.file ).replace ( '.txt', f"-linked.{image_type}" )


			if Util.is_directory ( output_path ) is False:

				os.makedirs ( output_path )


			subprocess.run ( command, shell=True )


			print ( f" {output_path}/{filename}\n" )
