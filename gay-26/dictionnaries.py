import random
names = ["Alex","Beth","Calorine","Dave","Eleanor","Freddie"]

students_scores = {student:random.randint(1,100) for student in names}

passed_student = {student:score for (student,score) in students_scores.items() if score>59}
print(passed_student)