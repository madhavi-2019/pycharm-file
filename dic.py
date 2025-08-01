std_names={'sudha':'45', 'raju':'46','surya':'76','ravi':'no marks'}
std_marks=input("Enter the student's_names:")
if std_marks in std_names:
    print(f"{std_marks}'s marks: {std_names[std_marks]}")
else:
    print(f"Student '{std_marks}' not found in the records.")
