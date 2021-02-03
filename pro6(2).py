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
    csv_file = csv.DictReader(file, delimiter=',')
    for row in csv_file:
        # below condition is to skip the heading from csv file
        # print(row.get('Order No'))
        if row.get('Order No') not in data.keys():
            data.update({
                row.get('Order No'): {
                    'Customer': {
                        'Name': row.get('Customer'),
                        'Address1': row.get('Address1'),
                        'Address2': row.get('Address2'),
                        'City': row.get('City'),
                        'Country': get_full_name(row.get('Country')),
                        'ZipCode': row.get('Zipcode')
                    },
                    'Products': [{
                        'SKU': row.get('SKU'),
                        'Price': row.get('Price'),
                        'Qty': row.get('Qty')
                    }]
                }
            })
        else:
            data.get(row.get('Order No')).get('Products').append({
                'SKU': row.get('SKU'),
                'Price': row.get('Price'),
                'Qty': row.get('Qty')
            })

print(data)
