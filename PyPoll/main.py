import csv

# Set path for file
csvpath = "PyPoll\Resources\election_data.csv"
#Took the help of Class Practice workouts and prof class exercises.
#Took help from Stackoverflow and Kaggle and Christopher Madden(TA) help.
# Open the CSV using the UTF-8 encoding
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Total number of votes cast
    total_votes=0
    #List of candidatelist and candidatevotes
   
    candidatesList = []
    candidatevotes = []
  
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV.Header: {csv_header}") not required for the display of the execution
    #looping through the csv file to count the total votes for each candidate
            
    for onerowdata in csvreader:
        total_votes= total_votes + 1
        if onerowdata[2] not in candidatesList:
            candidatesList.append(onerowdata[2])
            candidatevotes.append(1)
        else:
            candidateindex = candidatesList.index(onerowdata[2])
            candidatevotes[candidateindex] = candidatevotes[candidateindex] + 1
               
    #Finding the candidate percents
    candidatePercentvotes = [num * 100 / total_votes for num in candidatevotes ] 
    winner=candidatesList[candidatevotes.index(max(candidatevotes))]

    #printing the financial ananlysis as requested in to the text file
    fileWrite = open("PyPoll/Analysis/file.txt", "w")
    i=0
    print("--------------------------------", file = fileWrite)
    print("Election Results", file = fileWrite)
    print("--------------------------------", file = fileWrite)
    print(f"Total Votes: {total_votes}", file = fileWrite)
    print("--------------------------------", file = fileWrite)
    for num in candidatePercentvotes:
        print(f"{candidatesList[i]}: {round(candidatePercentvotes[i],3)}% ({candidatevotes[i]})", file = fileWrite)  
        i = i+1
    print("--------------------------------", file = fileWrite)
    print(f"Winner: {winner}", file = fileWrite)
    print("--------------------------------", file = fileWrite)
    fileWrite.close()


    
    #priting the results as required.
    i = 0
    print("--------------------------------")
    print("Election Results")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")
    for num in candidatePercentvotes:
        print(f"{candidatesList[i]}: {round(candidatePercentvotes[i],3)}% ({candidatevotes[i]})")  
        i = i+1
    print("--------------------------------")
    print(f"Winner: {winner}")
    print("--------------------------------")



    



    
  
 

   

   
    
   
   

