# Create a file path variable
csvpath = "/Users/linh/Desktop/Linh/Classwork/Lectures/02-Homework/03-Python/python-challenge/PyBank/Resources/budget_data.csv"

# Module for reading CSV files
import csv

# Creating a variable for row count and setting its initial value
# Excluding the headers
rowcount = 0

# Creating a variable for total profit/losses and setting its initial value
total_profit_loss = 0

# Creating a list for Profit/Losses column
profit_loss_list = []

# Creating a list for all revenue increases and decreases
change_list = []

# Creating a list for Date column
month_list = []


# Reading using csv module
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skipping the headers
    headerline = next(csvfile)

    # Iterating through the whole file
    for row in csvreader:

        # Adding one after looping through each row
        rowcount += 1

        # Adding the next profit/losses cell to the current total 
        # after looping through each row
        total_profit_loss += int(row[1])

        #Inserting all values in profit/losses column into a list
        profit_loss_list.append(int(row[1]))

        month_list.append(row[0])

    # Creating a variable for the total of all months' revenue deltas
    sum_of_change = 0

    # Looping through each profit/loss 
    for i in range(1, len(profit_loss_list)):

        # Calculating delta between 2 consecutive months
        change_list.append(profit_loss_list[i] - profit_loss_list[i-1])

        # Calculating total deltas
        sum_of_change += profit_loss_list[i] - profit_loss_list[i-1]

        # Finding the index of the greatest increase
        greatest_increase_index = change_list.index(max(change_list))

        # Locating the month of the greatest increase
        greatest_increase_month = month_list[greatest_increase_index + 1]

        # Finding the index of the greatest decrease
        greatest_decrease_index = change_list.index(min(change_list))

        # Locating the month of the greatest decrease
        greatest_decrease_month = month_list[greatest_decrease_index + 1]

    # Calculating the average 
    average_change = sum_of_change/(len(profit_loss_list)-1) 


    print("Financial Analysis")
    print("------------------------")

    # Printing the total number of months
    print(f"Total Months: {rowcount}")

    # Printing the net total amount of profit/losses
    print(f"Total: ${total_profit_loss}")

    # Printing the changes in profit/losses
    print(change_list)

    # Printing the net amount of changes in profit/losses
    print(sum_of_change)

    # Printing the average of those changes
    print(f"Average Change: ${round(average_change,2)}")
    
    # Printing the months and values of the greatest increase and greatest decrease
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${max(change_list)}).")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${min(change_list)}).")

# Creating a text file
text_file = "/Users/linh/Desktop/Linh/Classwork/Lectures/02-Homework/03-Python/python-challenge/PyBank/analysis/Financial_Analysis.txt"
with open(text_file, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("------------------------\n")
    text.write(f"Total Months: {rowcount}\n")
    text.write(f"Total: ${total_profit_loss}\n")
    text.write(f"Average Change: ${round(average_change,2)}\n")
    text.write(f"Greatest Increase in Profits: {greatest_increase_month} (${max(change_list)}).\n")
    text.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${min(change_list)}).")