def first_multiple_of_seven(start: int) -> int:
    while start % 7 != 0:
        start += 1
    return start 

print(first_multiple_of_seven(10))
print(first_multiple_of_seven(21))
print(first_multiple_of_seven(22))
print(first_multiple_of_seven(1))

# start % 7 == 0 means start is divisible by 7