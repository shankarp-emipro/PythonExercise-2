import csv

# empty dictionary to store data in future
data = {}


def get_full_name(country_code):
    if country_code == "USA":
        return "United States of America"
    if country_code == "AU":
        return "Australia"
    if country_code == "ES":
        return "Estonia"
    if country_code == "DE":
        return "Denmark"
    if country_code == "UK":
        return "United Kingdom"
    if country_code == "IT":
        return "Italy"


with open("data2.csv", 'r') as file:
    # loading csv file
    csv_file = csv.reader(file, delimiter=',')
    for row in csv_file:
        # below condition is to skip the heading from csv file
        if row[0] == 'Order No':
            continue
        if row[0] not in data.keys():
            data.update({
                row[0]: {
                    'Customer': {
                        'Name': row[1],
                        'Address1': row[5],
                        'Address2': row[6],
                        'City': row[8],
                        'Country': get_full_name(row[9]),
                        'ZipCode': row[7]
                    },
                    'Products': [{
                        'SKU': row[2],
                        'Price': row[4],
                        'Qty': row[3]
                    }]
                }
            })
        else:
            data.get(row[0]).get('Products').append({
                'SKU': row[2],
                'Price': row[4],
                'Qty': row[3]
            })
    file.close()

print(data)
