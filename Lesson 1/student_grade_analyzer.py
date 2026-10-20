scores =[85, 72, 91, 64, 78]

print("Student Scores:" )
for score in scores:
    print(score)

print()

passed = 0
failed = 0

for i, score in enumerate (scores, start=1):
    if score >= 90:
        grade = "Excellent"
        result = "Passed"
        passed += 1

    elif score >= 80:
        grade = "Very Good"
        result = "Passed"
        passed += 1

    elif score >= 75:
        grade = "Good"
        result = "Passed"
        passed += 1

    else:
        grade = "Failed"
        result = "Failed"
        failed += 1

    if result == "Failed":
        print(f"Students {i}: {score} - Failed")

    else:
        print(f"Students {i}: {score} - {grade} - {result}")

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

print()
print(f"Total Score: {total}")
print(f"Average Score: {average:.0f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")


    