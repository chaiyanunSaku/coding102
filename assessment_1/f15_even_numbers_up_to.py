def even_numbers_up_to(n: int) -> list[int]:
    ans = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            ans.append(i)
    return ans


print(even_numbers_up_to(10))
print(even_numbers_up_to(7))
print(even_numbers_up_to(1))
print(even_numbers_up_to(2))

# build a list by starting with [] and using .append() inside the loop