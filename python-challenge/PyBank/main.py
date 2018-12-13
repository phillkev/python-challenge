import os
import csv

# Path to collect data from the Resources folder
pybankCSV = os.path.join('..', '..', 'pybank', 'resources', 'budget_data.csv')

sumTxt = open("pybank.txt","w+")

# * Your task is to create a Python script that analyzes the records to calculate each of the following:


#   * The total number of months included in the dataset
totalMonths = 0

#   * The total net amount of "Profit/Losses" over the entire period
totalRevenue = 0

#   * The average change in "Profit/Losses" between months over the entire period
# sumchange is used to accumulate the total amount of change
# averageChange is used to calculate the average change across the period 
sumChange = 0
averageChange = 0

#   * The greatest increase in profits (date and amount) over the entire period
greatestProfitIncreaseAmount = 0
greatestProfitIncreaseMonth = ""

#   * The greatest decrease in losses (date and amount) over the entire period
greatestProfitDecreaseAmount = 0
greatestProfitDecreaseMonth = ""

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

with open(pybankCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    rowCount = 0


    # Loop through the data
    for row in csvreader:
        rowCount = rowCount + 1
        totalMonths = totalMonths + 1
        totalRevenue = totalRevenue + int(row[1])

        # the first row is used to initialize the previousRev variable
        # previousRev is critical for the average change calculation
        # Since this is the first month it contains the greatest increase and
        # greatest decrease in profits so those values are set with the first 
        # conditional 
        if rowCount == 1:
            previousRev = int(row[1])
            greatestProfitIncreaseAmount = int(row[1])
            greatestProfitIncreaseMonth = row[0]
            greatestProfitDecreaseAmount = int(row[1])
            greatestProfitDecreaseMonth = row[0]
        
        # sumchange keeps a running total of the change from the previous months average change
        # and the current rows profits change
        else:
            sumChange = sumChange + (int(row[1]) - previousRev)
            if int(row[1]) > greatestProfitIncreaseAmount:
                greatestProfitIncreaseAmount = int(row[1])
                greatestProfitIncreaseMonth = row[0]
            if int(row[1]) < greatestProfitDecreaseAmount:
                greatestProfitDecreaseAmount = int(row[1])
                greatestProfitDecreaseMonth = row[0]
            previousRev = int(row[1])
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalRevenue}")
    # Average change must ignore the first month since it is the starting point.  We do not want to skew
    # the Average change with the intialization amount

    averageChange = round(sumChange/(totalMonths-1), 2)
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits: {greatestProfitIncreaseMonth} (${greatestProfitIncreaseAmount})")
    print(f"Greatest Decrease in Profits: {greatestProfitDecreaseMonth} (${greatestProfitDecreaseAmount})")

    sumTxt.write("Financial Analysis\n")
    sumTxt.write("----------------------------\n")
    sumTxt.write("Total Months: %d\n" % (totalMonths))
    sumTxt.write("Total: $%d\n" % (totalRevenue))
    sumTxt.write("Average Change: $%.2f\n" % (averageChange))
    sumTxt.write("Greatest Increase in Profits: %s ($ %d)\n" % ((greatestProfitIncreaseMonth), (greatestProfitIncreaseAmount)))
    sumTxt.write("Greatest Decrease in Profits: %s ($ %d)\n" % ((greatestProfitDecreaseMonth), (greatestProfitDecreaseAmount)))
    
    sumTxt.close()

