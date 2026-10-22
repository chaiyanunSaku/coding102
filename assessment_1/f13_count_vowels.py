def count_vowels(word: str) -> int:
    count = 0
    for i in word.lower():
        if i in "aeiou":
            count += 1
    return count


print(count_vowels("apple"))
print(count_vowels("aeiou"))

# word.lower() lets us check only lowercase vowels, so "A" and "a" both count
# `i in "aeiou"` checks if the character i appears in the string "aeiou"