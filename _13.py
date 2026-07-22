#  palindrome

def Palindrome(text):
    return text ==text[::-1]


n=input("Enter the string :")


if Palindrome(n):
        
        print("Its a Palindrome")

else:
        
        print("Its not a Palindrome")


