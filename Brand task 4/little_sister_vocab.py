
"""
colors = '''red,
orange,
green,
purple,
yellow'''

colors.split(',\n')
print(colors)

for i, index in enumerate(colors):
    print(i, ":", index)
"""

def add_prefix_un(word):
    not_word = "un" + word
    print(not_word )

print(add_prefix_un('happy'))
  

def make_word_groups(prefix, word1, word2, word3):
    new_list = []
    list = [prefix, word1, word2, word3]
    for i in list:
        if i == list[0]:
            new_list.append(i)
        else:
            new_word = list[0] + i
            new_list.append(new_word)

    print(" :: ".join(new_list))
 
make_word_groups('en', 'danger', 'capsule', 'crust')