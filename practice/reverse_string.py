def reverse_string(x):
    rev = "".join(reversed(x))
    return rev

word = input("Enter a word: ")
print(f"The reversed word is: {reverse_string(word)}")
