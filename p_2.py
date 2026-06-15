# Program to sort alphabetically the words form a string provided by the user.
text=input("Enter a string: ")

words=text.split()
words.sort()

print("Words in alphabetical order :")

for word in words:
    print(word)