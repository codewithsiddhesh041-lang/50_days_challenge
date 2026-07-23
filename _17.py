# conut number of each element present in how much time


arr=list(map(int,input().split()))
for i in set(arr):
    print(i, ":", arr.count(i))