class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []  # Stack to keep track of operations for undo

    def append(self, string):
        self.history.append(self.text)  # Save current state for undo
        self.text += string

    def delete(self, k):
        self.history.append(self.text)  # Save current state for undo
        self.text = self.text[:-k]  # Delete last k characters

    def print_char(self, k):
        if 1 <= k <= len(self.text):
            print(self.text[k - 1])  # Print the k-th character (1-based index)

    def undo(self):
        if self.history:
            self.text = self.history.pop()  # Revert to the last state

def main():
    editor = TextEditor()
    n = int(input())  # Number of operations

    for _ in range(n):
        operation = input().strip().split()
        op_type = int(operation[0])

        if op_type == 1:  # Append operation
            editor.append(operation[1])
        elif op_type == 2:  # Delete operation
            editor.delete(int(operation[1]))
        elif op_type == 3:  # Print operation
            editor.print_char(int(operation[1]))
        elif op_type == 4:  # Undo operation
            editor.undo()

if __name__ == "__main__":
    main()
