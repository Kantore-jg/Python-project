student_dict = {
    "student": ["Angela","Kantore","Dave"],
    "score": [56,76,98]

}




import pandas

student_data_frame = pandas.DataFrame(student_dict)
for (key,value) in student_data_frame.items():
    pass
    #print(value)
print(student_data_frame)
for (index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
