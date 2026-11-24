# Goal: find each student's average score
scores = {
    "Star": [80, 90, 70],
    "Bob": [60, 75, 90],
    "Squid": [100, 95, 85],
}

averages = {}
total = 0

for name, marks in scores.items():
    for mark in marks:
        total = total + mark
    averages[name] = total / len(marks)

print(averages)