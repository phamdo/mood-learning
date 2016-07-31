import csv
import sys

class Date:
    def __init__(self, year, day):
        self.year = year
        self.day = day
    def __str__(self):
        return str(self.year) + "," + self.day


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

    def get_activities(self):
        return self.activities

    def get_mood(self):
        return self.mood

# processes raw data from 'rawfile' and strips unnecessary information 
# an ordinal measure of mood
def mood_rating(mood):
    mood_dict = {"awful" : 1, "not great" : 2, "meh" : 3, "good" : 4, "rad" : 5};
    return mood_dict[mood]

def mood(rating):
    mood_dict = {1 : "awful", 2 : "not great", 3 : "meh", 4 : "good", 5 : "rad"}
    return mood_dict[rating]

# takes in raw data, removes unwanted information (notes) and writes the formatted data to 'datafile'
def format_data(rawfile, datafile):
    with open(rawfile, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
        output = open(datafile, 'wt')
        writer = csv.writer(output)
        for row in reader:
            new_row = []
            for i in range(5):
                new_row.append(row[i])
            writer.writerow(new_row)

# returns a list of Entry objects containing all of the inputted data
def read_data(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
        first = True
        for row in reader:
            if (first): # skip the first line
                first = False
                continue
            entry = Entry(row[0], row[1], row[2], row[3], row[4])
            data.append(entry)
    return data
    
# use 'python read_data.py format raw_data.csv mood_data.csv' to format data
if (sys.argv[1] == "format"):
    format_data(sys.argv[2], sys.argv[3])
# use 'python read_data.py read mood_data.csv' to read data
elif (sys.argv[1] == "read"):
    print read_data(sys.argv[2])

