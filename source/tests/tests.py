import sys
import os
import unittest
from os.path import dirname, abspath

# APPEND PARENT 'SOURCE' PATH TO SYS.PATH
sys.path.append ( dirname ( dirname ( abspath( '.' ) ) ) )

# IMPORTING DEVELOPER FUNCTIONS
from source.app.utilities.util import Util

WDIR  = f"{os.getcwd ( )}/cases"
FILE  = f"{WDIR}/test-file.txt"
FLAG  = "-f"
DIRE  = f"{WDIR}"

ERROR = -1

class TestUtil ( unittest.TestCase ):

	#### 	SYSTEM 	########################################

	# VALIDATION

	def test_is_directory     ( self ): 						# 01

		self.assertTrue  ( Util.is_directory ( DIRE ) )

		self.assertFalse ( Util.is_directory ( f"{DIRE}/testtesttest" ) )

	def test_is_file          ( self ): 						# 02

		self.assertTrue  ( Util.is_file ( FILE         ) )

		self.assertFalse ( Util.is_file ( DIRE         ) )

		self.assertTrue  ( Util.is_file ( FILE, '.txt' ) )

		self.assertFalse ( Util.is_file ( FILE, 'txt'  ) )

	def test_is_flag          ( self ): 						# 03

		self.assertTrue  ( Util.is_flag ( FLAG ) )

		self.assertFalse ( Util.is_flag ( '#f' ) )

	# COMMAND

	def test_get_command_type ( self ): 						# 04

		self.assertEqual ( Util.get_command_type ( FLAG ), 'flag'      )

		self.assertEqual ( Util.get_command_type ( FILE ), 'file'      )

		self.assertEqual ( Util.get_command_type ( DIRE ), 'directory' )

	def test_get_commands     ( self ): 						# 05

		amount   = 20

		commands = [ [ ] for i in range ( amount ) ]
		results  = [ [ ] for i in range ( amount ) ]

		commands [  0 ] = [ '0', FLAG ]
		commands [  1 ] = [ '0', DIRE ]
		commands [  2 ] = [ '0', FLAG, DIRE ]
		commands [  3 ] = [ '0', DIRE, DIRE ]
		commands [  4 ] = [ '0', FLAG, DIRE, DIRE ]
		commands [  5 ] = [ '0', DIRE, FLAG, DIRE ]
		commands [  6 ] = [ '0', DIRE, DIRE, FLAG ]

		# results  [  0 ] = {'flag': FLAG, 'source': None, 'destination': None}
		results  [  0 ] = ERROR
		results  [  1 ] = {'flag': None, 'source': DIRE, 'destination': DIRE}
		results  [  2 ] = {'flag': FLAG, 'source': DIRE, 'destination': DIRE}
		results  [  3 ] = {'flag': None, 'source': DIRE, 'destination': DIRE}
		results  [  4 ] = {'flag': FLAG, 'source': DIRE, 'destination': DIRE}
		results  [  5 ] = {'flag': FLAG, 'source': DIRE, 'destination': DIRE}
		results  [  6 ] = {'flag': FLAG, 'source': DIRE, 'destination': DIRE}

		commands [  7 ] = [ '0', FLAG, FILE ]
		commands [  8 ] = [ '0', FILE, DIRE ]
		commands [  9 ] = [ '0', FILE, FILE ]
		commands [ 10 ] = [ '0', DIRE, FILE ] 				# << ERROR: DIRECTORY TO SINGLE FILE

		results  [  7 ] = {'flag': FLAG, 'source': FILE, 'destination': DIRE}
		results  [  8 ] = {'flag': None, 'source': FILE, 'destination': DIRE}
		results  [  9 ] = {'flag': None, 'source': FILE, 'destination': FILE}
		# results  [ 10 ] = {'flag': None, 'source': DIRE, 'destination': FILE}
		results  [ 10 ] = ERROR

		commands [ 11 ] = [ '0', FLAG, FILE, DIRE ]
		commands [ 12 ] = [ '0', FLAG, FILE, FILE ]
		commands [ 13 ] = [ '0', FLAG, DIRE, FILE ] 		# << ERROR: DIRECTORY TO SINGLE FILE

		results  [ 11 ] = {'flag': FLAG, 'source': FILE, 'destination': DIRE}
		results  [ 12 ] = {'flag': FLAG, 'source': FILE, 'destination': FILE}
		# results  [ 13 ] = {'flag': FLAG, 'source': DIRE, 'destination': FILE}
		results  [ 13 ] = ERROR

		commands [ 14 ] = [ '0', FILE, FLAG, DIRE ]
		commands [ 15 ] = [ '0', FILE, FLAG, FILE ]
		commands [ 16 ] = [ '0', DIRE, FLAG, FILE ] 		# << ERROR: DIRECTORY TO SINGLE FILE

		results  [ 14 ] = {'flag': FLAG, 'source': FILE, 'destination': DIRE}
		results  [ 15 ] = {'flag': FLAG, 'source': FILE, 'destination': FILE}
		# results  [ 16 ] = {'flag': FLAG, 'source': DIRE, 'destination': FILE}
		results  [ 16 ] = ERROR

		commands [ 17 ] = [ '0', FILE, DIRE, FLAG ]
		commands [ 18 ] = [ '0', FILE, FILE, FLAG ]
		commands [ 19 ] = [ '0', DIRE, FILE, FLAG ] 		# << ERROR: DIRECTORY TO SINGLE FILE

		results  [ 17 ] = {'flag': FLAG, 'source': FILE, 'destination': DIRE}
		results  [ 18 ] = {'flag': FLAG, 'source': FILE, 'destination': FILE}
		# results  [ 19 ] = {'flag': FLAG, 'source': DIRE, 'destination': FILE}
		results  [ 19 ] = ERROR


		for i in range ( amount ):

			message = f"\n\n\t>> Test: {i}\n\tcommands: {commands [ i ]}\n\tresults:  {results [ i ]}\n"

			self.assertEqual ( Util.get_commands ( commands [ i ] ), results [ i ], message )

	# FILE

	def test_get_eof 		  ( self ): 						# 06

		self.assertEqual ( Util.get_eof ( f"{WDIR}/test.txt" ), ERROR )

		self.assertEqual ( Util.get_eof ( FILE ), 7 )

	# STRING

	def test_repeat_character ( self ): 						# 07

		self.assertEqual ( Util.repeat_character ( 'A',  1 ), ERROR )
		self.assertEqual ( Util.repeat_character ( 'AA', 1 ), ERROR )
		self.assertEqual ( Util.repeat_character ( 'AA'    ), ERROR )

		self.assertEqual ( Util.repeat_character ( 'A', 2 ), 'AA'   )
		self.assertEqual ( Util.repeat_character ( 'b', 3 ), 'bbb'  )
		self.assertEqual ( Util.repeat_character ( ' ', 4 ), '    ' )

	# LIST

	def test_create_2d_list   ( self ): 						# 08

		self.assertEqual ( Util.create_2d_list ( 0 ), ERROR )

		self.assertEqual ( Util.create_2d_list ( 1 ), [ [ ] ] )
		self.assertEqual ( Util.create_2d_list ( 2 ), [ [ ], [ ] ] )
		self.assertEqual ( Util.create_2d_list ( 3 ), [ [ ], [ ], [ ] ] )

	def test_entry_padding    ( self ): 						# 09

		props = [
			( 'prop',      'number'      ),
			( 'property',  'string'      ),
			( 'element',   'HTMLElement' ),
			( 'something', 'Something'   ),
			( 'x',         'number'      ),
			( 'y',         'number'      )
		]

		self.assertEqual ( Util.entry_padding ( props ), [8, 4, 5, 3, 11, 11] )

		self.assertEqual ( Util.entry_padding ( props, 0 ), ERROR )

		self.assertEqual ( Util.entry_padding ( props, 10, 2 ), ERROR )

	def test_list_to_string   ( self ): 						# 10

		self.assertEqual ( Util.list_to_string ( [ 'one' ] ), 'one' )

		self.assertEqual ( Util.list_to_string ( [ 'one', 'two' ] ), 'one two' )

		self.assertEqual ( Util.list_to_string ( [ 'one', 'two', 'three' ] ), 'one two three' )

	#### 	CUSTOM 	########################################

	# VALIDATION

	def test_is_extension     ( self ): 						# 11

		lines = [
			'////    TITLE 01    ////',
		    '////    TITLE 02    ////',
		    '////    ONE TWO     ////',
		    '////    THREE FOUR FIVE 	////',
		    '////    SIX SEVEN EIGHT NINE TEN 	////',
		    '////    VALIDATION  ////',
		    '////    UTILITIES   ////',
		    '////    SPECIAL 	////'
		]

		extension_titles = [
			'TITLE 01',
		    'TITLE 02',
		    'ONE TWO',
		    'THREE FOUR FIVE',
		    'SIX SEVEN EIGHT NINE TEN',
		    'VALIDATION',
		    'UTILITIES',
		    'SPECIAL'
		]

		for line in lines:

			self.assertTrue  ( Util.is_extension ( line, extension_titles ) )
			self.assertFalse ( Util.is_extension ( line, f"extension_titlesA" ) )

	def test_is_js_class      ( self ): 						# 12

		files = [
			'cases/source/class.js',
			'cases/source/class-ext.js',
			'cases/source/class-ext-docstring.js'
		]

		for file in files:

			self.assertTrue ( Util.is_js_class ( file ) )

	# CLEANUP

	def test_clean_properties ( self ): 						# 13

		props = [
			( 'number',        '[prop1=25]', '',        'prop1', '25' ),
			( 'string',        'prop0',      'prop0',   '',      ''   ),
			( 'boolean',       'active',     'active',  '',      ''   ),
			( 'Special',       'special',    'special', '',      ''   ),
			( 'CustomObject',  'object0',    'object0', '',      ''   ),
			( 'SpecialObject', 'object1',    'object1', '',      ''   ),
			( 'HTMLElement',   'element',    'element', '',      ''   )
		]

		subs = [
			( 'CustomObject',  'CO'   ),
			( 'SpecialObject', 'SO'   ),
			( 'HTMLElement',   'HTMLE')
		]

		result = [
			['number', 'prop1=[<color:orangered>25</color>]'],
			['string', 'prop0'],
			['boolean', 'active'],
			['Special', 'special'],
			['CO', 'object0'],
			['SO', 'object1'],
			['HTMLE', 'element']
		]

		self.assertEqual ( Util.clean_properties ( props, subs ), result )

		pass


# TEST MAIN
if __name__ == '__main__':

	unittest.main ( )
