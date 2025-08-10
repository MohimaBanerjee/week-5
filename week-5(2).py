class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None
    
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            return -1
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

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
