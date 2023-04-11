import sys
import unittest

# SETTING PARENT PATH
sys.path.append ( '..' )

# IMPORTING DEVELOPER FUNCTIONS
from app.utilities.util import Util

FILE = "/Users/test.txt"
FLAG = "-f"
DIRE = "/Users"

class TestUtil ( unittest.TestCase ):

	def test_is_directory ( self ):

		self.assertTrue  ( Util.is_directory ( DIRE ) )

		self.assertFalse ( Util.is_directory ( f"{DIRE}/testtesttest" ) )

	def test_is_file      ( self ):

		self.assertTrue  ( Util.is_file ( FILE         ) )

		self.assertFalse ( Util.is_file ( DIRE         ) )

		self.assertTrue  ( Util.is_file ( FILE, '.txt' ) )

		self.assertFalse ( Util.is_file ( FILE, 'txt'  ) )

	def test_is_flag      ( self ):

		self.assertTrue  ( Util.is_flag ( FLAG ) )

		self.assertFalse ( Util.is_flag ( '#f' ) )

	def test_get_command  ( self ):

		self.assertEqual ( Util.get_command_type ( FLAG ), 'flag'      )

		self.assertEqual ( Util.get_command_type ( FILE ), 'file'      )

		self.assertEqual ( Util.get_command_type ( DIRE ), 'directory' )

	def test_get_commands ( self ):

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
		results  [  0 ] = -1
		results  [  1 ] = {'flag': None, 'source': DIRE, 'destination': None}
		results  [  2 ] = {'flag': FLAG, 'source': DIRE, 'destination': None}
		results  [  3 ] = {'flag': None, 'source': DIRE, 'destination': DIRE}
		results  [  4 ] = {'flag': FLAG, 'source': DIRE, 'destination': DIRE}
		results  [  5 ] = {'flag': FLAG, 'source': DIRE, 'destination': DIRE}
		results  [  6 ] = {'flag': FLAG, 'source': DIRE, 'destination': DIRE}

		commands [  7 ] = [ '0', FLAG, FILE ]
		commands [  8 ] = [ '0', FILE, DIRE ]
		commands [  9 ] = [ '0', FILE, FILE ]
		commands [ 10 ] = [ '0', DIRE, FILE ] 				# << ERROR: DIRECTORY TO SINGLE FILE

		results  [  7 ] = {'flag': FLAG, 'source': FILE, 'destination': None}
		results  [  8 ] = {'flag': None, 'source': FILE, 'destination': DIRE}
		results  [  9 ] = {'flag': None, 'source': FILE, 'destination': FILE}
		# results  [ 10 ] = {'flag': None, 'source': DIRE, 'destination': FILE}
		results  [ 10 ] = -1

		commands [ 11 ] = [ '0', FLAG, FILE, DIRE ]
		commands [ 12 ] = [ '0', FLAG, FILE, FILE ]
		commands [ 13 ] = [ '0', FLAG, DIRE, FILE ] 		# << ERROR: DIRECTORY TO SINGLE FILE

		results  [ 11 ] = {'flag': FLAG, 'source': FILE, 'destination': DIRE}
		results  [ 12 ] = {'flag': FLAG, 'source': FILE, 'destination': FILE}
		# results  [ 13 ] = {'flag': FLAG, 'source': DIRE, 'destination': FILE}
		results  [ 13 ] = -1

		commands [ 14 ] = [ '0', FILE, FLAG, DIRE ]
		commands [ 15 ] = [ '0', FILE, FLAG, FILE ]
		commands [ 16 ] = [ '0', DIRE, FLAG, FILE ] 		# << ERROR: DIRECTORY TO SINGLE FILE

		results  [ 14 ] = {'flag': FLAG, 'source': FILE, 'destination': DIRE}
		results  [ 15 ] = {'flag': FLAG, 'source': FILE, 'destination': FILE}
		# results  [ 16 ] = {'flag': FLAG, 'source': DIRE, 'destination': FILE}
		results  [ 16 ] = -1

		commands [ 17 ] = [ '0', FILE, DIRE, FLAG ]
		commands [ 18 ] = [ '0', FILE, FILE, FLAG ]
		commands [ 19 ] = [ '0', DIRE, FILE, FLAG ] 		# << ERROR: DIRECTORY TO SINGLE FILE

		results  [ 17 ] = {'flag': FLAG, 'source': FILE, 'destination': DIRE}
		results  [ 18 ] = {'flag': FLAG, 'source': FILE, 'destination': FILE}
		# results  [ 19 ] = {'flag': FLAG, 'source': DIRE, 'destination': FILE}
		results  [ 19 ] = -1


		for i in range ( amount ):

			message = f" >> Test: {i}\ncommands: {commands [ i ]}\nresults:  {results [ i ]}\n"

			self.assertEqual ( Util.get_commands ( commands [ i ] ), results [ i ], message )


# TEST MAIN
if __name__ == '__main__':

	unittest.main ( )
