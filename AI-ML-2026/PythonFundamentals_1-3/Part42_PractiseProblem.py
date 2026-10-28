# Student Enrolments

# Given a list of tuples with info (name, subject):

# List all unique courses
# List students enrolled in English
# Create dictionary (student, set of courses)

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

print("---------------List all unique courses------------------------")
courses_set = set()
for tup in info:
     courses_set.add(tup[1])

print("Unique courses:", courses_set)


print("---------------List students enrolled in English *Approach 1*------------------------")
for tup in info:
    if tup[1] == "English":
        print("Student enrolled in English:", tup[0])


print("---------------List students enrolled in English *Approach 2*------------------------")
for name, course in info:
    if course == "English":
        print("Student enrolled in English:", name)

print("---------------Create dictionary (student, set of courses)------------------------")
dict_student_courses = {}
for name, course in info:
    if(dict_student_courses.get(name) == None):
        dict_student_courses[name] = set()

        dict_student_courses.update({name: set()})
        dict_student_courses[name].add(course)

    else :
        dict_student_courses[name].add(course)

print(dict_student_courses)        