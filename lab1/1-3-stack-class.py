class Stack:
    def __init__(self, stack):
        self.stack = []
        
    def isEmpty(self):
        if(len(self.stack) == 0):
            return True 
        else:
            return False
    
    def top(self):
        if(not self.isEmpty()):
            return self.stack[-1]
        else:
            return None
    
    def push(self, num):
        self.stack.append(num)
    
    def pop(self):
        if(not self.isEmpty()):
            self.stack.pop()
    
    def display(self):
        print(self.stack)
        

st = Stack([])
st.push(5)
st.display()
st.pop()
st.display()
st.push(10)
st.push(19)
st.display()
print(st.top())