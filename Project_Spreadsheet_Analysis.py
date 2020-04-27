import csv


# Required task 1. Read the data from the spreadsheet

def read_file():
    data = []


    with open('sales.csv', 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)

        for row in spreadsheet:
            data.append(row)

    return data


# Required task 2. Collect all of the sales from each month into a single list
def calculate_sales(data):
    total_sales = []
    for row in data:
        monthly_sales = row['sales']
        total_sales.append(int(monthly_sales))

    # Required task 3. Output the total sales across all months
    print(f'The total sales across all {len(total_sales)} months are {sum(total_sales)}.')

    return sum(total_sales)


# Output to spreadsheet
def run():
    data = read_file()
    sales_sum = calculate_sales(data)
    output_spreadsheet(sales_sum)
    read_output()


summary_filename = 'Summary_of_results.csv'


def output_spreadsheet(sales_sum):
    field_names = ['Summary', 'Value']
    output_data = [
        {'Summary': 'Total sales', 'Value': sales_sum},
    ]

    with open(summary_filename, 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(output_data)


def read_output():
    with open(summary_filename, 'r') as csv_file:
        spreadsheet = csv.DictReader(csv_file)
        for row in spreadsheet:
            print(dict(row))


def monthly_changes(data):
    changes = []
    for index in range(1, len(data)):
        previous = int(data[index - 1]['sales'])
        current = int(data[index]['sales'])
        sales_change = (current - previous) / previous
        changes.append(sales_change * 100)
    print(changes)

# Print averages of sales and expenses
def calculate_avgs(data):
    sales = []
    expenses = []
    for d in data:
        sales.append(int(d["sales"]))
        expenses.append(int(d["expenditure"]))

    avg_sales = sum(sales) / len(sales)
    avg_expenses = sum(expenses) / len(expenses)

    print(f"Avg sales: {avg_sales}")
    print(f"Avg expenses: {avg_expenses}")

#Calculate the following: ○ Monthly changes as a percentage ○ The average
data = read_file()
monthly_changes(data)
calculate_avgs(data)


run()