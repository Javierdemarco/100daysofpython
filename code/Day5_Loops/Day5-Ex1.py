# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum = 0
number_of_students = 0
for n in student_heights:
    sum += n
    number_of_students += 1

average = round(sum / number_of_students)

print(average)


#Write your code below this row 👇
