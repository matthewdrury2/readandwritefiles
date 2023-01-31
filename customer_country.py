import csv

customers = open("customers.csv", "r")
reader = csv.reader(customers)
next(reader)

customer_country = open("customer countrv.csv", "w", newline="")
writer = csv.writer(customer_country, delimiter=",")

fieldnames = ["First Name", "Last Name", "Country"]
writer.writerow(fieldnames)

for row in reader:
    first_name = row[1]
    last_name = row[2]
    country = row[4]

    display = [first_name, last_name, country]
    writer.writerow(display)

customers.close()
customer_country.close()
