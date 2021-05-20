""" I'm making a search engine called MillionGazillion™.
I wrote a crawler that visits web pages, stores a few keywords in a database, 
and follows links to other web pages. I noticed that my crawler was wasting a 
lot of time visiting the same pages over and over, so I made a set, visited, 
where I'm storing URLs I've already visited. Now the crawler only visits a URL 
if it hasn't already been visited.

Thing is, the crawler is running on my old desktop computer in my parents' basement 
(where I totally don't live anymore), and it keeps running out of memory because 
visited is getting so huge.

How can I trim down the amount of space taken up by visited?  """

# Start coding from here

from __future__ import print_function
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
import unittest
import random
import string
import math

try:
    from reprlib import repr
except ImportError:
    pass




class Trie:

    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):

        current_node = self.root_node
        is_new_word = False

  
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

  
        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}

        return is_new_word

class WordGenerator:

    def __init__(self, length=100000):
        self.charlen = length
        self.chars = string.ascii_lowercase + string.ascii_uppercase
        self.charlist = \
            ''.join(random.choice(self.chars) for _ in range(length))
        print("init: %s chars" % length)

    def gen(self, max_length=None):

        length = random.randrange(0, max_length)
        start = random.randint(0, self.charlen)
        end = start + length
        if end > self.charlen:
            end = self.charlen
        word = self.charlist[start:end]
        return word


class TestTrieVsHash(unittest.TestCase):

    def a_test(self, number_of_words=1000, max_word_size=20, text_size=10000):

        # Our Trie of hash tables
        self.t = Trie()

        # Our naive hash table
        self.h = {}

        sizes_t = []
        sizes_h = []

        sizes_t.append(total_size(self.t.root_node))
        sizes_h.append(total_size(self.h))

        self.words = WordGenerator(length=text_size)

        bucket_size = int(math.ceil(number_of_words / 10.0))

        # https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm
        n = 0
        mean = 0.0
        M2 = 0.0

        for i in range(number_of_words):

            # get a word
            word = self.words.gen(max_length=max_word_size)

            # store a word
            self.t.check_present_and_add(word)
            self.h[word] = True

            # keep a running sum of the variance of word length
            n += 1
            x = len(word)
            delta = x - mean
            mean += delta / n
            delta2 = x - mean
            M2 += delta * delta2

            # print("n %s  len %s  delta %s  mean %s delta2 %s  M2 %s" %
            #       (n, x, delta, mean, delta2, M2))

            if i % bucket_size == 0:
                sizes_t.append(total_size(self.t.root_node))
                sizes_h.append(total_size(self.h))

        # all done, print out a csv of the results
        print("\nwords, trie bytes, hash bytes")
        for i in range(len(sizes_t)):
            # print("%s words, trie %s bytes, hash %s" %
            #       (i * bucket_size, sizes_t[i], sizes_h[i]))
            print("%s, %s, %s" %
                  (i * bucket_size, sizes_t[i], sizes_h[i]))

        if n < 2:
            stddev = float('nan')
        else:
            variance = M2 / (n - 1)
            stddev = math.sqrt(variance)

        print("\n%s words, mean length = %s, std. deviation = %s" %
              (n, mean, stddev))

        print("")

    def test_1small_words(self):
        self.a_test(max_word_size=20)

    def test_2big_words(self):
        self.a_test(max_word_size=200)

    def test_3small_corpus(self):
        self.a_test(text_size=1000, number_of_words=10000, max_word_size=20)

    def test_4lots_of_words(self):
        self.a_test(number_of_words=100000)



def total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.
    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:
        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}
    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                    }
    all_handlers.update(handlers)  # user handlers take precedence
    seen = set()                  # track object id's already seen
    # estimate sizeof object without __sizeof__
    default_size = getsizeof(0)

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrieVsHash)
    unittest.TextTestRunner(verbosity=2).run(suite)
