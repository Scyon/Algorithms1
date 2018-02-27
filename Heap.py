class Heap:

	def __init__(self):
		self.arr = []

	def heapify(self, n, i):
		# arr = list to be sorted
		# n = size of tree
		# i = root index
		largest = i
		left = 2 * i + 1
		right = 2 * i + 2
		# check if left child exists and is greater than root
		if left < n and self.arr[left] > self.arr[i]:
			# if true, set largest value's index to left child
			largest = left
		# check if right child exists and is greater than root
		if right < n and self.arr[right] > self.arr[largest]:
			# if true, set largest value's index to right child
			largest = right
		# check if the largest value is still the root
		if largest != i:
			# if largest is not root anymore, switch the values of the root and largest
			self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
			# check again recursively
			self.heapify(n, largest)

	def heapsort(self):
		# set n = size of list
		n = len(self.arr)
		# build a heap using the list
		# range(start = n, end = -1 (not inclusive), step = -1)
		for i in range(n-1, -1, -1):
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
	heap = Heap()
	arr = [12, 11, 13, 5, 6, 7]
	heap.insert(12)
	heap.insert(11)
	heap.insert(13)
	heap.insert(5)
	heap.insert(6)
	heap.insert(7)
	heap.heapsort()

