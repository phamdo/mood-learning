from read_data import *
from math import ceil
def nearest_neighbor(entries, item):   
    minDist = 1
    minEntries = []
    for entry in entries:
        d = dist(item.get_activities(), entry.get_activities())
        if d < minDist:
            minDist = d
            minEntries = []
            minEntries.append(entry)
        elif d == minDist:
            minEntries.append(entry)
    total = 0
    print "nearest neighbors : ", minEntries
    for entry in minEntries:
        total += mood_rating(entry.get_mood())
    return mood(ceil(total / len(minEntries)))
    


def dist(list1, list2):
    dist = 0
    total = 0
    same = 0
    for item in list1:
        if item not in list2:
            dist += 1
        else:
            same += 1
        total += 1
    dist += (len(list2) - same)
    total += len(list2)
    return dist/float(total)

entries = read_data(sys.argv[1])
inputs = read_data(sys.argv[2])
for item in inputs:
    print item
    print nearest_neighbor(entries, item)
