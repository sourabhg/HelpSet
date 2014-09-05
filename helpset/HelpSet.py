class HelpSet:
	elements = []

	# Create a Set
	def __init__(self,values=None):
		if values != None:
			if not self.checkDuplicates(values):
				self.elements = values
			else:
				self.elements = self.removeDuplicates(values)


	# Display a Set
	def listSet(self):
		return self.elements

	# Add a element to a set
	def add(self,member):	
		if member not in self.elements:
			self.elements.append(member)
		else:
			print 'Duplicates not allowed in set'
		return self.elements

	def delete(self):
		self.elements = []
		return self.elements

	# Add multiple elements to a set
	def addAll(self,members):
		for m in members:
			self.add(members[m])
		return self.elements

	# Check duplicates in a sets
	def checkDuplicates(self,values):
		dups = [x for x in values if values.count(x) > 1]
		if not dups:
			return False
		else:
			return True

	def removeDuplicates(self,values):
		res = []
		for i in values:
			if i not in res:
				res.append(i)

		return res
	
	# Make union of two sets
	def union(self,helpset):
		return self.removeDuplicates(self.elements + helpset.elements)

	# Get Common elements from two sets
	def intersect(self,helpset):
		return [x for x in self.elements if x in helpset.elements]

	def difference(self,helpset):
		return [x for x in self.elements if x not in helpset.elements]

	def cardinality(self):
		return len(self.elements)

	def remove(self,member):
		return self.elements.pop(member,None)