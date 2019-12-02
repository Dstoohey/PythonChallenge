import csv, os

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis")

total_months = 0
preview_revenue = 0
total_revenue = 0
months_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]

with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader: 
        total_months = total_months + 1
        total_revenue = int(row["Profit/Losses"])