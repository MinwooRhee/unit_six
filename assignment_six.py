
maximum = int(input("Type in the maximum number: "))

numbers = []

prime_numbers = []

for x in range(2, maximum+1):
    numbers.append(x)

while len(numbers) > 0:
    prime_numbers.append(numbers[0])

    for y in numbers:
        if y % prime_numbers[-1] == 0:
            numbers.remove(y)

print(" ")
print(numbers)
print(prime_numbers)
