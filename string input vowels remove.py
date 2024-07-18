
input = input("Enter a string: ")
vowels = "aeiouAEIOU"
output = ""
for char in input:
    if char not in vowels:
        output += char
        
print("String after removing vowels:", output)
