def even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    return "Odd"


print(even_or_odd(10))
print(even_or_odd(7))

# %(mod) gives the remainder, so number % 2 == 0 means number is even