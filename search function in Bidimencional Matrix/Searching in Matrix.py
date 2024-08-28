def searchingmatrix(matrix_a, number):
    """
    Searches for a number in a matrix and returns its position (row, column).

    :param matrix_a: List of lists (matrix) where the number will be searched.
    :param number: Number to search for in the matrix.
    :return: A tuple (row, column) if the number is found, or None if not found.
    """
    for i in range(len(matrix_a)):  # Iterate over each row in the matrix
        for j in range(len(matrix_a[i])):  # Iterate over each column in the current row
            if matrix_a[i][j] == number:  # Compare the element with the desired value
                return i, j  # Return the position (row, column) if the value is found
    return None  # Return None if the value is not found in the matrix


matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("\n\n---------------------------------------------------------------------\n")
print("This is a script for searching for a number.\n"
      "In order to work properly, you must pass 2 parameters:\n"
      "* The first is the matrix in which you want to search.\n"
      "* The second is the number you want to find.\n")
print("For example, imagine we have the matrix:\n"
      "[10, 20, 30],\n"
      "[40, 50, 60],\n"
      "[70, 80, 90]\n"
      "Now, enter the number you want to search for:")

# Validate that the user's input is an integer
while True:
    user_input = input()
    if user_input.isdigit():
        number_to_find = int(user_input)
        break
    else:
        print("Invalid input. Please enter an integer number:")

result = searchingmatrix(matrix, number_to_find)
if result is not None:
    print("The number is in the position:", result)
else:
    print("The number was not found in the matrix.")
