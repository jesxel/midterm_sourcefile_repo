# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",

    #Testing invalid records
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,"

]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A: Parse and organize the records.
for record in raw_records:

    # Split the record into fields.
    fields = record.split(",")

    # Check for an invalid field count.
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    # Store the student's name.
    name = fields[0]

    # Convert the score fields to numbers safely.
    try:
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    # Add the name and scores to student_scores.
    student_scores[name] = scores


# PART B: Display records alphabetically.
print("ORGANIZED STUDENT RECORDS")

# Sort the names and display every student and score list.
for name in sorted(student_scores):
    print(f"{name}: {student_scores[name]}")


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0


# PART C: Calculate the student results.
for name, scores in student_scores.items():

    # Guard against an empty score list.
    if len(scores) == 0:
        continue

    # Calculate total, average, highest, and lowest.
    total = sum(scores)
    number_of_scores = len(scores)
    average = total / number_of_scores
    highest_score = max(scores)
    lowest_score = min(scores)

    # Determine the student's remark.
    if average >= PASSING_GRADE:
        remark = "Passed"
    else:
        remark = "Failed"

    # Update the passed or failed counter.
    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    # Add the average to sum_of_averages.
    sum_of_averages += average

    # Append the result tuple to ranking.
    result = (average, name, highest_score, lowest_score, remark)
    ranking.append(result)


# PART D: Sort and display the ranking.
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

# Use enumerate() and tuple unpacking to display the ranking.
for rank, record in enumerate(ranking, start=1):
    average, name, highest_score, lowest_score, remark = record

    print(
        f"{rank:<5}"
        f"{name:<11}"
        f"{average:<9.2f}"
        f"{highest_score:<9}"
        f"{lowest_score:<8}"
        f"{remark}"
    )


# PART E: Display the class summary.

# Calculate the class average safely.
if len(ranking) > 0:
    class_average = sum_of_averages / len(ranking)
else:
    class_average = 0


# Use ranking[0] and ranking[-1] safely.
if len(ranking) > 0:
    highest_average, highest_name, _, _, _ = ranking[0]
    lowest_average, lowest_name, _, _, _ = ranking[-1]
else:
    highest_average = 0
    highest_name = "None"
    lowest_average = 0
    lowest_name = "None"


print("\nCLASS SUMMARY")

# Display all required summary information.
print(f"Number of Students: {len(ranking)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")
print(f"Highest: {highest_name} - {highest_average:.2f}")
print(f"Lowest: {lowest_name} - {lowest_average:.2f}")