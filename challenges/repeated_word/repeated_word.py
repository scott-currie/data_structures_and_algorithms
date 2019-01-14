import re
from ...data_structures.hash_table.hashtable import HashTable


def repeated_word(string):
    """ Parse a string and return the first word found that repeats. This strips out
    all punctuation and non-alpha characters before splitting on whitespace to
    create a list of words to search for.

    :param string: The raw string to parse
    :return: a string representing the first repeated word or None if no words repeat
    """
    p = re.compile('[^a-zA-Z ]')
    string = re.sub(p, '', string)
    ht = HashTable()
    for word in string.split():
        if ht.get(word) is not None:
            return word
        ht.add(word, 0)
    return None