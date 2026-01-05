python={"Remya","Raju","Sona"}
data_science={"Anju","Arya","Rahul","Anuja"}
python.add("Ravi")
print(python)
data_science.remove("Arya")
print(data_science)
print(python&data_science)
print(python-data_science)
print(python|data_science)
course={
    "python":3,
    "data_science":4
}
print(course)
for x,y in course.items():
    print("course:",x,"students:",y)
expected_growth = {}
for course, count in course.items():
    expected_growth[course] = count * 2
    print(expected_growth)



