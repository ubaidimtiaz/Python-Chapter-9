import time

fin = open('C:/words.txt')
fin.readline()
'''for line in fin:
    word = line.strip()
    print(word)'''


def read_file(fin):
    for line in fin:
        word = line.strip()
    return word


def no_e(word, forbid):
    for letter in word:
        if letter == forbid:
            return 'False'
    return 'True'


def avoid():
    wordin = input('Please enter word')
    stringin = input('Please enter forbidden string')
    for character in stringin:
        if no_e(wordin, character) == 'False':
            return 'False'
    return 'True'


def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True


def use_all(word, string):
    for letter in string:
        if letter not in word:
            return False

    return True


def is_abcedarian(word):
    x = 0
    while x < len(word) - 1:
        first = word[x]
        second = word[x + 1]
        if first > second:
            return False
        x = x + 1
    return True


def consec(word):
    x = 0
    noc = 0
    while x < len(word) - 1:
        if word[x] == word[(x + 1)]:
            noc = noc + 1
            x = x + 1
        else:
            noc = 0
        x = x + 1
    if noc >= 3:
        return True
    else:
        return False


def checkage(myage, momage):
    x = str(myage)
    i = 0
    z = ''
    for letter in x:
        y = x[len(x) - (i + 1)]
        z = z + y
        i = i + 1
    if int(z) == momage:
        return True


def giveage(myage, momage):
    while momage < 150:
        if checkage(myage, momage):
            print(myage, momage)
        myage = myage + 1
        momage = momage + 1


giveage(37, 73)

"""
for lafaz in fin:
    nov=lafaz.strip()
    if (is_abcedarian(nov)):
        print(nov)
"""

"""
import time
kehnti=open("C:\words.txt")
line=kehnti.readline()
def print_noe(filename):
    for word in kehnti:
        check=no_e(word)
        if check == 'True':
            print(word)




def no_e(word,alpha):
    z=0
    for letter in word:
        if letter ==alpha:
            z=z+1
    if z > 0 :
        k= 'False'
    else:
        k = 'True'
    return k


def avoid(word, fdn_let):
    for letter in fdn_let:
        check =no_e(word, letter)
    if check == 'True':
        print(word, "has no forbidden character")
    else:
        print(word, 'has illegal characters')



avoid('helloworld', 'abc')


"""

