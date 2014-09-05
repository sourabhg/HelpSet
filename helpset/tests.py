import unittest
from HelpSet import HelpSet

class HelpSetTests(unittest.TestCase):
	hs = HelpSet()
	hs1 = HelpSet(['23','45','11','123'])
	hs2 = HelpSet(['17','45','11','11'])
	hs4 = HelpSet(['17','45','11','11'])
	def testCreate(self):
		#Asserting creation of empty set
		self.assertEqual(self.hs.elements,[])
		#Asserting creation of set with elements
		self.assertEqual(self.hs1.elements,['23','45','11','123'])
		#Asserting creation when a elements are duplicate in input
		self.assertEqual(self.hs2.elements,['17','45','11'])

	def testDelete(self):
		self.assertEqual(self.hs4.delete(),[])

	def testUnion(self):
		self.assertEqual(self.hs1.union(self.hs2),['23','45','11','123','17'])

	def testIntersect(self):
		self.assertEqual(self.hs1.intersect(self.hs2),['45','11'])

	def testDifference(self):
		self.assertEqual(self.hs1.difference(self.hs2),['23','123'])

	def testAddMember(self):
		self.assertEqual(self.hs4.add('34'),['17','45','11','34'])

	def testCardinality(self):
		self.assertEqual(self.hs4.cardinality(),4)

if __name__== '__main__':
	unittest.main()
