# Python code
# To reverse words in a given string
 
# input string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
# prints the string backwards
print(s)
# defines the new array
l = []
# for loop to grab each word in the string
for i in s:
    # prints the word that is grabbed in the loop
    print(i)
    # apending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))


# Function to reverse words of string
def rev_sentence(sentence):
    print(sentence + " line 24")
 
    # first split the string into words
    words = sentence.split(' ')
 
    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))
 
    # finally return the joined string
    return reverse_sentence

# Refers to the name that the file uses the interpreter to call
if __name__ == "__main__":
    print(__name__)
    input = 'geeks quiz practice code'
    print (rev_sentence(input))



# Function to reverse words of string
import re
def rev_sentence(sentence):
 
    # find all the words in sentence
    words = re.findall('\w+', sentence)
 
    # Backward iterate over list of words and join using space
    reverse_sentence = ' '.join(words[i] for i in range(len(words)-1, -1, -1))
 
    # finally return the joined string
    return reverse_sentence
 
if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print (rev_sentence(input))