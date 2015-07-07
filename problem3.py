the_pass = open('password.txt','r')
def valid_pass(many_pass):
	kount_pas = 0
	for this_pass in many_pass:
		digs = get_dig(this_pass)
		lows = get_low(this_pass)
		ups = get_high(this_pass)
		if digs == True and lows == True and ups == True:
			kount_pas +=1
	print ("Password.txt has {0} valid passwords".format(kount_pas)) 


		


def get_dig(one_pass):
	#checks for digits and returns true if they are up to 4
	kount_digit = 0
	for xters in one_pass:
		if xters.isdigit() == True:
			kount_digit +=1
	if kount_digit > 3:
		return True
	return False


def get_low(one_pass):
	#checks for lower case alphabets and returns true if they are up to 2
	kount_lower = 0
	for xters in one_pass:
		if xters.islower() == True:
			kount_lower +=1
	if kount_lower > 1:
		return True
	return False

def get_high(one_pass):
	#checks for upper case alphabets and returns true if they are up to 4
	kount_higher = 0
	for xters in one_pass:
		if xters.isupper() == True:
			kount_higher +=1
	if kount_higher > 3:
		return True
	return False
valid_pass(the_pass)