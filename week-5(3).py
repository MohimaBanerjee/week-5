def isBalanced(s):
    # Dictionary to hold matching pairs of brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []
    
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the topmost element from the stack if it's not empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped bracket matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return "NO"
        else:
            # If it's an opening bracket, push onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched; otherwise, they were not
    return "YES" if not stack else "NO"

# Input reading
if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        result = isBalanced(s)
        print(result)
