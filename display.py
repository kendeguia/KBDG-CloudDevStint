#Reading CSV content from a file
import csv
with open('site.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)