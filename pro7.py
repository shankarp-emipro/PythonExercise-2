import csv

with open('data.csv', 'r') as source:
    # loading source file
    source_file = csv.reader(source)
    with open('data2.csv', 'w') as destination:
        # loading destination file
        destination_file = csv.writer(destination)
        for data in source_file:
            # reading source file data and writing into destination file line by line
            destination_file.writerow(data)
        print("CSV file created successfully.")
        destination.close()
    source.close()
