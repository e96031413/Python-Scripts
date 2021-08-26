class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		super(Stack, self).__init__()
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		self.stack.pop()

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[-1]

	def is_empty(self):
		if len(self.stack) < 1:
			return "Yes, it's empty"
		return "No, the size is {}".format(stack.size())

	def display(self):
		return self.stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(2)
print(stack.peek())
print(stack.is_empty())
print(stack.display())
stack.pop()
print(stack.display())
stack.pop()
print(stack.display())
stack.pop()
stack.pop()
print(stack.display())
stack.pop()
print(stack.display())
print(stack.is_empty())