class Stack:

	def __init__(self):
		self.stack = []

	def is_empty(self)
		return self.stack == []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def stack_size(self):
		return len(self.stack)

if __name__ == '__main__':
	stack = Stack()
	stack.push(1)
	stack.push(4)
	stack.push(5)
