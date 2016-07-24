import csv
import sys
#from enum import Enum

class Date:
    def __init__(self, year, day):
        self.year = year
        self.day = day
    def __str__(self):
        return str(self.year) + "," + self.day

# an ordinal measure of mood
#class Mood(Enum):
#    "awful" = 1
#    "not great" = 2
#    "meh" = 3
#    "good" = 4
#    "rad" = 5

class Entry:
    def __init__(self, year, day, time, mood, activities):
        self.date = Date(year, day)
        self.mood = mood
        self.activities = activities.split(" | ")

    def __str__(self):

        return self.date.__str__() + "," + self.mood + "," \
            + self.activities.__str__()

    def __repr__(self):
        return self.__str__()

# processes raw data and strips unnecessary information (notes)
# use 'python read_data format raw_data.csv mood_data.csv' to format data
def format_data():
    with open(sys.argv[2], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
        output = open(sys.argv[3], 'wt')
        writer = csv.writer(output)
        for row in reader:
            new_row = []
            for i in range(5):
                new_row.append(row[i])
            print new_row
            writer.writerow(new_row)

# returns a list of Entry objects containing all of the inputted data
def read_data():
    data = []
    with open(sys.argv[2], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
        for row in reader:
            entry = Entry(row[0], row[1], row[2], row[3], row[4])
            data.append(entry)
    return data
    #data = {}
    #with open(sys.argv[2], 'rb') as csvfile:
    #    reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    #    for row in reader:
    #        if (data.get(row[3]) != None):
    #            data[row[3]].append(row[4].split(" | "))
    #        else:
    #            data[row[3]] = [row[4]]
    #return data


# distance between any two entries is the number of activities that differ
def distance(list1, list2):
    dist = 0
    for item in list1:
        if item not in list2:
            dist += 1
        else:
            list2.remove(item)
    dist += len(list2)
    return dist

# distance between any two entries is the percentage of activities that
# differ (2 days with all same activities have distance 0, and 2 days
# with none of the same activities have distance 1)
def dist(list1, list2):
    dist = 0
    total = 0
    for item in list1:
        if item not in list2:
            dist +=1
        else:
            list2.remove(item)
        total += 1

    dist += len(list2)
    return dist/total

if (sys.argv[1] == "format"):
    format_data()
elif (sys.argv[1] == "read"):
    print read_data()

