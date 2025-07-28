import numpy as np

def get_matrix(name):
    print(f"Enter the elements of matrix {name} row-wise (3x3):")
    elements = []
    for i in range(3):
        while True:
            row_input = input(f"Row {i+1} (3 numbers separated by spaces): ")
            row = row_input.strip().split()
            if len(row) != 3:
                print("Please enter exactly 3 numbers.")
                continue
            try:
                row = [float(x) for x in row]
                elements.append(row)
                break
            except ValueError:
                print("Please enter valid numbers.")
    return np.array(elements)

def main():
    A = get_matrix("A")
    B = get_matrix("B")

    # Scalar input
    while True:
        scalar_input = input("Enter a scalar value for scalar multiplication: ")
        try:
            scalar = float(scalar_input)
            break
        except ValueError:
            print("Please enter a valid number.")

    print("\nMatrix A:\n", A)
    print("\nMatrix B:\n", B)

    # a) Addition
    add = A + B
    print("\n(a) Addition (A + B):\n", add)

    # b) Subtraction
    sub = A - B
    print("\n(b) Subtraction (A - B):\n", sub)

    # c) Multiplication (matrix product)
    mul = np.dot(A, B)
    print("\n(c) Multiplication (A * B):\n", mul)

    # d) Scalar multiplication
    scalar_mul = scalar * A
    print(f"\n(d) Scalar multiplication ({scalar} * A):\n", scalar_mul)

    # e) Transpose of A
    transpose = A.T
    print("\n(e) Transpose of A:\n", transpose)

if __name__ == "__main__":
    main()

