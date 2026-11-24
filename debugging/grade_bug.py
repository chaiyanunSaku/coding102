# Goal: give each student a letter grade
# 80 and above = A, 70 and above = B, 60 and above = C, below 60 = F

def average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


def letter_grade(score):
    if score > 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


scores = {
    "Star": [80, 90, 70],
    "Bob": [60, 75, 90],
    "Squid": [100, 95, 85],
}

report = {}
for name, marks in scores.items():
    avg = average(marks)
    report[name] = letter_grade(avg)

print(report)