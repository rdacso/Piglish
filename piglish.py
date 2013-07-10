pyg = 'ay'
original = raw_input('Enter a word:')
first_letter = original[0]
my_vowels = ["a","e","i","o","u"]
more_pyg = first_letter + "ay"
word = original.lower()
new_word = (word or original) + pyg
another_word = (word or original)[1:100] + first_letter + pyg



if len(original) > 0 and original.isalpha():
    if first_letter.lower() in my_vowels:
        print new_word
    else:
        print another_word
else:
    print 'empty'
    