stack = []

def pop(stack):
    if(stack):
        toReturn = stack[-1]
        stack.pop()
        return toReturn

def top(stack):
	if(stack):
		return stack[-1]
    
def push(stack, num):
    stack.append(num)


stack.append(5)
stack.append(10)
stack.append(15)

print(stack)

print(pop(stack))
print(top(stack))

print(stack)