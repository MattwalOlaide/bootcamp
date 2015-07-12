'''	Test cases for the series

'''
"""
	check n for in both functions:
	float
	alphabet
	negative
	int

	check second generate sum condition if its:
	even
	odd
	alphabet
	float
	negative
	int
"""
import unittest, problem4
class FiboTest(unittest.TestCase):
	def testFloatSeries(self):
		self.assertEqual(problem4.generate_series(2.5),-1,msg="You can not get a fibonacci series")
	def testAlphabetSeries(self):
		self.assertEqual(problem4.generate_series('abd'),-1,msg="fibonacci series of a string? Joker!")
	def testNegativeSeries(self):
		self.assertEqual(problem4.generate_series(-2),-1,msg="Lol! Dear unlearned prof. please remember that fibonacci starts @ zero.")
	def testIntegerSeries(self):
		self.assertEqual(problem4.generate_series(4),[0,1,1,2],msg="Chairman! Are you Mr Abaga?")
	def testSingleNumberSeries(self):
		self.assertEqual(problem4.generate_series(1),-1,msg="Uhn?")
	#for sums alone without even or odd determinant
	def testFloatSum(self):
		self.assertEqual(problem4.generate_series_sum(2.5,determinant = None),-1,msg="Hey! no such sums.")
	def testAlphabetSum(self):
		self.assertEqual(problem4.generate_series_sum('aab',determinant = None),-1,msg="Hey! no such sums.")
	def testNegativeSum(self):
		self.assertEqual(problem4.generate_series_sum(-4,determinant = None),-1,msg="Hey! no such sums.")
	def testIntegerSum(self):
		self.assertEqual(problem4.generate_series_sum(2,determinant = None),1,msg="cool")

	#for sums alone without even or odd determinant
	def testFloatDet(self):
		self.assertEqual(problem4.generate_series_sum(2.5,2.5),-1,msg="Fat Error! Ahahahahahha.")
	def testAlphabetDet(self):
		self.assertEqual(problem4.generate_series_sum('aab','determinant'),-1,msg="Fat Error! Ahahahahahha.")
	def testNegativeDet(self):
		self.assertEqual(problem4.generate_series_sum(-4,-1),-1,msg="Fat Error! Ahahahahahha.")
	def testIntegerEven(self):
		self.assertEqual(problem4.generate_series_sum(2,determinant="even"),10,msg="cool")
	def testIntegerOdd(self):
		self.assertEqual(problem4.generate_series_sum(2,determinant="odd"),2,msg="cool")
	
	
if __name__ == '__main__':
	unittest.main()


	
	