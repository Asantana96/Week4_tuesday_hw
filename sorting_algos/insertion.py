a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
words_dict = {}
def count_words(string):
    words = string.lower().split(' ')
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1    
        words_dict[word] += 1
    return words_dict

print(count_words(a_text))
