class Node:

	def __init__(self, data):
		self.data = data
		self.rightChild = None
		self.leftChild = None


class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self, data):
		# check if root exists
		if not self.root:
			# if root does not exist, set new node as root
			self.root = Node(data)
		else:
			# root exists --> call method to insert node
			self.root = insertNode(data, self.root)

	def insertNode(self, data, node):
		# check if data is in left branch
		if data < node.data:
			# check if node has a leftchild
			if node.leftChild:
				# node is in left branch --> call method again with leftchild this time
				node.leftChild = insertNode(data, node.leftChild)
			# node does not have leftchild --> create node
			else:
				node.leftChild = Node(data)
		# check if data is in right branch
		elif data > node.data:
			# check if node has a rightchild
			if node.rightChild:
				# node is in right branch --> call method again with rightchild this time
				node.rightChild = insertNode(data, node.rightChild)
			# node does not have rightchild --> create node
			else:
				node.rightChild = Node(data)
		return node

	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root)

	def removeNode(self, data, node)
		# base case for recursion --> simply checks if node exists in tree
		# if not then return node and do not modify tree
		if not node:
			return node
		# check if data is in left branch
		if data < node.data:
			node.leftChild = self.removeNode(data, node.leftChild)
		# check if data is in right branch
		elif data > node.data:
			node.rightChild = self.removeNode(data, node.rightChild)
		# we have found the node to be removed
		else:
			# case 1 --> node is a leaf node
			if not node.rightChild and not node.leftChild:
				del node
				return None
			# case 2 --> node with single leftchild
			elif not node.rightChild:
				tempNode = node.leftChild
				del Node
				return tempNode
			# case 3 --> node with single rightchild
			elif not node.leftChild:
				tempNode = node.rightChild
				del node
				return tempNode
			# case 4 --> node with two children
			# get predecessor
			tempNode = self.getPredecessor(node.leftChild)
			# set node to predecessor
			node.data = tempNode.data
			# delete predecessor recursively, we know it is in left branch
			# and we know that it satisfies case 1 or 2 which we can deal with
			node.leftChild = self.removeNode(tempNode.data, node.leftChild)
		return node

	def getPredecessor(self, node):
		# check if given node has a rightchild
		if node.rightChild:
			# if so, call function recursively to return next rightchild
			return self.getPredecessor(node.rightChild)
		return node

	def traverse(self):
		if self.root:
			traverseInOrder(self.root)

	def traverseInOrder(self, node):
		if self.leftChild:
			self.traverseInOrder(node.leftChild)
		print(node.data)
		if self.rightChild:
			self.traverseInOrder(node.rightChild)

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
