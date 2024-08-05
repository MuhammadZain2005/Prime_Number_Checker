"""
PRIME NUMBER CHECKER : Basic Program

Difficulty : 3/10

Comments : Had to learn that prime numbers usually go through the range from 2 to their square root and
adding one to it to find its divisor. Had to learn the Division pair property of prime numbers and the square root
of "n". (Mathematical Difficulty)
"""
import time
import random


def is_prime_basic(prime_check):
    if prime_check <= 1:
        return False
    if prime_check <= 3:
        return True
    if prime_check % 2 == 0 or prime_check % 3 == 0:
        return False
    i = 5
    while i * i <= prime_check:
        if prime_check % i == 0 or prime_check % (i + 2) == 0:
            return False
        i += 6
    return True


def miller_rabin(n, k=5):  # number of tests
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write (n - 1) as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime(prime_check):
    if prime_check < 10 ** 7:
        return is_prime_basic(prime_check)
    else:
        return miller_rabin(prime_check)


def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    try:
        prime = int(input("Insert a number to see if it's prime > "))
        start_time = time.time()
        if is_prime(prime):
            print(f"The number {prime} is a prime number.")
        else:
            print(f"The number {prime} is not a prime number.")
        end_time = time.time()
        print(f"Time taken to check: {end_time - start_time:.6f} seconds")

        generate = input("Do you want to generate a list of prime numbers up to a limit? (yes/no) > ").strip().lower()
        if generate == 'yes':
            limit = int(input("Enter the limit > "))
            start_time = time.time()
            primes = generate_primes(limit)
            end_time = time.time()
            print(f"Prime numbers up to {limit}: {primes}")
            print(f"Time taken to generate primes: {end_time - start_time:.6f} seconds")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
