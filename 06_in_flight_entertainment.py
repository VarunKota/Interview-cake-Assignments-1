""" You've built an inflight entertainment system with on-demand movie streaming.
Users on longer flights like to start a second movie right when their first one ends,
but they complain that the plane usually lands before they can see the ending. 
So you're building a feature for choosing two movies whose total runtimes will equal 
the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of 
integers movie_lengths (in minutes) and returns a boolean indicating whether there 
are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory. """

# Start coding from here
function brute_infligth (flight_length, movie_length) {
  var i = 0, j = 0, first_movie, second_movie;

  for (; first_movie = movie_length[i++];) {
    for (j = i; second_movie = movie_length[j++];) {
      if (first_movie + second_movie == flight_length) {
        return true;
      }
    }
  }
  
  return false;
}

// O(n) and can't show one movie twice
function hash_infligth (flight_length, movie_length) {
  var hash = {}, first_movie, second_movie, i = 0;

  for (; first_movie = movie_length[i++];) {
    second_movie = flight_length - first_movie;

    if (second_movie in hash) {
      return true;
    }

    hash[first_movie] = true;
  }

  return false;  
}
