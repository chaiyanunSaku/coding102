scores = {"Sponge": 78, "Patrick": 42, "Sandy": 95, "Squidward": 50}

def best_student(scores):
    best_name = ""
    best_score = -1
    for name, score in scores.items():
        if score > best_score:
            best_score = score
            best_name = name
    return best_name, best_score

name, score = best_student(scores)
print(name, score)