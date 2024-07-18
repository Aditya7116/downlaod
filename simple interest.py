num_sets = 3

for i in range(1, num_sets + 1):
    p = float(input(f"Enter principal amount for set {i}: "))
    n = float(input(f"Enter time period for set {i}: "))
    r = float(input(f"Enter rate of interest for set {i}: "))
    
  
    simple_interest = (p * n * r) / 100
    

    print(f"Simple Interest for set {i} is: {simple_interest}")
