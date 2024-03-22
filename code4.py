def calculate_average_grades():
    grades = []
    while True:
        grade = input("Enter a grade (-1 to stop): ")
        if grade == "-1":
            break
        grades.append(int(grade))
    average = sum(grades) / len(grades)
    print("Average:", int(average))
    print("Grades in order:", *grades)

# Example usage
calculate_average_grades()
