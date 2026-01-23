class stack():
    def __init__ (self, items, size): #Initialises the constructor
        self.items = items #Passes 2 attributes items & size
        self.size = size

    def push(self, data): # Push adds data to the array
        self.items.append(data)
        return(self.items)

    def pop(self): # Pop removes the top item of the stack.
        return(self.items.pop())

    def isEmpty(self): # Checks if the stack is empty & returns true/false
        return(not bool (self.items))

    def isFull(self): # Checks if the stack is full and returns true / false
        length = len(self.items)
        if length >= self.size:
            return(True)
        else:
            return(False)

    def get_size(self): # Returns the size of the stack
        return(len(self.items))

    def peek(self): # Returns the top item of the stack.
        return(self.items[-1])

s1 = stack([], 10)

print(s1.push("a"))
print(s1.push("b"))
print(s1.push("c"))

print(s1.pop())

print(s1.isEmpty())

print(s1.isFull())

print(s1.get_size())

print(s1.peek())
