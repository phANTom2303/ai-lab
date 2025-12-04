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


def isBracket(c):
    if(c == '{' or c == '(' or c == '[' or c == '}' or c == ')' or c == ']'):
        return True
    else:
        return None
    
def getBracketPair(c):
    if(c == ')'):
        return '('
    elif(c == '}'):
        return '{'
    else:
        return '['

expression = input("Enter a bracket sequence : ")
st = Stack([])
possible = True
for c in expression:
    if(not isBracket(c)):
        continue
    else:
        if(c == '(' or c == '{' or c == '['):
            st.push(c)
        else:
            last = st.top()
            if(last != getBracketPair(c)):
                possible = False
                break
            else:
                st.pop()

if(possible and st.isEmpty()):
    print("Balanced Brackets.")
else:
    print("Unbalanced Brackets.")