def search_employees(employees, target_dept):
    high_salary_ids = set()
    dept_count = {target_dept: 0}

    found_in_dept = False 

    for emp in employees:
        emp_id, name, dept, salary = emp

        if dept == target_dept:
            found_in_dept = True

            if salary > 50000:
                high_salary_ids.add(emp_id)
                dept_count[target_dept] += 1

    try:
        if not found_in_dept:
            raise ValueError(f"No employees in department '{target_dept}'.")
    except ValueError as e:
        print(e)
        return {}

    return dept_count

employees = [
    (1, "Alice", "HR", 60000.0),
    (2, "Bob", "IT", 45000.0),
    (3, "Charlie", "HR", 55000.0)
]
print(search_employees(employees, "HR"))
