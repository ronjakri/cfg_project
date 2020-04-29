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


run()

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











import matplotlib.pyplot as plt



def LoHi_sales(data):
    x = []
    for index in data:
        x.append(int(index['sales']))

    sales = [min(x), max(x)]

    print("The lowest sale is: ", min(x), "\nThe highest sale is: ", max(x))
    return sales



def graph(data):

    x = []
    y1 = []
    y2 = []
    for index in data:
        x.append(index['month'])
        y1.append(int(index['sales']))
        y2.append(int(index['expenditure']))
    plt.ylabel('sales and expenditure')
    plt.xlabel('months')
    plt.title('Sales and Expenditure by Month')
    plt.bar(x,y1, label = 'sales', color = 'blue', align = 'edge', width = 0.3,  )
    plt.bar(x,y2, label = 'expen.', color = 'green', width = 0.3)
    plt.legend()
    plt.show()



data = read_file()
LoHi_sales(data)


user = input("Do you want to see the graph? (y/n) ")
if user == 'y':
    graph(data)


def asking_user():

    user = input("Which month do you want to display? ")

    for index in range(0, len(data)):
        if user == data[index]['month']:
            print(f"The sale in {user} was ", int(data[index]['sales']))
            print(f"The expenditure in {user} was ", int(data[index]['expenditure']))

asking_user()

