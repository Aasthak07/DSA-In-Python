#strings 

#vaild palindrome

s=input("enter the string:")
s=s.lower()

if s==s[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")