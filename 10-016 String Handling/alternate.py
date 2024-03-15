import os
os.system('cls' if os.name == 'nt' else 'clear')
# created a total 0f 3 programs.
# 2 of which are to change case of alternate letters in a string 
# the last one is to change case of alternate words in a string



# In examplwe 1 used the list function to help indexing and changing case
 
print("Example:1")

word = "Hello world"
word = list(word)
word_len = len(word)


# using for loop to help change index one by one

for i in range (0,word_len):
    if i % 2 == 0:
        word[i] = word[i].upper()
    else:
        word[i] = word[i].lower()

print("".join(word))


# In example 2 created an empty variable and added strings once case had been changed

print("Example:2")

word = "Hello world"
wordlist = ""
word_len = len(word)

for i in range (0,word_len):
    if i % 2 == 0:
        add = word[i].upper()
        wordlist = wordlist+add
    else:
        add = word[i].lower()
        wordlist = wordlist+add

print(wordlist)




# program to change case of alternate word in the string

# using split command to create a list of words

print("Example:3")

word = "Hello world"
word = word.split()
word_len = len(word)


for i in range (0,word_len):
    if i % 2 == 0:
        word[i] = word[i].upper()
    else:
        word[i] = word[i].lower()

print(" ".join(word))






