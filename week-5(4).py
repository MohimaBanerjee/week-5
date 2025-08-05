def infix_to_postfix(infix_exp):
    """
    Convert infix expression to postfix expression using Shunting Yard algorithm
    """
    # Precedence dictionary (higher number means higher precedence)
    precedence = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
    
    # Stack for operators and output list
    stack = []
    output = []
    
    for char in infix_exp:
        # If character is operand, add to output
        if char.isalpha() or char.isdigit():
            output.append(char)
        
        # If character is '(', push to stack
        elif char == '(':
            stack.append(char)
        
        # If character is ')', pop from stack until '('
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from stack
        
        # If character is operator
        else:
            # Pop operators with higher or equal precedence
            while (stack and stack[-1] != '(' and 
                   precedence[char] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(char)
    
    # Pop remaining operators from stack
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# Test cases
test_cases = [
    ("a+b*(c^d-e)^(f+g*h)-i", "abcd^e-fgh*+^*+i-"),
    ("A*(B+C)/D", "ABC+*D/"),
    ("(a+b)*(c+d)", "ab+cd+*"),
    ("a+b*c-d/e^f", "abc*+def^/-"),
    ("K+L-M*N+(O^P)*W/U/V*T+Q", "KL+MN*-OP^W*U/V/T*+Q+")
]

print("Infix to Postfix Conversion Results:")
print("-" * 50)
for infix, expected in test_cases:
    result = infix_to_postfix(infix)
    print(f"Infix: {infix:<25} => Postfix: {result}")
    print(f"Expected: {expected:<23} {'✓' if result == expected else '✗'}")
    print("-" * 50)
