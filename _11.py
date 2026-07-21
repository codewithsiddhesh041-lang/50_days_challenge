# reverse the number
def revers_number(num):
    rev=0

    while num > 0:
        digit= num % 10
        rev=rev * 10 +digit
        num //= 10

    return rev

number= int(input("Enter a number :"))
print(f"The reverse number is: {revers_number(number)}")