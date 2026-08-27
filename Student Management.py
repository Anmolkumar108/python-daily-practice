students = {
    "student1": {
        "name": "Anmol Singh",
        "age": 19,
        "course": "BCA",
        "college": "SIT Aurangabad",
        "cgpa": 8.81
    },

    "student2": {
        "name": "Vicky Singh",
        "age": 24,
        "course": "B.Tech (CSE)",
        "college": "Giani Zail Singh College of Engineering & Technology, Bathinda",
        "cgpa": 7.8
    },

    "student3": {
        "name": "Hritik Nayan",
        "age": 20,
        "course": "BCA",
        "college": "SIT Aurangabad",
        "cgpa": 8.1
    }
}


choice = input("What information do you want? ").lower().strip()

# Extra spaces ko remove karna
choice = choice.replace("_", " ")


# Student name identify karna
if "student1" in choice or "student 1" in choice:
    student = students["student1"]

elif "student2" in choice or "student 2" in choice:
    student = students["student2"]

elif "student3" in choice or "student 3" in choice:
    student = students["student3"]

else:
    print("Student not found.")
    exit()


# Only Student Name
if "name" in choice and "student" in choice:
    print("Name:", student["name"])

# Only age
elif "age" in choice:
    print("Age:", student["age"])

# Only course
elif "course" in choice:
    print("Course:", student["course"])

# Only college
elif "college" in choice or "collage" in choice:
    print("College:", student["college"])

# Only CGPA
elif "cgpa" in choice or "sgpa" in choice:
    print("CGPA/SGPA:", student["cgpa"])


else:
    print("\n--- Student Information ---")
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("College:", student["college"])
    print("CGPA/SGPA:", student["cgpa"])