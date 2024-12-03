grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = {}
students_list = sorted(students)
for i, student in enumerate(students_list):
    average_grade = sum(grades[i]) / len(grades[i])
    average_grades[student] = average_grade

print(average_grades)