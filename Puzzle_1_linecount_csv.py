import csv

csv_file = open("puzzlesV2/csv-sample.csv")
csv_read = csv.reader(csv_file)
rows_count = 0

for i in csv_read:
    rows_count+=1

print(f'The number of rows present in the given csv file is {rows_count}')