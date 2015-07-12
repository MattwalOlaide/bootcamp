class BinarySearch(list):
	def __init__(self,a,b):
		data = range(0,a,b)
		super(BinarySearch,self).__init__(data)
		self.length = a

	def search(self,number):
		count  = 0
		#my_list = self
		#print my_list
		first  = 0
		self.length = len(self)
		last  = self.length - 1
		obj_location = {'count':'','index':''}
		while first <= last:
			count += 1
			mid_point = (first + last) // 2
			if self[first] == number:
				index = first
				obj_location["count"] = count
				obj_location["index"] = index
				return obj_location
			elif self[last] == number:
				index = last
				obj_location["count"] = count
				obj_location["index"] = index
				return obj_location
			elif self[mid_point] == number:
				index = mid_point
				obj_location["count"] = count
				obj_location["index"] = index
				return obj_location
			else:
				if last % 2 == 0:
					if self[mid_point] > number:
						last = mid_point
					else:
						first = mid_point
				else:
					if self[mid_point] > number:
						last = mid_point - 1
					else:
						first = mid_point + 1
		return False
#nw = BinarySearch(27,3)
#print nw
#print nw.search(9)
#print nw.length