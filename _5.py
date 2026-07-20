
n = int(input("Enter how many numbers: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_count = 0
odd_count = 0

print("\nEven Numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)
        even_count += 1

print("\nOdd Numbers:")
for num in numbers:
    if num % 2 != 0:
        print(num)
        odd_count += 1

print("\nTotal Even Numbers:", even_count)
print("Total Odd Numbers:", odd_count)