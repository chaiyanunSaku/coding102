def hollow_star_box(n: int) -> str:
    ans = ""
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                ans += "*"
            else:
                ans += " "
        if i != n - 1:
            ans += "\n"
    return ans


print(hollow_star_box(5))

# i is the row and j is the column
# "if i == 0 or i == n - 1 or j == 0 or j == n - 1:" checks if it is an edge; if so then ans += "*" else ans += " "