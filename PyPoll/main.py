# PyPoll Challenge
# This script analyzes election data from a CSV file to calculate:
# - Total number of votes cast
# - Complete list of candidates who received votes
# - Percentage of votes each candidate won
# - Total number of votes each candidate won
# - Winner of the election based on popular vote
# Import required dependencies
import csv
import os
from pathlib import Path  # Added for better path handling

# Define the full path to your files
# Update these paths to match your actual file location
base_path = "/Users/luiscarloslopez/Desktop/Starter_Code/PyPoll"
file_to_load = os.path.join(base_path, "Resources", "election_data.csv")
file_to_output = os.path.join(base_path, "analysis", "election_analysis.txt")

# Initialize variables to store election data
total_votes = 0           # Counter for total votes
candidate_votes = {}      # Dictionary to store each candidate's vote count
candidate_percentages = {} # Dictionary to store each candidate's vote percentage
winner = ""              # Variable to store winner's name
winning_count = 0        # Variable to store winning vote count
 
# Read the CSV file
try:
    with open(file_to_load) as election_data:
        # Create CSV reader object
        reader = csv.reader(election_data)
 
        # Skip header row
        header = next(reader)
 
        # Process each vote/row in the CSV file
        for row in reader:
            # Increment total vote counter
            total_votes += 1
 
            # Get candidate name from current row
            candidate_name = row[2]
 
            # If candidate appears for first time, add to dictionary
            if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 0
 
            # Add vote to candidate's count
            candidate_votes[candidate_name] += 1
 
    # Calculate percentage of votes for each candidate
    # and determine winner
    for candidate in candidate_votes:
        # Calculate vote percentage
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate] = percentage
 
        # Determine winning vote count and candidate
        if votes > winning_count:
            winning_count = votes
            winner = candidate
 
    # Prepare output string
    output = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"  # Format with comma for thousands
        f"-------------------------\n"
    )
 
    # Add each candidate's results to output
    for candidate in candidate_votes:
        output += (f"{candidate}: {candidate_percentages[candidate]:.3f}% "
                  f"({candidate_votes[candidate]:,})\n")
 
    # Complete output with winner
    output += (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )
 
    # Print results to terminal
    print(output)
 
    # Save results to text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
 
    print(f"Results saved to {file_to_output}")
 
except FileNotFoundError:
    print(f"Error: Cannot find {file_to_load}")
    print("Make sure 'election_data.csv' is in the Resources folder")
except Exception as e:
    print(f"An error occurred: {str(e)}")
 