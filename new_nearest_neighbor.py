from read_data import *
from math import ceil

data = {}
activities_list = []
def n1earest_neighbor(entries, item):   
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

def read_activities(entries):
    data = {}
    activities = []
    for entry in entries:
        for activity in entry.get_activities():
            if activity not in activities:
                activities.append(activity)
    
    for entry in entries:
        results = {}
        for activity in activities:
            if activity in entry.get_activities():
                results[activity] = 1
            else:
                results[activity] = 0
        data[entry] = results
    global activities_list
    activities_list = activities
    return data

def activity_dict(entry):
    activities = {}
    for activity in activities_list:
        
        if activity in entry.get_activities():
            activities[activity] = 1
        else:
            activities[activity] = 0
    return activities

def nearest_neighbor(item):
    min_dist = len(activities_list)
    minEntries = []
    for entry in data.keys():
        dist = 0
        activities = activity_dict(item)
        
        for activity in activities_list:
            if (data[entry][activity] != activities[activity]):
                dist += 1
        if dist < min_dist:
            min_dist = dist
            minEntries = []
            minEntries.append(entry)
        elif dist == min_dist:
            minEntries.append(entry)
    total = 0
    print "nearest neighbors : ", minEntries
    for entry in minEntries:
        total += mood_rating(entry.get_mood())
    return mood(ceil(total / float(len(minEntries))))
   

entries = read_data(sys.argv[1])
inputs = read_data(sys.argv[2])
data = read_activities(entries)
# add support for inputs w/ activities never seen before
for item in inputs:
    print item
    print nearest_neighbor(item)
    print     



