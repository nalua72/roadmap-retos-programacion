from functools import reduce
from datetime import datetime


integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

even = list(filter(lambda x: x%2 == 0, integer))
print(even)
cubed = list(map(lambda x: x**3, integer))
print(cubed)
sumcum = reduce(lambda a,b:a+b, integer)
print(sumcum)

"""
Extra
"""


def main():

    students = [
        {"name": "Jose", "birthdate": "10-07-1972", "grades": [5, 8.5, 3, 10]},
        {"name": "Isabel", "birthdate": "06-10-1970", "grades": [1, 9.5, 2, 4]},
        {"name": "Saul", "birthdate": "17-10-2010", "grades": [9.7, 9.5, 8.5, 10]},
        {"name": "Jaime", "birthdate": "25-01-1980",
            "grades": [10, 9, 9.7, 9.9]}
    ]
    def calculate_mean(marks: list[int]) -> int:
        return reduce(lambda a,b:a+b, marks)/len(marks)
    
    #Imprime la lista de estudiantes y su nota media
    print(f"lista de estudiantes y nota media: ")
    list_student_by_mean = list(map(lambda student: {"name": student["name"], "mean": calculate_mean(student["grades"])}, students))
    print(list_student_by_mean)
    
    # #Imprime la lista de estudiantes con notas medias superior a 9
    print(f"\nlista de estudiantes con media superior a 9: ")
    list_best_students = list(filter(lambda student: calculate_mean(student["grades"])>9, students))
    print(list_best_students)

    #Imprime la lista de estudiantes ordenados por fecha de nacimiento
    print(f"\nlista de estudiantes ordenados por edad: ")
    birthday_ordered = sorted(students, key=lambda student: datetime.strptime(student["birthdate"], "%d-%m-%Y"))
    print(birthday_ordered)

    #Imprime la nota mas alta
    print(f"\n La nota más alta es:")
    print(max(map(lambda student: max(student["grades"]), students)))

if __name__ == "__main__":
    main()