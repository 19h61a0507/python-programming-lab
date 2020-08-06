def palindrome(string):
    if(string==string[::-1]):
      print("The string is a palindrome")
    else:
      print("Not a palindrome")
      
string=input("enter the string")
palindrome(string)
