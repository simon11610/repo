largest_number = None

n = int(input("Въведете броя на числата: "))

for i in range(n):
    number = int(input(f"Въведете число {i + 1}: "))
    if largest_number is None or number > largest_number:
        largest_number = number

print(f"Най-голямото число е: {largest_number}")