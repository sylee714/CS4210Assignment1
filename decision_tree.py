#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

age_values = {'Young' : 1, 'Prepresbyopic' : 2, 'Presbyopic' : 3}
spectacle_pres_values = {'Myope' : 1, 'Hypermetrope' : 2}
astigmatism_values = {'Yes' : 1, 'No' : 2}
tear_prod_rate_values = {'Normal' : 1, 'Reduced' : 2}
recommend_lenses_values = {'Yes' : 1, 'No' : 2}

def transformEntry(entry):
    new_entry = []

    new_entry.append(age_values[entry[0]])
    new_entry.append(spectacle_pres_values[entry[1]])
    new_entry.append(astigmatism_values[entry[2]])
    new_entry.append(tear_prod_rate_values[entry[3]])

    return new_entry

def transformData(db):
    x = []

    for entry in db:
        x.append(transformEntry(entry))

    return x

def transformLabel(db):
    y = []

    for entry in db:
        last_index = len(entry) - 1
        y.append(recommend_lenses_values[entry[last_index]])

    return y

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print(db)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
X = transformData(db)
print(X)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = transformLabel(db)
print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()