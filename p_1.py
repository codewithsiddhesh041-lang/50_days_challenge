# Program to count the number of each vowel in a string

string=input("Enter the string: ").lower()

vowles={'a':0,'e':0,'i':0,'o':0,'u':0}

for char in string:
    if char in vowles:
        vowles[char]+=1

print("Vowles counts:")
for vowel,count,in vowles.items():
    print(vowel,"=",count)



