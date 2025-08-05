class MyStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

def process_operations(operations):
    my_stack = MyStack()
    results = []
    
    for op in operations:
        if op[0] == 1:  # Push operation
            my_stack.push(op[1])
        elif op[0] == 2:  # Pop operation
            results.append(my_stack.pop())
    
    return results

# Example usage
if __name__ == "__main__":
    # Input: list of operations
    oper = [[1, 2], [1, 3], [2], [1, 4], [2]]  # Corresponds to the operations
    output = process_operations(oper)
    print(output)  # Output: [3, 4]
