
#import and establish path
import os
import csv

budget_data = os.path.join("Pybank/Resources/budget_data.csv")

#get the total months
with open(budget_data, "r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csv_reader)
        total_rows = len(list(csv_reader))


#get the total sum 
columns_to_sum = [1]
total_sum = 0

with open(budget_data, "r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csv_reader)

        for row in csv_reader:
                row_sum = sum(float(row[1]) for i in columns_to_sum)
                total_sum += row_sum
        dollars_total_sum = "${}".format(int(total_sum)) #this is displaying the total sum as an integer, formatted with the dollar sign $ 

    
#changes in profit/loss over time, and average of changes
column_changes = 1
changes = []
previous_value = None

with open(budget_data, "r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csv_reader)

        for row in csv_reader:
                current_value = float(row[column_changes])
                if previous_value is not None:
                    value_change = current_value - previous_value
                    changes.append(value_change)

                previous_value = current_value

        average_change = sum(changes) / len(changes)
        dollars_average_change = "${}".format(int(average_change))
 

#find the greatest increase
#I feel like there may be a way easier/cleaner way to do this, but I'm just following what I did before
column_greatest_increase = 1
column_greatest_increase_date = 0
greatest_increase = None
greatest_increase_date = None
previous_value = None

with open(budget_data, "r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csv_reader)

        for row in csv_reader:
                current_value=float(row[column_greatest_increase])
                current_value_date=(row[column_greatest_increase_date])

                if previous_value is not None:
                    value_increase = current_value - previous_value

                    if greatest_increase is None or value_increase > greatest_increase:
                        greatest_increase = value_increase
                        greatest_increase_date = current_value_date
                previous_value = current_value

        dollars_greatest_increase = "${}".format(int(greatest_increase))
#I initially had only the {dollars_greatest_increase}, and had to add in the {greatest_increase_date} on top


#find the greatest decrease
column_greatest_decrease = 1
column_greatest_decrease_date = 0
greatest_decrease = None
greatest_decrease_date = None
previous_value = None

with open(budget_data, "r") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csv_reader)

        for row in csv_reader:
                current_value=float(row[column_greatest_decrease])
                current_value_date=(row[column_greatest_decrease_date])

                if previous_value is not None:
                    value_decrease = previous_value - current_value

                    if greatest_decrease is None or value_decrease > greatest_decrease:
                        greatest_decrease = value_decrease
                        greatest_decrease_date = current_value_date
                previous_value = current_value

        dollars_greatest_decrease = "${}".format(int(greatest_decrease))


#print everything in terminal
#I added print() at the beginning and end for a little cleaner appearance :)
print()
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_rows}")
print(f"Total sum: {dollars_total_sum}")
print(f"Average Change: {dollars_average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} ({dollars_greatest_increase})") 
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (-{dollars_greatest_decrease})")
print()


#output, write to Analysis folder
output_path = os.path.join("Pybank/Analysis/budget_analysis.csv")

with open(output_path, "w") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(["Financial Analysis"])
        csv_writer.writerow(["------------------------------"])
        csv_writer.writerow([f"Total Months: {total_rows}"])
        csv_writer.writerow([f"Total sum: {dollars_total_sum}"])
        csv_writer.writerow([f"Average Change: {dollars_average_change}"])
        csv_writer.writerow([f"Greatest Increase in Profits: {greatest_increase_date} ({dollars_greatest_increase})"]) 
        csv_writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} (-{dollars_greatest_decrease})"])

print()
print("--> Results recorded in Pybank/Analysis/budget_analysis.csv <--")
print()