ERROR = -1

def repeat_character ( character, times ):

	#### 	ERROR HABDLING 	################################

	if len ( character ) != 1:

		print ( 'repeat_character.py accepts a single character param only !' )

		return ERROR


	if times < 2 or times == None:

		print ( 'repeat_character.py accepts a times value of above 1 only !')

		return ERROR

	#### 	LOGIC 	########################################

	return character * times
