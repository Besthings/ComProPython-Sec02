# Sample data structure for employee performance
performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90],
        "Bob": [70, 75, 78, 80],
        "Charlie": [66, 65, 70, 72]
    },
    "Engineering": {
        "David": [90, 92, 94, 95],
        "Eve": [85, 88, 87, 90],
        "Frank": [88, 87, 86, 85]
    },
    "HR": {
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73],
        "Ivan": [60, 62, 64, 66]
    }
}

# 1. Calculate the average performance score for each employee.
def calculate_average_scores(data):
    average_scores = {}
    for department, employees in data.items():
        average_scores[department] = {}
        for employee, scores in employees.items():
            average_scores[department][employee] = sum(scores) / len(scores)
    return average_scores

average_scores = calculate_average_scores(performance_data)

# 2. Identify the top performer in each department based on their average score.
def top_performers_per_department(data):
    top_performers = {}
    for department, employees in data.items():
        top_employee = max(employees.items(), key=lambda x: sum(x[1]) / len(x[1]))
        top_performers[department] = (top_employee[0], sum(top_employee[1]) / len(top_employee[1]))
    return top_performers

top_performers = top_performers_per_department(performance_data)

# 3. Determine the department with the highest average performance score.
def department_with_highest_average(data):
    department_averages = {}
    for department, employees in data.items():
        total_scores = sum(sum(scores) for scores in employees.values())
        num_scores = sum(len(scores) for scores in employees.values())
        department_averages[department] = total_scores / num_scores
    top_department = max(department_averages, key=department_averages.get)
    return top_department, department_averages[top_department]

top_department, department_avg_score = department_with_highest_average(performance_data)

# 4. Find employees who have shown continuous improvement.
def employees_with_continuous_improvement(data):
    continuous_improvement = {}
    for department, employees in data.items():
        continuous_improvement[department] = []
        for employee, scores in employees.items():
            if all(earlier < later for earlier, later in zip(scores, scores[1:])):
                continuous_improvement[department].append(employee)
    return continuous_improvement

improved_employees = employees_with_continuous_improvement(performance_data)

# 5. Generate a summary report.
def generate_summary_report(average_scores, top_performers, top_department, department_avg_score, improved_employees):
    report = "Summary Report:\n"
    for department, employees in average_scores.items():
        report += f"Department: {department}\n"
        for employee, avg_score in employees.items():
            report += f"  {employee}: Average Score = {avg_score:.2f}\n"
        top_employee, top_score = top_performers[department]
        report += f"Top Performer: {top_employee} with Average Score = {top_score:.2f}\n\n"
    
    report += f"Best Department: {top_department} with Average Score = {department_avg_score:.2f}\n\n"

    report += "Employees with Continuous Improvement:\n"
    for department, employees in improved_employees.items():
        if employees:
            report += f"Department: {department}\n"
            for employee in employees:
                report += f"  {employee}\n"
        else:
            report += f"Department: {department} - None\n"

    return report

summary_report = generate_summary_report(average_scores, top_performers, top_department, department_avg_score, improved_employees)
print(summary_report)