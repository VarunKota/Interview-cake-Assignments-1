""" I want to learn some big words so people think I'm smart.
I opened up a dictionary to a page in the middle and started flipping through, 
looking for words I didn't know. I put each word I didn't know at increasing 
indices in a huge list I created in memory. When I reached the end of the dictionary, 
I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. 
In other words, this is an alphabetically ordered list that has been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the "rotation point," which is where I 
started working from the beginning of the dictionary. This list is huge 
(there are lots of words I don't know) so we want to be efficient here.

To keep things simple, you can assume all words are lowercase.  """

# Start coding from here
def find_rotation_point(words):
    """return the index of the rotation point of a sorted word list"""

    # basically a modified binary search
    index = 0
    n = len(words)
    if n > 1:
        left = 0
        right = n - 1

        while (right - left) > 1:
            if words[left] > words[right]:
                # the pivot is somewhere within this interval
                # but where?
                # split the interval in half
                # check each half for the pivot
                # use the half that contains the pivot
                nexttry = int((left + right) / 2.0 + 0.5)
                if words[nexttry] > words[right]:
                    left = nexttry
                else:
                    right = nexttry
            else:
                # Boy: Do not try and find the pivot. That's
                #      impossible. Instead only try to realize the truth.
                # Neo: What truth?
                # Boy: There is no pivot.
                return left

        if words[left] <= words[right]:
            index = left
        else:
            index = right

    return index
