class Node:

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None
		self.height = 0

class AVL:

	def __init__(self):
		self.root = None

	def insert(self, data):
		self.root = insert_node(data, self.root)

	def traverse(self):
		if self.root:
			self.traverse_in_order(self.root)

	def traverse_in_order(self, node):
		if node.leftChild:
			self.traverse_in_order(node.leftChild)
		print node.data
		if node.rightChild:
			self.traverse_in_order(node.rightChild)

	def insert_node(self, data, node):
		if not node:
			return Node(data)
		if data < node.data:
			node.leftChild = self.insert_node(data, node.leftChild)
		else:
			node.rightChild = self.insert_node(data, node.rightChild)
		node.height = max(self.calculate_height(node.rightChild), self.calculate_height(node.leftChild)) + 1
		return self.settle_violations(data, node)

	def settle_violations(self, data, node):
		balance = self.calculate_balance(node)
		# case 1 --> left left heavy situation
		if balance > 1 and data < node.leftChild.data:
			return self.rotate_right(node)
		# case 2 --> right right heavy situation
		if balance < -1 and data > node.rightChild.data:
			return self.rotate_left(node)
		# case 3 --> left right heavy situation
		if balance > 1 and data > node.leftChild.data:
			node.leftChild = self.rotate_left(node.leftChild)
			return self.rotate_right(node)
		# case 4 --> right left heavy situation
		if balance < -1 and data < node.rightChild.data:
			node.rightChild = self.rotate_right(node.rotate_right)
			return self.rotate_left(node)
		return node

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
		node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1
		balance = self.calculate_balance(node)
		#doubly left heavy
		if balance > 1 and self.calculate_balance(node.leftChild) >= 0:
			return self.rotate_right(node)
		#left right case
		if balance > 1 and self.calculate_balance(node.leftChild) < 0:
			node.leftChild = self.rotate_left(node.leftChild)
			return self.rotate_right(node)
		#doubly right heavy
		if balance < -1 and self.calculate_balance(node.rightChild) <= 0:
			return self.rotate_left(node)
		#right left case
		if balance < -1 and self.calculate_balance(node.rightChild) > 0:
			node.rightChild = self.rotate_right(node.rightChild)
			return self.rotate_left(node)
		return node

	def get_predecessor(self, node):
		if node.rightChild:
			return self.get_predecessor(node.rightChild)
		return node

	def calculate_height(self, node):
		if not node:
			return -1
		return node.height

	def calculate_balance(self, node):
		if not node:
			return 0
		return self.calculate_height(node.leftChild) - self.calculate_height(node.rightChild)

	def rotate_right(self, node):
		print('Rotating right on node {}'.format(node.data))
		tempLeftChild = node.leftChild
		t = tempLeftChild.rightChild
		tempLeftChild.rightChild = node
		node.leftChild = t
		node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1
		tempLeftChild.height = max(self.calculate_height(tempLeftChild.leftChild), self.calculate_height(tempLeftChild.rightChild)) + 1
		return tempLeftChild

	def rotate_left(self, node):
		print('Rotating right on node {}'.format(node.data))
		tempRightChild = node.rightChild
		t = tempRightChild.leftChild
		tempRightChild.leftChild = node
		node.rightChild = t
		node.height = max(self.calculate_height(node.leftChild), self.calculate_height(node.rightChild)) + 1
		tempRightChild.height = max(self.calculate_height(tempRightChild.leftChild), self.calculate_height(tempRightChild.rightChild)) + 1
		return tempRightChild

