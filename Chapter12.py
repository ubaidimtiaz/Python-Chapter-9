t = tuple(('x', 'y', 'z'))
l = tuple(('a', 'b', 'c'))


def print_whatever(variable):
    for x in variable:
     print(x)


def divide_Number(n1, n2):
    print(n1)
    print(n2)
    quot = n1 // n2
    rema = n1 % n2
    print(quot, rema)


t = ('a',2,3,4)
def make_dict(*arg):
    y=dict()
    i=0
    for value in arg:
        y[i]=value
        i=i+1


    print (y)





def sum_all(*arg):
    y = 0
    for x in arg:
        y = y + x
    print(y)
t=[('a',1),('b',1),('c',1),('d',1),('e',1)]


k=dict()
for index, element in enumerate('abc'):
    k[index]=element


def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)
    print (t)
    res = []
    for y in t:
        res.append(y)

    return res


def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: string

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

for x in dict:
    dict[x]==value
    return x


print(most_frequent('abbcccdddddeeeeeee'))




