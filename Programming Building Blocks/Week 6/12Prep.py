youngest_name = ""
youngest_age = 999

#Predefined people list
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

#iterate
for person in people:
    #Split
    item = person.split(" ")
    name = item[0]
    age = item[1]
    #print name and age
    print(f"Name : {name} Age : {age}")
    #find youngest
    #store youngest
    if age < youngest_age:
        youngest_age = age
        youngest_name = name
    
    