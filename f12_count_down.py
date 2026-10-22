def count_down(n: int) -> list[int]:
    ans = []
    while n >= 1:
        ans.append(n)
        n -= 1
    return ans


print(count_down(5))