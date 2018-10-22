
maximum = int(input("Type in the maximum number: "))

numbers = []

prime_numbers = []

for x in range(2, maximum+1):
    numbers.append(x)


prime_numbers.append(numbers[0])

for x in range(len(numbers)):
    if x+1 % prime_numbers[-1] == 0:
        numbers.remove(x+1)


print(numbers)
print(prime_numbers)