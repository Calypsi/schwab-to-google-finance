import csv

f_name = "test/test_data.csv"

def open_csv():
    with open(f_name) as csvfile:
        f_reader = csv.reader(csvfile, delimiter = ",")
        next(f_reader)
        return next(f_reader)

