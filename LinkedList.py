class Node:

	def __init__(self, data):
		self.data = data
		self.nextNode = None


class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	def insert_start(self, data):
		self.size = self.size + 1
		newNode = Node(data)
		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

	def remove(self, data):
		if self.head is None:
			return
		self.size = self.size - 1
		currentNode = self.head
		previousNode = None
		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode
		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode

	def list_size(self):
		return self.size

	def insert_end(self, data):
		self.size = self.size + 1
		newNode = Node(data)
		actualNode = self.head
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode
		actualNode.nextNode = newNode

	def traverse_list(self):
		actualNode = self.head
		while actualNode is not None:
			print(actualNode.data)
			actualNode = actualNode.nextNode

if __name__ == '__main__':
	linkedList = LinkedList()
	linkedList.insert_start(12)
	linkedList.insert_start(13)
	linkedList.insert_end(14)
	linkedList.traverse_list()
	print(linkedList.list_size())