def full_name(first_name: str, last_name: str) -> str:
    return f"{first_name[0].upper()}{first_name[1:]} {last_name[0].upper()}{last_name[1:]}"


print(full_name("spongebob", "squarePants"))

# text[0] is the first character, text[1:] is everything after it