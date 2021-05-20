""" A building has 100 floors. One of the floors is the highest floor an egg can 
be dropped from without breaking.

If an egg is dropped from above that floor, it will break. 
If it is dropped from that floor or below, it will be completely undamaged and 
you can drop the egg again.

Given two eggs, find the highest floor an egg can be dropped from without breaking, 
with as few drops as possible. """

# Start coding from here
def get_average(floors):
    trials = get_trials_per_floor(floors)
    score = sum(trials)
    return score*1.0/floors[-1], max(trials)

floors_map = {}
def get_floors(N, level=0):
    if N == 1:
        return [1]
    if N in floors_map:
        return floors_map[N]
    best_floors = None
    best_score = None
    for i in range(1,N):
        base_floors = [f+i for f in get_floors(N-i, level+1)]
        for floors in [base_floors, [i] + base_floors]:
            score = get_average(floors)
            if best_score is None or score < best_score:
                best_score = score
                best_floors = floors

    if N not in floors_map:
        floors_map[N] = best_floors
    return best_floors

floors = get_floors(100)
print "Solution:",floors
print "max trials",get_max_trials(floors)
print "avg.",get_average(floors)

naive_floors = [14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100]
print "naive_solution",naive_floors 
print "max trials",get_max_trials(naive_floors)
print "avg.",get_average(naive_floors)
