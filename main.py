def get_input():
    print("How many rows?")
    n = int(input())
    matrix = []
    for i in range(n): #takes first matrix, input rows as numbers separated by spaces
        print("Row", i, "?")
        matrix.append([int(j) for j in input().split()])
    return matrix

def dot_product(A,B): #takes two lists, multiplies the corresponding entries, and adds them together
    a = 0
    for i in range(0,len(A)):
        a += int(A[i]) * int(B[i])
    return a

def row(n,A): #returns row n from matrix A, just for notation purposes
    return A[n]

def col(n,A): #returns column n from matrix A
    b = []
    for i in range(0,len(A)):
        b.append(A[i][n])
    return b

def matrix_multiplication_mod_26(A,B): #multiplies matrices together
    result = []
    row_of_result = []
    for i in range(0,len(row(0,A))):
        for j in range(0,len(col(0,B))):
            row_of_result.append(dot_product(row(i,A),col(j,B))%26)
        result.append(row_of_result)
        row_of_result = []
    return result


m1 = get_input()
m2 = get_input()

for elem in matrix_multiplication_mod_26(m1,m2):
    print(elem)








