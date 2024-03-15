import os
os.system('cls' if os.name == 'nt' else 'clear')

#var="Hello"
#print(var[4::-1])

#produces a different result with 0 in end part instead of space. 
# there is space at both ends.
#len does not count 0 where as in dexing there is 0 position
# a string with len 16 will have oly 15 positions when indexing
var="Hello"
print(var[4:0:-1])

#newstring="Hello World!"
#fizz=newstring[0:5]
#print (fizz)

# matematical operations
#cal=((15 + 5) - 10) / 2
#print(cal)

# indexing
#greeting="Hello"
#print(greeting.replace("ll","  ")) # upper, lower,strip,replace etc

#people="Person 1\nPerson 2" #\n helps to print across mutiple lines,\t creates space,end='' helps to print the next output in same line

#print (people,end=' ')
#print (people,end=' ')
#print(people)

