# find each element present in ..arr

arr=list(map(int,input().split()))

v=[]

for i in arr:
    if i not in v:
        c=0
        for j in arr:
            if i==j:
                c+=1
        print(i,":",c)
        v.append(i)

