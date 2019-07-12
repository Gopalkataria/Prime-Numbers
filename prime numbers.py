from math import sqrt
import sys


def prime(rng):  # return a list of prime numbers

    Primes = []
    if rng >= 2:
        Primes.insert(0, 2)

    for num in range(3, (rng + 1), 2):  # main loop of all odd numbers
        # main loop till that odd number finding odd factors

        for fact in range(3, (round(sqrt(num)) + 1), 2):
            if num % fact == 0:  # if num / factor gives remainder 0
                break

        # FOR - ELSE NOT TO BE CONFUSED WITH IF - ELSE !!
        # IT'S NOT A PART OF IF

        else:  # executed if no exception is risen
            Primes.append(num)

    return Primes


if __name__ == "__main__":
    x = sys.argv[1]
    if x.isdigit():
        prime(int(x))
