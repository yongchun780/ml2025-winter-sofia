# module5_mod.py

class NumberProcessor:
    def __init__(self):
        """Initialize an empty list to store numbers."""
        self.numbers = []

    def read_numbers(self, N):
        """Reads N numbers from user input and stores them in a list."""
        print(f"Enter {N} numbers:")
        for i in range(1, N + 1):
            num = int(input(f"Number {i}: "))
            self.numbers.append(num)

    def find_number(self, X):
        """Finds the index (1-based) of X in the list or returns -1 if not found."""
        if X in self.numbers:
            return self.numbers.index(X) + 1  # Convert 0-based to 1-based index
        else:
            return -1
