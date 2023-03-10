'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

# problem is getting min value with O(1) rest operations are anyway O(1)
# keep track of min value at each point a value is added to stack
# need to create another stack called minstack which will have another 

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        # check if min stack is empty
        if self.minstack:
            # if minstack is not empty then compare values to get min value
            minval = min(val, self.minstack[-1])
        else:
            # else current value is the min value
            minval = val
        self.minstack.append(minval)
    
    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minstack[-1]