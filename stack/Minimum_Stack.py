class MinStack:
    def __init__(self):
        self.stack=[]
        self.MinStack=[]
    def push(self, val: int) -> None:
        if len (self.MinStack)>0:
            self.MinStack.append(min(val,(self.MinStack[-1])))
        else:
            self.MinStack.append(val)
        self.stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()
    def top(self) -> int:
        return (self.stack[-1])
    def getMin(self) -> int:
        return (self.MinStack[-1])
        