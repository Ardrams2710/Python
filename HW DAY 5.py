Frontend_course={"Vasuki","Abhirami","Aromal","Ajay"}
Backend_course={"Anu","Arun","Vishnu"}
Backend_course.add("Remya")
Frontend_course.remove("Abhirami")
print(Frontend_course)
print(Frontend_course&Backend_course)
print(Backend_course-Frontend_course)
print(Frontend_course|Backend_course)
course={
    "Frontend":4,
    "Backend":3
}
print(course)
for x,y in course.items():
    print("course:",x,"students:",y)
new_dic = {
    **course,
    "Fullstack": sum(course.values())
}
print("new course values:",new_dic)