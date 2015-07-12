def generate_series(number,determinant=None):
	my_list = []
	a,b = 0,1
	my_list.append(a)
	if type(number) is int:
		limiter = number - 1
		if number < 2:
			#print "fibonacci series can not have less than two numbers"
			return -1
		for i in range(0,limiter):
			a,b = b,a+b
			my_list.append(a)
		#print "List of a fibonacci sequence of {0} numbers is: {1}".format(number,my_list)
		return my_list		
	else:
		print"Your input is not supported"
		return -1

def generate_series_sum(number,determinant=None):
	
	if type(number) is int:
		my_list = [0,1]
		new_list =[]
		if determinant == "even":
			
			while len(new_list) < number:
				holder = get_next_item(my_list)
				my_list.append(holder)
				if holder % 2 == 0:
					new_list.append(holder)
			return new_list
			return sum_list(new_list)
				
		elif determinant == "odd":
			while len(new_list) < number:
				holder = get_next_item(my_list)
				my_list.append(holder)
				if holder % 2 != 0:
					new_list.append(holder)
			return new_list
			return sum_list(new_list)
				

		elif determinant is None:
			my_list = generate_series(number)
			return sum_list(my_list)
		else:
			return -1
		
	else:
		return -1

def get_next_item(number):
	last_item = len(number) - 1
	gen_item = number[last_item] + number[last_item-1]
	return gen_item

def sum_list(my_list):
	series_sum = 0
	for num in my_list:
		if type(num) != int:
			return "Not a list of integers"
		series_sum += num
	return series_sum


#num = int(raw_input("Enter a number:"))

#print generate_series(num)
#print generate_series_sum(num,"odd")

