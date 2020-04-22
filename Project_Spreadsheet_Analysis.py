import csv

# Required task 1. Read the data from the spreadsheet

def read_file():

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

# Required task 2. Collect all of the sales from each month into a single list
    total_sales = []

    for row in spreadsheet:
        monthly_sales = row['sales']
        total_sales.append(int(monthly_sales))

# Required task 3. Output the total sales across all months
name = 'London'
print(f'The total sales across all {len(total_sales)} months are {sum(total_sales)}' + name)






