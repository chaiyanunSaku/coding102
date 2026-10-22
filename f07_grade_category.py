def grade_category(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "Needs Improvement"


print(grade_category(99))
print(grade_category(85))
print(grade_category(70))
print(grade_category(50))