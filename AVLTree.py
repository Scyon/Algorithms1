class Node:

	def __init__(self, data):
		self.data = data
		self.rightChild = None
		self.leftChild = None
		self.height = 0


class AVL:

	def __init__(self):
		self.root = None

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root)

	def traverseInOrder(self, node):
		if node.leftChild:
			self.traverseInOrder(node.leftChild)
		print node.data
		if node.rightChild:
			self.traverseInOrder(node.rightChild)

	def insert(self, data):
		self.root = insertNode(data, self.root)

	def insertNode(self, data, node):
		# perform normal BST insertion
		if not node:
			return Node(data)
		if data < node.data:
			node.leftChild = insertNode(data, node.leftChild)
		if data > node.data:
			node.rightChild = insertNode(data, node.rightChild)
		# after inserting new node, update height of ancestor node
		node.height = 1 + max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild))
		# get the balance factor
		balance = self.calculateBalance(node)
		# case 1 -- left left
		if balance > 1 and data < node.leftChild.data:
			return self.rotateRight(node)
		# case 2 -- left right
		if balance > 1 and data > node.leftChild.data:
			node.leftChild = self.rotateLeft(node.leftChild)
			return self.rotateRight(node)
		# case 3 -- right right
		if balance < -1 and data > node.rightChild:
			return self.rotateLeft(node)
		# case 4 -- right left
		if balance < -1 and data < node.rightChild:
			node.rightChild = self.rotateRight(node.rightChild)
			return self.rotateLeft(node)
		return node

	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root)

	def removeNode(self, data, node):
		if not node:
			return node
		if data < node.data:
			node.leftChild = removeNode(data, node.leftChild)
		elif: data > node.data:
			node.rightChild = removeNode(data, node.rightChild)
		else:
			if not node.rightChild and not node.leftChild:
				del node
				return None
			if not node.rightChild:
				tempNode = node.leftChild
				del node
				return tempNode
			if not node.leftChild:
				tempNode = node.rightChild
				del node
				return tempNode
			tempNode = self.getPredecessor(node.leftChild)
			node.data = tempNode.data
			node.leftChild = self.removeNode(tempNode.data, node.leftChild)
			node.height = 1 + max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild))
			balance = self.calculateBalance(node)
			# case 1 -- left left
			if balance > 1 and self.calculateBalance(node.leftChild) >= 0:
				return self.rotateRight(node)
			# case 2 -- left right
			if balance > 1 and self.calculateBalance(node.leftChild) < 0:
				node.leftChild = self.rotateLeft(node.leftChild)
				return self.rotateRight(node)
			# case 3 -- right right
			if balance < -1 and self.calculateBalance(node.rightChild) < 0:
				return self.rotateLeft(node)
			# case 4 -- right left
			if balance < -1 and self.calculateBalance(node.rightChild) >= 0:
				node.rightChild = self.rotateRight(node.rightChild)
				return self.rotateLeft(node)
			return node

	def getPredecessor(self, node):
		if node.rightChild:
			return self.getPredecessor(node.rightChild)
		return node

	def calculateHeight(self, node):
		if not node:
			return -1
		return node.height

	def calculateBalance(self, node):
		if not node:
			return 0
		return self.calculateHeight(node.leftChild) - self.calculateHeight(node.rightChild)

	def rotateRight(self, node):
		tempLeftChild = node.leftChild
		t = tempLeftChild.rightChild
		#perform rotation
		tempLeftChild.rightChild = node
		node.leftChild = t
		#update heights
		node.height = 1 + max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild))
		tempLeftChild.height = 1 + max(self.calculateHeight(tempLeftChild.leftChild), tempLeftChild.rightChild)
		#return new root
		return tempLeftChild

	def rotateLeft(self, node):
		tempRightChild = node.rightChild
		t = tempRightChild.leftChild
		#perform rotation
		tempRightChild.leftChild = node
		node.rightChild = t
		#update heights
		node.height = 1 + max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild))
		tempRightChild.height = 1 + max(self.calculateHeight(tempRightChild.leftChild), tempRightChild.rightChild)
		#return new root
		return tempRightChild
