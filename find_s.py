#-------------------------------------------------------------------------
# AUTHOR: Seungyun Lee
# FILENAME: find_s.py
# SPECIFICATION: Finding a maximally specific hypothesis of the given data set by using "Find-S algorithm"
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n Print only the Positive Instaces: ")
for entry in db:
    if entry[4] == 'Yes':
        print(entry)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
for entry in db:
    if entry[4] == 'Yes': # break out after finding the first positive instance
        hypothesis = entry
        break
print("\n After finding the first positive training data and assigning it to the hypothesis:")
print(hypothesis)

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here
for entry in db:
    if entry[4] == 'Yes':
        for i in range(len(entry)-1):
            if entry[i] != hypothesis[i]: # assign '?' if they values are different
                hypothesis[i] = '?'

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:")
print(hypothesis)