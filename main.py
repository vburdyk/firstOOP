def input_matrix():
    columns = int(input("Enter the number of columns: "))
    rows = int(input("Enter the number of rows: "))

    matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            el = int(input(f"Enter elements [{i}][{j}]: "))
            row.append(el)
        matrix.append(row)

    return matrix


def multiplication_digit(matrix1):
    digit = int(input("Enter a number for multiply matrix: "))

    result_matrix = [[element * digit for element in row] for row in matrix1]

    return result_matrix


def add_matrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrix are not the same!")

    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)

    return result_matrix


def deduction_matrix(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrix are not the same!")

    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result_matrix.append(row)

    return result_matrix


def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Num of columns in matrix1 should be same with num of rows in matrix2")

    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            res = 0
            for g in range(len(matrix2)):
                res += matrix1[i][g] * matrix2[g][j]
            row.append(res)
        result_matrix.append(row)

    return result_matrix


operation = input(f"Enter which operation you want to do: \n"
                  f"1 - Multipy matrix by digit \n"
                  f"2 - Add two matrices \n"
                  f"3 - Deduction of two matrices \n"
                  f"4 - Multiply two matrices \n"
                  f"Write operation here: ")

if operation == "1":
    print("Enter matrix1:")
    matrix1 = input_matrix()
    result = multiplication_digit(matrix1)

    for row in result:
        print(row)


elif operation == "2":
    print("Enter matrix1:")
    matrix1 = input_matrix()

    print("Enter matrix2:")
    matrix2 = input_matrix()

    result = add_matrix(matrix1, matrix2)

    for row in result:
        print(row)

elif operation == "3":
    print("Enter matrix1:")
    matrix1 = input_matrix()

    print("Enter matrix2:")
    matrix2 = input_matrix()

    result = deduction_matrix(matrix1, matrix2)

    for row in result:
        print(row)

elif operation == "4":
    print("Enter matrix1:")
    matrix1 = input_matrix()

    print("Enter matrix2:")
    matrix2 = input_matrix()

    result = multiply_matrices(matrix1, matrix2)

    for row in result:
        print(row)

else:
    print("Please write correct operation!")



