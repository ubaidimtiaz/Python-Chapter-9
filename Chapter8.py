
prefixes = 'JKLMNOPQ'
#for letter in 'prefixes':
#    print(letter+'ubaid')


greeting ='Hello world'

new_greeting=greeting[:5]+' Ubaid'

def find(word, letter):
    index = 0
    while index < len(word):
       if word[index] ==letter:
            return index
       index = index +1
    return -1



def counter(word,letter):
    count=0
    for x in word:
        if x==letter:
            count=count+1
    return count


def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)



def word_compare(word1,word2):
    if word1 == word2:
        print("Alright")
    elif word1<word2:
        print( word1 ,'  before  ',word2)
    else:
        print(word2, '  before  ', word1)





def rotate_word(word,n):
    new_word=('')
    for letter in word:
        new_letter = ord(letter) + n
        new_word=new_word+chr(new_letter)
    return(new_word)


print(rotate_word('Aa', 1))

