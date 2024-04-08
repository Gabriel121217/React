import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Function that opens csv file. 
# It returns a list containing the rows of the csv file
# Each row is stored as a list
file = "5_years_financial_data.csv"

def read_file(file_name):
    unfiltered = []

    with open(file_name, 'r') as file:             #Opens the csv file
        csvreader = csv.reader(file)

        for row in csvreader:                      #Stores each row in a list
            unfiltered.append(row)
    
    unfiltered.pop(0)
    return (unfiltered)

def extract_month_year(date):
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date, '%d/%m/%Y')

        # Extract the month from the datetime object
        month = date_obj.strftime('%B')

        # Extract the year from the datetime object
        year = date_obj.strftime('%Y')

        return month, year
    
    except ValueError:
        return 'Invalid date format'

# Function that sorts the entries by year
# Entries are sorted by year in a dictionary 
def sorted_by_years(unfiltered):                  
    all_years = {}
    for entry in unfiltered:                              
        month, year = extract_month_year(entry[0])                      # Identifies year

        if  year in all_years:                      # Adds in the entry to appropriate dictionary key if the year was added
            all_years[year].append(entry)

        else:                                       # If the year was not stored before, adds new key into the dictionary
            all_years[year] = [entry]
    return (all_years)


# function that sorts entries into categories
# Entries are sorted by year in a dictionary 
def sorted_by_category(unfiltered):
    all_expenses = {}
    
    for entry in unfiltered:
        category = entry[1]
        if category in all_expenses:
            all_expenses[category].append(entry)

        else:
            all_expenses[category] = [entry]

    return(all_expenses)


# takes in a dictionary of entries sorted by category
# tallies up the entries by category 
def tally(sorted):
    summary = {}

    for keys in sorted:
        total = 0

        for entry in sorted[keys]:
            cost =float(entry[2])
            
            total += cost
        summary[keys]= round(total,2)

    return(summary)


#plots pie chart based on processed dictionary
def pie (dictionary):
    mylabels = []
    entries = []
    for keys in dictionary:
        mylabels.append(keys)
        entries.append(dictionary[keys])
    
    expenses = np.array(entries)

    plt.pie(expenses, labels = mylabels)
    plt.show()

pie(tally(sorted_by_years(read_file(file))))

