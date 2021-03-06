# =======================
# 1. Update Values in Dictionaries and Lists
# =======================

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1a.) -> Change - value 10 in x to 15. x should now be [[5,2,3],[15,8,9]]

x[1][0] = 15 
print (x[1][0])

# 2b.) -> Change last_name of first student from 'Jordan' to 'Bryant'

students[0]['last_name'] = 'Bryant'
print (students[0]['last_name'])

# 3c.) -> Change 'Messi' to 'Andres' in the sports_directory

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])

# 4d.) -> Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 

z[0]['y'] = 30
print(z[0]['y'])

# =======================
# 2. Iterate Through a List of Dictionaries
# =======================

# Create a function iterateDictionary(some_list) -> function loops through each dictionary in the list and prints each key and associated value.

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(0, len(students)):
        print (f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}") #yay, fstrings! 

iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# =======================
# 3. Get Values from a List of Dictionaries
# =======================
# create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.


def iterateDictionary2(key_names, someList):
    for i in range(0,len(someList)):
        print(someList[i][key_names])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


# ex. iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# iternateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

# =======================
# 4. Iterate Through a Dictionary with List Values
# =======================

# create a function printInfo(some_dict) that gives a dictionary whose values are all lists, print the names of each key along with the size of its list, and print associated values within each key's list

def printInfo(someList):
    for key in someList:
        print(f"{len(someList[key])}{key.upper()}")
        for i in range(0, len(someList[key])):
            print(someList[key][i])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


