import csv
#with open("input.txt","r") as file:
#    content = file.read()
    
#print(content.upper())

data = [
    ["Ashlesh", 100],
    ["John", 90],
    ["Liam", 85],
    ["ABD", 95],
    ["Ash", 100]
]

total_grade=0
count = 0
with open("pythonNew\students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
print("Students.csv has been created successfully")

with open("pythonNew\students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        name,grade = row
        total_grade += int(grade)
        count +=1
        
average = total_grade/count

with open("average.txt", "w") as output_file:
    output_file.write(f"The average grade is {average:.1f}")
    
print("Average grade calculated and saved in 'average.txt'")

