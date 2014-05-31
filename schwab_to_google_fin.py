import fileinput, csv

schwab_file = "test/test_data.csv"
tmp_format_file = "test/new_test_data.csv"
tmp_format_file2 = "test/new_test_data2.csv"


# def open_csv():
#     with open(f_name) as csvfile:
#         f_reader = csv.reader(csvfile, delimiter = ",")
#         next(f_reader)
#         return next(f_reader)

def remove_first_line(file1, file2):
    with open(file1) as csvfile:
        f_reader = csv.reader(csvfile)
        next(f_reader)
        with open(file2, 'w') as new_csvfile:
            f_writer = csv.writer(new_csvfile)
            for row in f_reader:
                f_writer.writerow(row)

def format_headers(fileA, fileB):
    with open(fileA) as csvfile, open(fileB, 'w') as csvoutfile:
        f_reader = csv.reader(csvfile)
        header = next(csvfile)
        header_list = header.split(",")

        for field in header_list:
            if field == 'Fees & Comm':
                header_list[header_list.index(field)] = "Commission"
            elif field == 'Price':
                header_list[header_list.index(field)] = "Purchase price per share"
            elif field == "Amount\n":
                header_list[header_list.index(field)] = "Other"
            elif field == "Quantity":
                header_list[header_list.index(field)] = "Shares"
        header_list.pop()
        header_list.pop()

        writer = csv.writer(csvoutfile)
        writer.writerow(header_list)
        for row in f_reader:
            row.pop()
            row.pop()
            row.insert(len(row) - 1, row.pop())
            print(row)
            writer.writerow(row)

def open_csv_dict():
    with open(new_f_name) as csvfile:
        csvfile.seek(0)
        next(csvfile)
        f_reader = csv.DictReader(csvfile)

        for row in f_reader:
            print(row)

def main():
    remove_first_line(schwab_file, tmp_format_file)
    format_headers(tmp_format_file, tmp_format_file2)

main()



