class HashTable(object):

	def __init__(self):
		self.size = 10
		self.keys = [None] * self.size
		self.values = [None] * self.size
			
	def put(self, key, data):
		index = self.hashfunction(key)
		# if key at given index is not None, there is a collision
		while self.keys[index] is not None:	
			if self.keys[index] == key:
				self.values[index] = data # update
				return
			# rehash to find another slot
			index = (index+1)%self.size
		# insert key and value
		self.keys[index] = key
		self.values[index] = data
	
	def get(self, key):
		index = self.hashfunction(key)
		while self.keys[index] is not None:
			if self.keys[index] == key:
				return self.values[index]
			index = (index+1)%self.size
		# key is not present in the associative array
		return None

	def hashfunction(self, key): 
		sum = 0
		for letter in key:
			# ord() returns unicode representation of character
			sum = sum + ord(letter)
		# returns remainder when divided by the size of the HashTable
		return sum%self.size


if __name__ == "__main__":
	table = HashTable()	
	table.put("apple",10)
	table.put("orange",20)
	table.put("car",30)
	table.put("table",40)
	print(table.get("cara"))
