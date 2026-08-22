class MinStack:
    # get min : store a minimum value that gets updated whenever a new number is added
    # however, this number can also be deleted due to pop, so need to store a history of min numbers 
    # we only need to store 2 previous, if the number being removed is the minimum, we replace the current minimum with the old minimum

    def __init__(self):
        self.stack = []
        self.minimums = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimums) > 0:
            if val <= self.minimums[-1]:
                self.minimums.append(val)
        else:
            self.minimums.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minimums[-1]:
            self.minimums.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
