""" You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to 
rank them from highest to lowest. So far you're using an algorithm that sorts 
in O(n log n) time, but players are complaining that their rankings aren't 
updated fast enough. You need a faster sorting algorithm.

Write a function that takes:
a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n log n) time.

For example:

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)

We’re defining n as the number of unsorted_scores because we’re expecting the 
number of players to keep climbing.

And, we'll treat highest_possible_score as a constant instead of factoring 
it into our big O time and space costs because the highest possible score isn’t 
going to change. Even if we do redesign the game a little, the scores will stay 
around the same order of magnitude. """

# Start coding from here
unsorted_scores=[]
n=int(input("enter no.of inputs:"))
print("Enter the elements in the list:")
for i in range(n):
       unsorted_scores.append((input()))
unsorted_scores[:]=list(map(int,unsorted_scores))
if (i<=100):
        a=(list(reversed(sorted(unsorted_scores))))
print("The unsorted scores are: ",unsorted_scores) 
print("The final scores are:",a)
