# Minwoo Rhee
# 2018 10 24
# assignment_six
# Sieve of Eratosthenes algorithm finds all prime numbers up to user input


def create_lists():
    """
    gets the user input of a maximum number
    creates two lists, one for all numbers from 2 to the maximum number, the other one empty
    :return: a list of all numbers, an empty list
    """

    maximum = int(input("Type in the maximum number: "))

    numbers = []

    prime_numbers = []

    for x in range(2, maximum+1):
        numbers.append(x)

    return numbers, prime_numbers


def sieve_of_eratosthenes(numbers, prime_numbers):
    """
    Sieve of Eratosthenes algorithm
    starting from 2, remove all multiples of prime numbers
    add all prime numbers to an empty list
    :param numbers: a list of all numbers from 2 to the maximum number
    :param prime_numbers: an empty list to be filled with prime numbers
    :return: list of prime numbers
    """

    while len(numbers) > 0:  # loop runs until all numbers are crossed out (removed) in the list
        prime_numbers.append(numbers[0])

        for y in numbers:
            if y % prime_numbers[-1] == 0:  # index [-1] gives whatever the element that was appended the last
                numbers.remove(y)
    return prime_numbers


def main():

    numbers, prime_numbers = create_lists()
    prime_numbers = sieve_of_eratosthenes(numbers, prime_numbers)

    print("The list of prime numbers is:")
    print(prime_numbers)


main()
