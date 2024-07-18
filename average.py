def calculate(*args):
    total = 0
    for num in args:
        total += num

    average = total / len(args)
    
    return average


result = calculate(1, 2, 3, 4, 5)

print(result )