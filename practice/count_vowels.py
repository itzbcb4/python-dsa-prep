def count_vowels(x):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in x:
        if char in vowels:
            count += 1
    return count

word = input("Enter a word: ")
print(f"The number of vowels in '{word}' is: {count_vowels(word)}")
