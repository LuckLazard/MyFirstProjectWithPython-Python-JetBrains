objects_earned = { "Bubblegum" : 202, 
                  "Toffee" : 118, 
                  "Ice cream": 2250, 
                  "Milk chocolate": 1680, 
                  "Doughnut": 1075,
                  "Pancake": 80
                 }
print("Earned amount:")
income = 0
for key, value in objects_earned.items():
    print(f"{key}: ${value}")
    income += value

print(f"\nIncome: ${income}")
print("Staff expenses:")
x = int(input())
income -= x
print("Other expenses:")
x = int(input())
income -= x
print(f"Net income: ${income}")