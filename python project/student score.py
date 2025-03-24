student_scores={"Harry":81,
                "Ron":78,
                "Hermione":99,
                "Draco":74,
                "neville":62}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="Outstanding"
    elif score>80:
        student_grades[student]="Exceeds expectations"
    elif score>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail!!!!"
    for name in student_grades:
        grades=student_grades[name]
#grades=student_grades[]
#print(score)
#print(student_scores)
    print(f"{student}==>{grades}")

#Nesting dictionnary in dictionnary

'''travel_log={"burundi":{"city_visited":["bujumbura","Gitega","Muyinga","Ngozi"],"total_visit":4},
            "Rwanda":{"city_visited":["kigari","musanze","Kamenge"],"total_visit":3}}'''
# #Nesting dictionnary in a list
# travel_log=[{"country":"burundi",
#              "city_visited":["bujumbura","Gitega","Muyinga","Ngozi"],
#                 "total_visit":4},
#             {"country":"Rwanda",
#              "city_visited":["kigari","musanze","Kamenge"],
#               "total_visit":3}]
# def add_newCountry(country,total_visited,city_visited):
#     #country=input("enter a country: ")
#     city_visited=[]
#     #city_visiteds=input("donner les villes que vous voulez visiter: ")
#     #total_visited=int(input("enter a total number of city visited"))
#     new_country={}
#     #city_visited.append(city_visiteds)
#     total_visited=len(city_visited)
#     new_country["country"]=country
#     new_country["city_visited"]=city_visited
#     new_country["total_visited"]=total_visited
#     travel_log.append(new_country)
# add_newCountry("Russia",2,["Moscow","saint petersburg"])
# print(travel_log)
