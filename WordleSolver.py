# Read file and create list of words based on file
words = open("valid-wordle-words.txt", "rt").readlines()
# Create 2d array where each word is its own array, remove newline char
words = [list(word.rstrip()) for word in words]

print("Enter letters without spaces")
print("Ex. To enter 'A' and 'G', enter 'AG'")

# Letters which are not in the final word
bad = set(input("Enter bad letters: ").strip().lower())
# Letters which are in the final word, but in an unknown position
good = set(input("Enter good letters: ").strip().lower())

# Remove words based on above requirements 
i = 0
# Iterate through every word
while i < len(words):
    # If word shares chars with bad chars
    if not bad.isdisjoint(words[i]):
        del words[i]
        i -= 1
    # If word doesn't have good chars
    elif good.isdisjoint(words[i]):
        del words[i]
        i -= 1
    i += 1

print("Enter the known letters in the proper positions")
print("with unknown letters represented as an underscore (case insensitive)")
print("Ex. R_A_G")

# Letters in known position and unknown letters
placed = list(input("Enter the placed letters: ").strip().lower())

i = 0
# Iterate through every word
while i < len(words):
    j = 0
    # Iterate through every letter in word
    while j < 5:
        # If char in placed doesn't match char in word, delete
        if placed[j] != "_" and placed[j] != words[i][j]:
            del words[i]
            i -= 1
            break
        j += 1
    i += 1  

# Prints result
if len(words) > 1:
    print("Here are the possible solutions:")
    print(["".join(word) for word in words])
elif len(words) == 1:
    print("Here is your solution:")
    print("".join(words[0]))
else:
    print("No words match your input, please try again")
