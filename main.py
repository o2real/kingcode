programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)


#Create an empty dictionary.
empty_dictionary = {}

#Wipe
# programming_dictionary = {}
# print(programming_dictionary)

#Edit
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#loop
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#--------------------------------------------- 

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}



for student in student_scores :
  score = student_scores[student]
  if score > 90 :
    student_grades[student] = "Outstanding"
  elif score > 80 :
    student_grades[student] = "Exceeds Expectations"
  elif score > 70 :
    student_grades[student] = "Acceptable"
  else :
    student_grades[student] = "Fail"


print(student_grades)


#--------------------

travel_log = {
  "France" :{"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" :12},
  "Germany" :{"cities_visited" :["Berlin", "Hamburg", "Stuttgart"], "total_visits" :12},
}

#Nesting Dictionary in a list

travel_log = [
  {
    "country" : "France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"], 
    "total_visits" : 12
  },
  {
    "country" : "Germany", 
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits" : 12
  },
]


#아 오늘 블로그 하느라 시간 다 날랐네

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, times_visited, cities_visited) :
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)
# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
