# module5_call.py
from module5_mod import NumberProcessor

def main():
    """Main function to execute the program flow."""
    processor = NumberProcessor()

    # Step 1: Read the integer N (positive integer)
    N = int(input("Enter a positive integer N: "))

    # Step 2: Read N numbers
    processor.read_numbers(N)

    # Step 3: Read X (number to find)
    X = int(input("Enter the integer X to search: "))

    # Step 4: Find and print the result
    result = processor.find_number(X)
    print(result)

if __name__ == "__main__":
    main()
