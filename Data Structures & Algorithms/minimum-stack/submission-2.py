class MinStack:

    def __init__(self):
        # stack -> python list
        # stack_min -> python list min
        self.stack = []
        self.min_stack = []

        # stack = [1]
        # stack_min = [1]

        # stack = [1, 2]
        # stack_min = [1]

        # stack = [1, 2, 0]
        # stack_min = [1, 0]

        # return getmin 0

        # stack = [1, 2]
        # stack_min = [1]

        # return top 2

        # return getmin 1

    def push(self, val: int) -> None:
        # list.append() -> O(1)
        # list_min.append() if val <= list_min.top()
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # list.pop() -> O(1)
        # list_min.pop() -> O(1)
        top = self.top()
        self.stack.pop()
        if top == self.getMin():
            self.min_stack.pop()
        

    def top(self) -> int:
        # return list[len()] -> O(1)
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        # iterate list find min -> O(n)
        # we need O(1)

        # return list_min[len()] -> O(1)
        return self.min_stack[len(self.min_stack) - 1]
        
