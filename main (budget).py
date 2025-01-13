# Dependencies
import csv
import os
import pandas as pd
# Files to load and output
file_to_load = os.path.join("C:/Users/oury/Documents/GitHub/python-challenge/Resources/budget_data.csv")
# Input file path
file_to_output = os.path.join("C:/Users/oury/Documents/GitHub/python-challenge/Analysis/budget_analysis.txt")

# The total number of months included in the dataset
df = pd.read_csv(file_to_load)
row_count = len(df)

print(f"Total number of months: {row_count}")

net_total = df['Profit/Losses'].sum()

print(f"Net total amount of 'Profit/Losses': {net_total}")


# Calculate the changes in "Profit/Losses"
df['Change'] = df['Profit/Losses'].diff()

# Calculate the average of the changes
average_change = df['Change'].mean()

# Display the results
print(f"Average Change in 'Profit/Losses': {average_change}")

# Find the greatest increase in profits
max_increase = df['Change'].max()
max_increase_date = df.loc[df['Change'].idxmax(), 'Date']

# Display the results
print(f"Greatest Increase in Profits: {max_increase} on {max_increase_date}")

# Find the greatest decrease in profits
max_decrease = df['Change'].min()
max_decrease_date = df.loc[df['Change'].idxmin(), 'Date']

# Display the results
print(f"Greatest Decrease in Profits: {max_decrease} on {max_decrease_date}")

output = f"Financial Analysis----------------------------Total Months: {row_count}, Total:${net_total}, Average Change:${average_change}, Greatest Increase in Profits:${max_increase} on {max_increase_date}, Greatest Decrease in Profits: ${max_decrease} on {max_decrease_date}"

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)