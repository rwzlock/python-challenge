#Dependencies
import os
import csv

#Path of the 2 csv inputs
csvpath1 = os.path.join('Resources', 'budget_data_1.csv')
csvpath2 = os.path.join('Resources', 'budget_data_2.csv')
#Path of the 2 csv outputs
outputpath1 = os.path.join('output', 'results1.csv')
outputpath2 = os.path.join('output', 'results2.csv')
#budget_data_1.csv has its results stored in results1.csv
#budget_data_2.csv has its results stored in results2.csv

#The path has to be specified when the person running the program decides which file they want to run the data on. I could have repeated this for both files in the
#same program, but did not see a reason to double the length of the code when the person running it could just change the path to specify the file they want to use to 
#read or write.

#Variable for total revenue
total_months= 0
total_revenue = 0
#Lists for the monthly revenue changes, actual values and a container for months
monthly_revenues = []
monthly_changes = []
months = []
#Lists for the change per month and average change
change = 0
average_change = 0
#Lists for greatest increase and decrease
increase = 0
decrease = 0

#Read using CSV module
with open(csvpath1, 'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skips the header line
    next(csvreader)
    
    for row in csvreader:
        #Add 1 to the total_months, add revenue (row[1]) to total revenue. Append the budget value to a list named monthly_revenues
        # that will be used to calculate the changes between months. Lastly append the month for easier printing at the end
        total_months=total_months+1
        total_revenue=total_revenue+int(row[1])
        monthly_revenues.append(int(row[1]))
        months.append(str(row[0]))

    #Constructs list that contains all monthly changes using the definition of the derivative with h=1 
    #Definition of derivative: [f(x+h)-f(x)]/h
    for i in range(1, len(monthly_revenues)):
        change = monthly_revenues[i]-monthly_revenues[i-1]
        monthly_changes.append(change)
    #Calculate average of the monthly_changes list to find the average change
    average_change = sum(monthly_changes)/len(monthly_changes)
    #Find the maximum and minimum of the monthly_changes list to find the greatest increase and decrease amount
    increase = max(monthly_changes)
    decrease = min(monthly_changes)
    #Find the month in the months list corresponding to the greatest increase and decrease found in the monthly changes
    #The +1 is a correction factor. Because a change is really a difference between two months, I can use either month to specify the increase and decrease
    #I defined the month as the month where the changes end. Ex. if the biggest change was from jan-11 to feb-11, my month would be listed as feb-11.
    increase_month = months[monthly_changes.index(increase)+1]
    decrease_month = months[monthly_changes.index(decrease)+1]

     #Series of print statements to print the results to the command line
    print("Financial Analysis")
    print("-"*20)
    print("Total Months: "+str(total_months))
    print("Total Revenue: $"+str(total_revenue))
    print("Average Revenue Change: $"+str(average_change))
    print("Greatest Increase in Revenue: "+str(increase_month)+" $"+str(increase))
    print("Greatest Decrease in Revenue: "+str(decrease_month)+" $"+str(decrease))
    print("-"*20)
    
    #Use csvwriter to write the results into a csvfile
with open(outputpath1, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    #Series of write statements to write the data to a csv
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months:', str(total_months)])
    csvwriter.writerow(['Total Revenue:', '$'+str(total_revenue)])
    csvwriter.writerow(['Average Revenue Change:', '$'+str(average_change)])
    csvwriter.writerow(['Greatest Increase in Revenue', str(increase_month), '$'+str(increase)])
    csvwriter.writerow(['Greatest Decrease in Revenue', str(decrease_month), '$'+str(decrease)])
    