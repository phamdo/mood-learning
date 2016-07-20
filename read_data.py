# use 'python read_data format raw_data.csv mood_data.csv' to format data

import csv
import sys

# processes raw data and strips unnecessary information (notes)
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

def read_data():
    data = {}
    with open(sys.argv[2], 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',', quotechar = '|')
        for row in reader:
            data[row['activities']] = data[row['mood']]
    return data

if (sys.argv[1] == "format"):
    format_data()
elif (sys.argv[1] == "read"):
    print read_data()
    
