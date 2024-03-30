
# new program to add "un" infront of a word
def add_prefix_un(word):
    not_word = "un" + word
    print(not_word )

add_prefix_un('happy')

  
# new program to print prefix followed by 3 words with the given prefix
def make_word_groups(prefix, word1, word2, word3):
    new_list = [] # creating a new list to add the new words created after adding prefix
    list = [prefix, word1, word2, word3]

    # using for loop to iterate through each item in list and make changes
    for i in list:
        if i == list[0]:
            new_list.append(i)
        else:
            new_word = list[0] + i
            new_list.append(new_word)

    print(" :: ".join(new_list)) # converting from list to sentence form
 
make_word_groups('en', 'danger', 'capsule', 'crust')


# new program to remove suffix 'ness' and printing root word
def remove_suffix_ness (word):
    length = len(word)

    # checking the condition if i comes in the word and making changes accordingly
    if word[-5] == 'i':
        new_prefix = word[:length-5]
        print(new_prefix + 'y')
    else:
        new_prefix = word[:length-4]
        print(new_prefix)

remove_suffix_ness('boldness')


# new program to convert adjective to verb 
def adjective_to_verb (sentence, index):
    list_ = sentence.split()
    new_word = list_[index]+'en'
    print(new_word)

adjective_to_verb('it got dark as the sun set', 2)


    
    
       