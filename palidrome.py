# def isPalindrome(s):
#     # [::-1] starts at the end of the string and works backwards
#     return s == s[::-1]
  
# # Driver code
# s = input("Please enter your word. ")
# ans = isPalindrome(s)
  
# if ans:
#     print("Yes")
# else:
#     print("No")

# function to check string is
# palindrome or not

# iterative approach
def isPalindrome(str):
  
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
  
# main function
s = "malayalam"
ans = isPalindrome(s)
  
if (ans):
    print("Yes")
else:
    print("No")