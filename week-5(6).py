def calculate_span(prices):
    n = len(prices)
    span = [0] * n  # Initialize the span array
    stack = []  # Stack to store indices of the prices

    for i in range(n):
        # Calculate span for prices[i]
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()  # Pop elements from the stack that are less than or equal to prices[i]
        
        # If stack is empty, it means prices[i] is greater than all previous prices
        if not stack:
            span[i] = i + 1  # Span is the index + 1
        else:
            span[i] = i - stack[-1]  # Span is the difference between current index and index of last higher price
        
        stack.append(i)  # Push current index onto the stack

    return span

# Example usage:
arr1 = [100, 80, 60, 70, 60, 75, 85]
print(calculate_span(arr1))  # Output: [1, 1, 1, 2, 1, 4, 6]

arr2 = [10, 4, 5, 90, 120, 80]
print(calculate_span(arr2))  # Output: [1, 1, 2, 4, 5, 1]
