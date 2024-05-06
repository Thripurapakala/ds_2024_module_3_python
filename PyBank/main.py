import os
import csv

# Path to collect data from the Resources folder.
budget_csv = os.path.join('PyBank/Resourses/budget_data.csv')
# Define the function and have it accept the 'budget_csv as its sole parameter.

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas.
    csvreader = csv.reader(csvfile, delimiter=',')
    #Took the help of Class Practice workouts and prof class exercises.
    #Took help from Stackoverflow and Kaggle.
    #declaring all the needed variables.
    header = next(csvreader)
    totalMonths=0
    total = 0
    initFlag = False
    profitLossMax = 0
    profitLossMin = 0
    prevProfitLoss = 0
    profitLossChange = 0
    profitLossMaxDate = ""
    profitLossMinDate = "" 
    profitLossChangeTotals = 0 
    profitLossChangeRate = 0


    #looping the csvreader file .
  
    for i in csvreader:
        #finding total months and total profit/loss.
        totalMonths = totalMonths + 1
        total= total + int(i[1])

        #intitalizing to skip the first row for finding the average change.
        if initFlag == True:
            profitLossChange = int(i[1]) - prevProfitLoss
        #intitalizing the values for the max and min.
        if initFlag == False:
            profitLossMax = int(i[1])
            profitLossMin = int(i[1]) 
            initFlag = True

        #assigning the previous value.
        prevProfitLoss = int(i[1])

        #finding the profit loss change totals.
        profitLossChangeTotals = profitLossChangeTotals + profitLossChange

        #finding the Max profit/loss change.
        if profitLossMax < profitLossChange :
            profitLossMax = profitLossChange
            profitLossMaxDate = str(i[0])

        #Fiding the min profit/loss change.
        if profitLossMin > profitLossChange :
            profitLossMin = profitLossChange
            profitLossMinDate = str(i[0])  

    #Finding the profit loss change rate.
    profitLossChangeRate = profitLossChangeTotals / (totalMonths - 1)   
    
    fileWrite = open("PyBank/Analysis/file.txt", "w")

    #printing the financial ananlysis as requested.
    print("------------------------------", file = fileWrite)
    print("Financial Analysis", file = fileWrite)
    print("------------------------------", file = fileWrite)    
    print(f"Total Months: {totalMonths}", file = fileWrite)        
    print(f"Total: ${total}", file = fileWrite)
    print(f"Average Change: ${round(profitLossChangeRate,2)}", file = fileWrite)
    print(f"Greatest Increase in Profits: {profitLossMaxDate} (${profitLossMax})", file = fileWrite)
    print(f"Greatest Decrease in Profits: {profitLossMinDate} (${profitLossMin})", file = fileWrite)

    fileWrite.close()

    print("------------------------------") 
    print("Financial Analysis")
    print("------------------------------")    
    print(f"Total Months: {totalMonths}")        
    print(f"Total: ${total}")
    print(f"Average Change: ${round(profitLossChangeRate,2)}")
    print(f"Greatest Increase in Profits: {profitLossMaxDate} (${profitLossMax})")
    print(f"Greatest Decrease in Profits: {profitLossMinDate} (${profitLossMin})")


    
                         
   
        


    