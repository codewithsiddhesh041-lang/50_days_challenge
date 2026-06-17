#Program to transpose a matrix using nested loops

A=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transpose=[]

for i in range(len(A[0])):      # columns
    row=[]
    for j in range(len(A)):     # --- Rows
        row.append(A[j][i])

    transpose.append(row)

print("Transpose Matrix: ")
for row in transpose:
    print(row)