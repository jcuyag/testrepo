import unittest



class TestSpider(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass


	def test_method(self):
		print "this is testing only"

	def test_method_two(self):
		self.assertEqual(2, 2)

	def test_method_three(self):
		self.assertNotEqual(2, 7)

if __name__ == '__main__':
	unittest.main()
