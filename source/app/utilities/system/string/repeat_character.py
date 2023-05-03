ERROR = -1

def repeat_character ( character, times ):

	#### 	ERROR HABDLING 	################################

	if len ( character ) != 1:

		print ( ' >> [ERROR] repeat_character.py\n\t~ Accepts a single character param only !' )

		return ERROR


	if times < 2 or times == None:

		print ( ' >> [ERROR] repeat_character.py\n\t~ Accepts a times value of above 1 only !' )

		return ERROR

	#### 	LOGIC 	########################################

	return character * times
