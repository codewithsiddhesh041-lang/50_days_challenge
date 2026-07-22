# fing second last number
arr=list(map(int,input("Enter the numbers:").split()))

arr=list(set(arr))
arr.sort()

print(arr[-2])