import os
os.system('cls' if os.name == 'nt' else 'clear')

"""
num_list=[1,2,3,4,5,6]
new_num_list=[element*2 for element in num_list]

print(new_num_list)

"""

num=list(range(0,10))
print(num)


"""
questions = [["What color is the daytime sky on a clear day? ", "blue"],
            ["What is the answer to life, the universe and everything? ", "42"],
            ["What is a three letter word for mouse trap? ", "cat"]]

if len(questions) == 0 :
    print(" There are no questions")

right = 0
index = 0
for i in range (0,len(questions)):
    question = questions[index][0]
    answer = questions[index][1]
    given_answer = input ( question)
    
    if answer == given_answer:
        print( "Your answer is correct")
        right=right+1
        index=index+1
        
    else: 
        print("Your answer is incorrect")
        index=index+1

print (f"the right no of answers given by is {right}")

"""

names = ["Richa jain","Akshay jain","Reyan Sangal","Dia Sangal"]
names_dictionary = {}

for i in names:
    temp = i.split()
    print ( temp[0],temp[1] )

    name = temp [0]
    surname = temp [1]
    names_dictionary[name] = surname

print(names_dictionary)


print("Example:3")

word = "Hello world"
word = word.split(" ")
word_len = len(word)
print (word)


for i in range (0,word_len):
    if i % 2 == 0:
        word[i] = word[i].upper()
    else:
        word[i] = word[i].lower()

print(" ".join(word))



