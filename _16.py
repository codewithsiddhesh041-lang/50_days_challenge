
# second largest number
arr = list(map(int, input().split()))

first = second = float('-inf')

for i in arr:
    if i > first:
        second = first
        first = i
    elif first > i > second:
        second = i

if second == float('-inf'):
    print("Second largest element does not exist")
else:
    print(second)