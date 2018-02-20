class Queue:

	def __init__(self):
		self.queue = []

	def is_empty(self):
		return self.queue == []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self, data):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def queue_size(self):
		return len(self.queue)

if __name__ == "__main__":
	queue = Queue()
	queue.enqueue(3)
	queue.enqueue(5)
	queue.peek()