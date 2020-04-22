cheeses =['Cheddar','EDAM', 'gouda']
numbers=[2,3,5,10,66,5,5,5]
empty=[]






#print (cheeses)
i=0
'''
while i<len(numbers):
    numbers[i] = numbers[i]*2
    i=i+1


print (numbers)
'''
'''
for i in range(8):
    print(i)
    numbers[i] = numbers[i]*2
'''

def only_upper(t):
    temp=[]
    for chez in t:
        if chez.isupper():
            temp.append(chez)
    return temp

cheeses.pop(2)

t = ['a', 'b', 'c']
t.remove('b')
#print(t)
t2 = ['d', 'e', 'f']
del t2[1]
#print(t2)


s='Hello World'
#print(s)
k=list(s)
wo=s.split()
#print (k,"\n", wo)

s='spam3-spam2-spam1'
delimiter='-'
s1=s.split()
s2=list(s)
s3=s.split(delimiter)

#print(s1, '\n', s2,'\n', s3)


#print(s3)

#l1=s3.append(4)
#l2=s3+[4]
#print(s3,l1,l2)

def delete_head(x):
    l3=s3[1:]
    return l3

s3=s3.sort()

t = [1,2,3,4,5,6]


def sumlists(list):
    s=0
    for x in list:

        y=sum(x)
        s=s+y
    return s


def cumsum(list):
    y=sum(list)
    list.append(y)
    
def middle(list):
    newlist=list[1:-1]
    return newlist

def chop(list):
    list.pop(0)
    list.pop(-1)


def is_sorted(t):
    return t == sorted(t)

def is_anagram(word1,word2):
     if len(word1)!=len(word2):
         return False
     for letter in word1:
         if letter not in word2:
             return False
     return True

def has_duplicates(list):
    z=sorted(list)
    for x in range(len(z)-1):
        print (z[x])
        if z[x]==z[x+1]:
            return True
    return False


    return False






fin = open('C:/words.txt')
fin.readline()

def read_file(fin):
    wordlist=[]
    for line in fin:
        word=line.strip()
        wordlist.append(word)
    return wordlist

wordlist = read_file(fin)


def in_bisect(list,word):
    midpoint=len(list)//2
    sorted_list=sorted(list)
    if word==sorted_list[midpoint]:
        return True
    elif word > sorted_list[midpoint]:
        if word in sorted_list[midpoint:]:
            return True
    else:
        if word in sorted_list[0:midpoint]:
            return True
    return False


print(in_bisect(wordlist, 'zyme'))
    
    





