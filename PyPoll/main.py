import csv

# Set path for file
csvpath = "PyPoll\Resources\election_data.csv"

# Open the CSV using the UTF-8 encoding
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Total number of votes cast
    total_votes=0
    #To find each candidate votes declared votes1 for cnadidate1 and respectively
    votes1 = 0
    votes2 = 0 
    votes3 = 0
    #declared variables for candidates 
    candidate1="Charles Casper Stockham"
    candidate2="Diana DeGette"
    candidate3="Raymon Anthony Doane"
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #loopint through the csv file to count the total votes for each candidate
    for row in csvreader:
        total_votes= total_votes + 1
        if row[2] == candidate1:
            votes1 = votes1 + 1
        if row[2] == candidate2:
            votes2 =votes2 + 1
        if row[2] == candidate3:
            votes3 =votes3 + 1
    #Finding the pernets for each candidate
    percent_votes1= votes1 /total_votes *100
    percent_votes2= votes2 /total_votes *100
    percent_votes3= votes3 /total_votes *100

    fileWrite = open("PyPoll/Analysis/file.txt", "w")

    #printing the financial ananlysis as requested in to the text file
    print("--------------------------------", file = fileWrite)
    print("Election Results", file = fileWrite)
    print("--------------------------------", file = fileWrite)
    print(f"Total Votes: {total_votes}", file = fileWrite)
    print("--------------------------------", file = fileWrite)
    print(f"{candidate1}: {round(percent_votes1,3)}% ({votes1})", file = fileWrite)
    print(f"{candidate2}: {round(percent_votes2,3)}% ({votes2})", file = fileWrite)
    print(f"{candidate3}: {round(percent_votes3,3)}% ({votes3})", file = fileWrite)
    print("--------------------------------", file = fileWrite)
    print(f"Winner: {candidate2}", file = fileWrite)
    print("--------------------------------", file = fileWrite)

    fileWrite.close()

    #priting the results as requested.
    print("--------------------------------")
    print("Election Results")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")
    print(f"{candidate1}: {round(percent_votes1,3)}% ({votes1})")
    print(f"{candidate2}: {round(percent_votes2,3)}% ({votes2})")
    print(f"{candidate3}: {round(percent_votes3,3)}% ({votes3})")
    print("--------------------------------")
    print(f"Winner: {candidate2}")
    print("--------------------------------")
    
   
   

