from read_data import *

def nearest_neighbor(datafile, inputfile):
    entries = read_data(datafile)
    inputs = read_data(inputfile)
    for item in inputs:
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
        print minEntries



def dist(input1, input2):
    dist = 0
    total = 0
    list2 = lis2
    for item in list1:
        if item not in list2:
            dist += 1
        else:
            list2.remove(item)
        total += 1
    dist += len(list2)
    total += len(list2)
    print dist, total
    return dist/float(total)

nearest_neighbor(sys.argv[1], sys.argv[2])
