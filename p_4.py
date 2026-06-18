A=[[1,2,3],
   [4,5,6]]


B=[[7,8],
   [9,10],
   [11,12]]


result=[[0,0],
        [0,0]]

for i in range(len(A)):               # it's the row of A
    for j in range(len(B[0])):        # colums of B
        for k in range(len(B)):       # column of A / rows of B
            result[i][j]+=A[i][k]*B[k][j]

for row in result:
    print(row)