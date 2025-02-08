# module4.py

# Step 1: Read the integer N (positive integer)
N = int(input("Enter a positive integer N: "))

# Step 2: Read N numbers one by one
numbers = []
for i in range(1, N + 1):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

# Step 3: Read the integer X
X = int(input("Enter the integer X to search: "))

# Step 4: Find X in the list and output the result
if X in numbers:
    print(numbers.index(X) + 1)  # Output the index (1-based)
else:
    print("-1")  # Output -1 if X is not found

