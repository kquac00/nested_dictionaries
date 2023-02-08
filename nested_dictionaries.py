# 1. Update Values in Dictionaries and Lists

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
#Change the value 20 in z to 30

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
x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students[0])

sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

z[0]["y"] = "30"
print(z[0])


# 2. Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name':  'David', 'last_name' : 'Ferrari'},
    {'first_name' : 'Jeff', 'last_name' : 'Smith'}
]

def iterateDictionary(incoming_list):
    for diction in incoming_list:
        print(f"First Name: { diction['first_name']} : Last Name { diction['last_name']}")
        for key in diction:
            print(f"{key} - {diction[key]}")

iterateDictionary(students)
        
# 3. Get Values From a List of Dictionaries
        students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name':  'David', 'last_name' : 'Ferrari'},
    {'first_name' : 'Jeff', 'last_name' : 'Smith'}
]

teachers = [
    {'first_name':  'Mitch', 'last_name' : 'Jason'},
    {'first_name' : 'John', 'last_name' : 'Rose'},
    {'first_name':  'Dave', 'last_name' : 'Doe'},
    {'first_name' : 'Jeff', 'last_name' : 'Peters'}
]

def iterateDictionary2(key_name, Some_list):
    for dic in Some_list:
        if key_name in dic:
            print(dic[key_name])
        else: 
            print("key not found") 
        
iterateDictionary2("last_name",teachers)

#4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for value in range(len(some_dict[key])): 
            print(some_dict[key][value])  
        print("")

printInfo(dojo)