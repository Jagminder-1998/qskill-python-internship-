import numpy as np

def get_matrix(rows, cols, name):
    print(f"\nEnter values for Matrix {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i+1} values separated by space: ").split()))
        matrix.append(row)
    return np.array(matrix)

def main():
    print("Matrix Operations Tool")
    print("----------------------")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix_a = get_matrix(rows, cols, "A")
    matrix_b = get_matrix(rows, cols, "B")

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("\nResult (A + B):")
        print(matrix_a + matrix_b)

    elif choice == 2:
        print("\nResult (A - B):")
        print(matrix_a - matrix_b)

    elif choice == 3:
        print("\nResult (A x B):")
        print(np.dot(matrix_a, matrix_b))

    elif choice == 4:
        print("\nTranspose of Matrix A:")
        print(matrix_a.T)

    elif choice == 5:
        if rows == cols:
            print("\nDeterminant of Matrix A:")
            print(np.linalg.det(matrix_a))
        else:
            print("\nDeterminant can only be calculated for square matrices.")

    else:
        print("\nInvalid choice.")

if __name__ == "__main__":
    main()
