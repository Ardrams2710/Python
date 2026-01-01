multiline_string="""A Python course offers a comprehensive introduction to the Python 
programming language, a high-level, general-purpose language renowned for its simplicity
and readability. Courses typically cover foundational topics such as variables, data types,
control structures (like loops and conditional statements), functions, and modules, with
many progressing to more advanced concepts such as object-oriented programming (OOP) 
and file handling."""
multiline_string=multiline_string.strip()
print("length of the multiline string",len(multiline_string))
print("first character",multiline_string[0])
print("last character",multiline_string[-1])
print("preview(first 50 characters)",multiline_string)
replaced_multilinestring=multiline_string.replace("python","PYTHON")
print("after replacement\n",replaced_multilinestring)
lowercase_multilinestring=multiline_string.lower()
print("lowercase multiline string\n",lowercase_multilinestring)
words=multiline_string.split()
print("list of words",words)
print("The course description is {} characters long and has {} words".format(len(multiline_string),len(words)))
