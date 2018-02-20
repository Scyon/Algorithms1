class Node:

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None


class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insert_node(data, self.root)

	def insert_node(self, data, node):
		if data < node.data:
			if node.leftChild:
				self.insert_node(data, node.leftChild)
			else:
				node.leftChild = Node(data)
		else:
			if node.rightChild:
				self.insert_node(data, node.rightChild)
			else:
				node.rightChild = Node(data)

	def remove(self, data):
		if self.root:
			self.root = self.remove_node(data, self.root)

	def remove_node(self, data, node):
		if node is None:
		 	return node
		if data < node.data:
			node.leftChild = self.remove_node(data, node.leftChild)
		elif data > node.data:
			node.rightChild = self.remove_node(data, node.rightChild)
		else:
			if not node.rightChild and not node.leftChild:
				print('removing leaf node')
				del node
				return None
			if not node.leftChild:
				print('removing node with single right child')
				tempNode = node.rightChild
				del node
				return tempNode
			elif not node.rightChild:
				print('removing node with single left child')
				tempNode = node.leftChild
				del node
				return tempNode
			print('removing node with two children')
			tempNode = self.get_predecessor(node.leftChild)
			node.data = tempNode.data
			node.leftChild = self.remove_node(tempNode.data, node.leftChild)
		return node

	def get_predecessor(self, node):
		if node.rightChild:
			return self.get_predecessor(node.rightChild)
		return node

	def get_minimum(self):
		if self.node:
			return self.get_min(self.root)

	def get_min(self, node):
		if node.leftChild:
			return self.get_min(node.leftChild)
		return node.data

	def get_maximum(self):
		if self.node:
			return self.get_max(self.root)

	def get_max(self, node):
		if node.rightChild:
			return self.get_max(node.rightChild)
		return node.data

	def traverse(self):
		if self.root:
			self.traverse_in_order(self.root)

	def traverse_in_order(self, node):
		if node.leftChild:
			self.traverse_in_order(node.leftChild)
		print(node.data)
		if node.rightChild:
			self.traverse_in_order(node.rightChild)

if __name__ == '__main__':
	bst = BinarySearchTree()
	bst.insert(3)
	bst.insert(5)
	bst.insert(25)
	bst.insert(23)
	bst.insert(19)
	bst.insert(38)
	bst.traverse()
	print('-' * 50)
	bst.remove(38)
	bst.traverse()
	print('-' * 50)
	bst.insert(12)
	bst.insert(43)
	bst.remove(122)
	bst.traverse()
	print('-' * 50)
