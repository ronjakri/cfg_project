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

        print(f'The total sales across all {len(total_sales)} months are {sum(total_sales)}.')


read_file()

summary_filename = 'Summary_of_results.csv'
def output_spreadsheet():
    field_names = ['Summary', 'Value']
    data = [
        {'Summary': 'Total sales', 'Value': 45642},
    ]

    with open(summary_filename, 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(data)


output_spreadsheet()


def read_output():
    with open(summary_filename, 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            print(dict(row))


read_output()
