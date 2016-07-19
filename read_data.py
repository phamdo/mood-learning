import csv
import sys

# read data
def read_data():
    with open(sys.argv[1], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
        output = open(sys.argv[2], 'wt')
        writer = csv.writer(output)
        for row in reader:
            new_row = []
            for i in range(5):
                new_row.append(row[i])
            print new_row
            writer.writerow(new_row)


read_data()
