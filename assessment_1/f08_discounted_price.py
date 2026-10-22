def discounted_price(total: float) -> float:
    if total >= 500:
        return total * 0.9
    return total


print(discounted_price(510))
print(discounted_price(350))