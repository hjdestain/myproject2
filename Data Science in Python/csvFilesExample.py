# Week: 1
# Lesson: Python Demonstration: Reading and Writing CSV Files
# Date Started: 18 May 2020
# Date Finished: 18 May 2020

# import csv module to assist in reading csv file
import csv

# in the notebook, %precision 2 sets the float precision to two

# organize the csv file into a list of dictionaries, sample elements, and find the length
with open('Sample100.csv') as csvfile:
    # uses a sample csv file found online
    Sample100 = list(csv.DictReader(csvfile))
        # DictReader converts the file into a dictionary, which are then put into lists
print("The first three elements are:\n",Sample100[:3],"\n")    
print("The number of dictionaries is:",len(Sample100),"\n")

# view the column names using the key method
print("The keys are:",Sample100[0].keys(),"\n")
    # [0] ensures the method is referring to a dictionary,
    # not the entire list (which does not have key values)

# calculate average leave
averageLeave = sum(float(d['Leave']) for d in Sample100) / len(Sample100)
    # d is an individual dictionary
    # d['Leave'] refers to the number associated with the key 'Leave'
    # the for loop iterates it over all dictionaries in Sample100
print("The average leave is:",averageLeave,"\n")

# obtain unique values present for a certain key
description = set(d['Description'] for d in Sample100)
    # set is a collection of unordered and unindexed values, written with {}
    # returns the unique values for the 'Leave' key in a set
print("The descriptions are:",description,"\n")

# obtain average leave for each unique value
leaveByDescription = []
for x in description:
    sumLeave = 0
    descriptionCount = 0
    for d in Sample100:
        if d['Description'] == x:
            sumLeave += float(d['Leave'])
            descriptionCount += 1
    average = sumLeave / descriptionCount
    leaveByDescription.append((x, average))
print(leaveByDescription)

