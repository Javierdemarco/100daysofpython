with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file1:
    file_2_data = file1.readlines()

result = [int(n) for n in file_1_data if n in file_2_data]

# Write your code above 👆

print(result)
