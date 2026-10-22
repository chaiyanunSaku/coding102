def sum_to_n(n: int) -> int:
    count = 0
    for i in range(n+1):
        count += i
    return count


print(sum_to_n(5))

# range(n+1) goes 0, 1, ..., n