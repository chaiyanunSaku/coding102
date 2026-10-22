def password_strength(password: str) -> str:
    if len(password) < 8:
        return "Too short"
    return "Strong enough"


print(password_strength("1234567"))
print(password_strength("1234567890"))