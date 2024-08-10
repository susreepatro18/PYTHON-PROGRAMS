def count_primes(n):
    if n < 2:
        return 0

    # Create a list to track whether each number is prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    p = 2
    while (p * p <= n):
        if is_prime[p]:
            # Mark multiples of p as False starting from p^2
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Count the number of primes (True values in is_prime)
    count = sum(is_prime)

    return count


n = int(input("Enter the value: "))
print(count_primes(n))