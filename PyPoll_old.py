# Import the datetime class from the datetime module.
import datetime as dt
import csv
import os

# Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")


# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# Write some data to the file.
# outfile.write("Hello World")

# Close the file
# outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # Write three counties to the file.
    # txt_file.write("Arapahoe\n")
    # txt_file.write("Denver\n")
    # txt_file.write("Jefferson\n")
    # txt_file.write("Arapahoe, Denver, Jefferson")
    # txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

# 1. The total number of votes to cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winnder of the election vased on popular vote.
