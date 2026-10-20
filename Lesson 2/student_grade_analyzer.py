"""Student Grade Analyzer - Starter Code

Complete every section marked TODO. Keep this file and grades.txt in the
same folder. Rename the completed file to student_grade_analyzer.py.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""

    if grade >= 90:
        classification = "Excellent"
        status = "Passed"
    elif grade >= 85:
        classification = "Very Good"
        status = "Passed"
    elif grade >= 80:
        classification = "Good"
        status = "Passed"
    elif grade >= 75:
        classification = "Satisfactory"
        status = "Passed"
    else:
        classification = "Needs Improvement"
        status = "Failed"

    return classification, status


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""

    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                # Skip blank lines
                if not line:
                    continue

                # Split the record into fields
                fields = line.split(",")

                # Accept only records with exactly 3 fields
                if len(fields) != 3:
                    continue

                student_id = fields[0].strip()
                name = fields[1].strip()
                grade_text = fields[2].strip()

                try:
                    grade = float(grade_text)
                except ValueError:
                    continue

                # Accept only grades from 0 to 100
                if grade < 0 or grade > 100:
                    continue

                student = {
                    "student_id": student_id,
                    "name": name,
                    "grade": grade
                }

                students.append(student)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except OSError:
        print(f"Error: Could not read the file '{filename}'.")

    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""

    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student["grade"]

        # Add grade to the total
        total_grade += grade

        # Count passed and failed students
        classification, status = classify_grade(grade)

        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        # Find highest grade
        if grade > highest_student["grade"]:
            highest_student = student

        # Find lowest grade
        if grade < lowest_student["grade"]:
            lowest_student = student

    average = total_grade / len(students)

    statistics = {
        "number_of_students": len(students),
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest_student": highest_student,
        "lowest_student": lowest_student
    }

    return statistics


def display_students(students):
    """Display all student records in a formatted table."""

    print("\nSTUDENT RECORDS")
    print("-" * 85)
    print(
        f"{'Student Number':<16}"
        f"{'Student Name':<20}"
        f"{'Grade':<10}"
        f"{'Classification':<22}"
        f"{'Status':<10}"
    )
    print("-" * 85)

    for student in students:
        classification, status = classify_grade(student["grade"])

        print(
            f"{student['student_id']:<16}"
            f"{student['name']:<20}"
            f"{student['grade']:<10.2f}"
            f"{classification:<22}"
            f"{status:<10}"
        )

    print("-" * 85)


def display_statistics(statistics):
    """Display the calculated class statistics."""

    print("\nCLASS STATISTICS")
    print("-" * 40)

    print(f"Number of students: {statistics['number_of_students']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")

    highest = statistics["highest_student"]
    lowest = statistics["lowest_student"]

    print(
        f"Highest: {highest['name']} - "
        f"{highest['grade']:.2f}"
    )

    print(
        f"Lowest: {lowest['name']} - "
        f"{lowest['grade']:.2f}"
    )

    print("-" * 40)


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""

    matches = []

    keyword = keyword.strip().lower()

    for student in students:
        student_id = student["student_id"].lower()
        name = student["name"].lower()

        if keyword in student_id or keyword in name:
            matches.append(student)

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""

    try:
        with open(filename, "w") as file:

            file.write("STUDENT GRADE ANALYZER REPORT\n")
            file.write("=" * 85 + "\n\n")

            file.write("STUDENT RESULTS\n")
            file.write("-" * 85 + "\n")

            for student in students:
                classification, status = classify_grade(student["grade"])

                file.write(
                    f"Student Number: {student['student_id']}\n"
                )
                file.write(
                    f"Student Name: {student['name']}\n"
                )
                file.write(
                    f"Grade: {student['grade']:.2f}\n"
                )
                file.write(
                    f"Classification: {classification}\n"
                )
                file.write(
                    f"Status: {status}\n"
                )
                file.write("-" * 40 + "\n")

            file.write("\nCLASS STATISTICS\n")
            file.write("-" * 40 + "\n")

            file.write(
                f"Number of students: "
                f"{statistics['number_of_students']}\n"
            )

            file.write(
                f"Class average: "
                f"{statistics['average']:.2f}\n"
            )

            file.write(
                f"Passed: {statistics['passed']}\n"
            )

            file.write(
                f"Failed: {statistics['failed']}\n"
            )

            highest = statistics["highest_student"]
            lowest = statistics["lowest_student"]

            file.write(
                f"Highest: {highest['name']} - "
                f"{highest['grade']:.2f}\n"
            )

            file.write(
                f"Lowest: {lowest['name']} - "
                f"{lowest['grade']:.2f}\n"
            )

        print(f"\nReport successfully saved to '{filename}'.")

    except OSError:
        print(f"Error: Could not write to '{filename}'.")


def main():
    """Run the menu-driven Student Grade Analyzer."""

    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)

        elif choice == "2":
            display_statistics(statistics)

        elif choice == "3":
            keyword = input("Enter student number or name: ").strip()

            matches = search_student(students, keyword)

            if matches:
                print("\nSEARCH RESULTS")
                display_students(matches)
            else:
                print("No matching student found.")

        elif choice == "4":
            save_report(
                students,
                statistics,
                "grade_report.txt"
            )

        elif choice == "5":
            print("Thank you for using Student Grade Analyzer.")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")
            continue


if __name__ == "__main__":
    main()