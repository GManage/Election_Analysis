# The Data we nees to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Percentage of votes each candidate won
# Total number of votes each candidate won
# The winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

#####################################################################

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
    #txt_file.write("Hello World")

# Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")

# Write three counties to the file AT ONE TIME!
      # txt_file.write("Arapahoe, Denver, Jefferson")

# Write three counties to the file.
    txt_file.write("Counties in the Election\n------------------------------\nArapahoe\nDenver\nJefferson")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    print(headers)
