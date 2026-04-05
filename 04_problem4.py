# Count vowels in a file
vowels = "aeiouAEIOU"
count = 0

with open("data.txt", "r") as f:
    text = f.read()
    for ch in text:
        if ch in vowels:
            count += 1

print("Total vowels in file:", count)
