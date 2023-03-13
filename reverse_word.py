# def reverser(word):
#     reversed_word = ""
#     for index in range(len(word)-1, -1, -1): #gives a number middle -1 stops before zero, last -1 counts down)
#         reversed_word += word[index]
#     return reversed_word

# print(f"pajamas reversed is: {reverser('pajamas')}")

# def reverser(word):
#     reversed_word = word[-1] + word[-2] + word[-3] + word[-4] + word[-5] + word[-6]
#     print(f'{reversed_word}')

# reverser("Gotham")

# def cap_letters(phrase):
#     capped_letter_phrase = input("please type two words ")
#     cap_first_letter = capped_letter_phrase.title()
    
#     print(cap_first_letter)



# cap_letters(phrase="")

# from itertools import count


# compress_character = input("Enter a string")

# number_of_characters = compress_character.count("a")
    
# print(number_of_characters)

# def compress_str(user_string):
#     return [(len(list))]

#Code to count the number of characters in a string
# def solve(string_cout):
#    res = ""
#    cout = 1
#    for i in range(1, len(string_cout)):
#       if string_cout[i - 1] == string_cout[i]:
#          cout += 1
#       else:
#          res = res + string_cout[i - 1]
#          if cout > 1:
#             res += str(cout)
#          cout = 1
#    res = res + string_cout[-1]
#    if cout > 1:
#       res += str(cout)
#    return res

# string_cout = input("Please enter a string. ")
# print(solve(string_cout))

string_count = input("Please type some code. ")
letter_counter = 1
letter_holder = ""

for i in range(1, len(string_count)): #Starts at position 1
    if string_count[i-1] == string_count[i]: #String count input starts at 1 so the two are equal
        letter_counter += 1 #Since the two letters are equal, the count goes up.
    else:
        letter_holder = letter_holder + string_count[i-1]
        if letter_counter > 1:
            letter_holder += str(letter_counter)
        letter_counter = 1
letter_holder = letter_holder + string_count[-1]
if letter_counter > 1:
    letter_holder += str(letter_counter)
#return letter_holder



print(string_count)
print(letter_holder)
print(letter_counter)

# number_of_char = string_count.count("l")
# find_char = string_count.find("l")
# print(number_of_char)
# print(find_char)