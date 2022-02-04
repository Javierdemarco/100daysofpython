from random import randint

list = [1,2,3]
new_list = []
for n in list:
    add_1= n + 1
    new_list.append(add_1)

# [new_item for item in list]
new_list = [n + 1 for n in list]
new_list = [letter for letter in "Javier"]
new_list = [n * 2 for n in range(1,5)]

# [new_item for item in list if test]
names = ["Javier", "Paula", "Jhon", "Dave"]
new_list = [name for name in names if len(name) > 4]
new_list = [name.upper() for name in names if len(name) > 4]

# {new_key : new_value for item in list if test}
# {new_key : new_value for (key,value) in dict.item() if test}
student_scores = {student : randint(0, 100) for student in names}
passed_students = {student : score for student, score in student_scores.items() if score >=
    60}

# Iterate over pandas dataframe
student_dict = {
    "student": ["Javier", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_df = pandas.DataFrame(student_dict)


# Loop through rows of a data frame
for index, row in student_df.iterrows():
    if row.student == "Javier":
        print(row.student)
