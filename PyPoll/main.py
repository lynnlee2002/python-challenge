# Creating the file path
file_path = "/Users/linh/Desktop/Linh/Classwork/Lectures/02-Homework/03-Python/python-challenge/PyPoll/Resources/election_data.csv"
# Module for reading CSV files
import csv

# Creating a variable for the number of votes cast
vote_count = 0

# Creating a candidate list and candidate vote dictionary
candidate_list = []
candidate_vote = {}

# Reading using csv module
with open (file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skipping the headers
    headerline = next(csvfile)

    # Iterating throught the whole file
    for row in csvreader:

        # Adding one vote after looping through each row
        vote_count +=1

        # Creating a variable for each candidate name
        candidate_name = row[2]

        # If a candidate's name is not in the candidate list
        if candidate_name not in candidate_list:

            # If true, then adding it to the candidate list
            candidate_list.append(row[2])

            # Creating candidate_name key and setting up vote counts as the key's corresponding values 
            # Resetting vote count when jumping to the following candidate
            candidate_vote[candidate_name] = 0

        # Adding one count for each candidate in the dictionary if the next candidate 
        # is the same the current one, and show the key/
        candidate_vote[candidate_name] += 1
    
    #Printing the first section to the terminal 
    print("Election Results")
    print("------------------------------")

    # Printing total number of votes cast to the terminal
    print(f"Total Votes: {vote_count}")
    print("------------------------------")

    # Creating a variable for the maximum vote count
    max_count = 0

    # Creating a variable for the winning candidate
    winning_candidate = ""

    # Looping through each candidate name key in the candidate_vote dictionary
    for candidate_name in candidate_vote:
            
            # Retrieivng all candidates' votes from the dictionary 
            individual_vote_extracted = candidate_vote.get(candidate_name)

            # Calculating each candidate's vote percentage
            percentage = individual_vote_extracted/vote_count * 100

            # Creating a variable for printing the election result of each candidate
            candidate_vote_stats = (f"{candidate_name}: {round(percentage,3)}% ({individual_vote_extracted})")
            print(candidate_vote_stats)

            # Finding the winning candidate with their highest vote
            if individual_vote_extracted > max_count:
                max_count = individual_vote_extracted
                winning_candidate = candidate_name
    
    # Printing the remaining to the terminal
    print("------------------------------")
    print(f"Winner: {winning_candidate}")           
    print("------------------------------")

#Creating a text file
text_file = "/Users/linh/Desktop/Linh/Classwork/Lectures/02-Homework/03-Python/python-challenge/PyPoll/analysis/Election_Results.txt"

# Writing the election ressults to the text file
with open(text_file, 'w') as text:
    text.write("Election Results\n")
    text.write("------------------------------\n")
    text.write(f"Total Votes: {vote_count}\n")
    text.write("------------------------------\n")
    for candidate_name in candidate_vote:
        individual_vote_extracted = candidate_vote.get(candidate_name)
        percentage = individual_vote_extracted/vote_count * 100
        candidate_vote_stats = (f"{candidate_name}: {round(percentage,3)}% ({individual_vote_extracted})")
        text.write(f"{candidate_vote_stats}\n")

        if individual_vote_extracted > max_count:
            max_count = individual_vote_extracted
            winning_candidate = candidate_name

    text.write("------------------------------\n")
    text.write(f"Winner: {winning_candidate}\n")           
    text.write("------------------------------")



 

    