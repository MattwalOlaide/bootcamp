def generate_series(number):
	my_list = []
	a,b = 0,1
	my_list.append(a)
	if type(number) is int:
		limiter = number - 1
		for i in range(0,limiter):
			a,b = b,a+b
			my_list.append(a)
		print "List of a fibonacci sequence of {0} numbers is: {1}".format(number,my_list)
		return my_list
	else:
		print"not supported"
		return -1
def generate_series_sum(number,determinant=None):
	if type(number) is int:
		my_list = generate_series(number)
		if determinant is None:
			series_sum = 0
			for num in my_list:
				series_sum += num
			print "Sum of a fibonacci sequence of {0} numbers is: {1}".format(number,series_sum)
		elif determinant=="even":
			get_even_num(number,my_list)
			#print "The sum of the first {0} even numbers in a fibonacci sequence is: {1}",format(number,numbers_sum)
			
		elif determinant=="odd":
			pass
		else:
			return -1
	else:
		return -1


def get_even_num(number,my_list):
	kount = 0
	even_nums = []
	for num in my_list:
		if num % 2 == 0:
			kount +=1
			even_nums.append(num)
			if kount >= number:
				sumNumbers(even_nums,number)
			else:
				new_limit = number + 1
				generate_series(new_limit)


def sumNumbers(another_list,number):
	kount = 0
	numbers_sum = 0
	while kount < number:
		even_num = another_list[kount]
		numbers_sum += even_num
	print  "The sum of the first {0} even numbers in a fibonacci sequence is: {1}",format(number,numbers_sum)



num = int(raw_input("Enter a number:"))

generate_series(num)
generate_series_sum(num,"even")

