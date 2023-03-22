# def read_large_file(file_object):
#     """A- generator function to read a large file lazily."""
#
#     # Loop indefinitely until the end of the file
#     while True:
#
#         # Read a line from the file: data
#         data = file_object.readline()
#
#         # Break if this is the end of the file
#         if not data:
#             break
#
#         # Yield the line of data
#         yield data
#
#
# with open('train.csv') as file:
#     # Create a generator object for the file: gen_file
#     gen_file = read_large_file(file)
#     print(next(gen_file))
#     print(next(gen_file))
import csv
import sys


def get_email_data(csv_fname):
    with open(csv_fname, "r") as email_records:
        for email_record in csv.reader(email_records):
            yield email_record


if __name__ == '__main__':
    filename = "train.csv"
    train_data = iter(get_email_data(filename))
    print(sys.getsizeof(train_data))
    print(next(train_data))  # Skipping the column names
    for i, row in enumerate(train_data):
        if i <= 5:
            row[0] = row[0] + str(50)
            print(row)
