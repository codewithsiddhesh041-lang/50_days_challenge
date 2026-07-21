# sum of digits
def sum(num):
    sum=0

    while num > 0:
        digit=num %10
        sum = sum+digit
        num//=10

    return sum

number=int(input("Enter the number :"))
print(f"The sum of number is :{sum(number)}")