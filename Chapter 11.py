eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}


def histogram(word):
    d = dict()
    for letter in word:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] = d[letter] + 1
    return d


firstdict = (histogram('liadrhuliuhgsgjdiglfgfh'))


def reverse_lookup(dict, item):
    for key in dict:
        if dict[key] == item:
            return key
    raise LookupError('Not found')


def inverse_dict(dic):
    inverse = dict()
    for key in dic:
        value = dic[key]
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)

    return inverse


fin = open('C:/words.txt')


def read_file(fin):
    dictionary_words = dict()

    for line in fin:
        word = line.strip()
        if word not in dictionary_words:
            dictionary_words[word] = line
        else:
            dictionary_words[word] = dictionary_words[word].append(line)
    return dictionary_words


y = read_file(fin)
print(y['aah'])
