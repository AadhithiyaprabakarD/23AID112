def process_grades(students):
    passing_count = 0  
    failing_names = set() 

    for student in students:
        name = student['name']
        grades = student['grades']
        attendance = student['attendance']

        try:
            if not grades:
                raise ValueError(f"Student '{name}' has no grades.")
        except ValueError as e:
            
            print(e)  
            continue

        avg_grade = sum(grades) / len(grades) 
        
        if avg_grade >= 70 and attendance >= 80:
            passing_count += 1 
        else:
            failing_names.add(name) 
    
    
    return passing_count, failing_names

students = [
    {'name': 'Alice', 'grades': [85, 90, 78], 'attendance': 90},
    {'name': 'Bob', 'grades': [65, 70, 60], 'attendance': 75},
    {'name': 'Charlie', 'grades': [], 'attendance': 85}  # Will trigger error
]
print(process_grades(students))
