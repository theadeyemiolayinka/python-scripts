def generate_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers

primes = generate_prime_numbers(1, 50)
print("Prime numbers between 1 and 50:", primes)
