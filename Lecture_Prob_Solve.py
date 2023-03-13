word = "Hello"

last_letter = word[len(word)-1]
for index in range(len(word)-1, -1, -1):
    print(word[index])

print(last_letter)