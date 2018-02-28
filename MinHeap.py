class Heap:

	def __init__(self):
		self.arr = []

	def heapify(self, n, i):
		# arr = list to be sorted
		# n = size of tree
		# i = root index
		smallest = i
		left = 2 * i + 1
		right = 2 * i + 2
		# check if left child exists (by checking if index is within range of list) 
		# and is less than root
		if left < n and self.arr[left] < self.arr[i]:
			# if true, set smallest value's index to left child
			smallest = left
		# check if right child exists (by checking if index is within range of list) 
		# and is less than root
		if right < n and self.arr[right] < self.arr[smallest]:
			# if true, set smallest value's index to right child
			smallest = right
		# check if the smallest value is still the root
		if smallest != i:
			# if smallest is not root anymore, switch the values of the root and smallest
			self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
			# check again recursively
			self.heapify(n, smallest)

	def heapsort(self):
		# set n = size of list
		n = len(self.arr)
		# build a heap using the list
		# range(start = n, end = -1 (not inclusive), step = -1)
		for i in range(n, -1, -1):
			# heapify list with every index i
			self.heapify(n, i)
		# iterate through the heap elements
		# range()
		for i in range(n-1, -1, -1):
			# swap node with root
			self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
			# heapify new tree
			self.heapify(i, 0)
		for element in self.arr:
			print(element)

	def insert(self, item):
		self.arr.append(item)


if __name__ == '__main__':
	# [12, 11, 13, 5, 6, 7]
	heap = Heap()
	heap.insert(12)
	heap.insert(11)
	heap.insert(13)
	heap.insert(5)
	heap.insert(6)
	heap.insert(7)
	heap.heapsort()

