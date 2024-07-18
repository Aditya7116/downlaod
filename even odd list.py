
random = []
odd = []
even = []

print("Enter 10 integers:")
for i in range(10):
    num = int(input())
    random.append(num)

for num in random:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Input List:", random)
print("Odd List:", odd)
print("Even List:", even)
