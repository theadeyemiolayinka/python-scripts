def is_smith(num):
    def prime_factors(n):
        factors = []
        divisor = 2

        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1

        return factors

    digit_sum = sum(int(digit) for digit in str(num))
    factors = prime_factors(num)
    factors_sum = sum(sum(int(digit) for digit in str(factor)) for factor in factors)

    return digit_sum == factors_sum

result = is_smith(666)
print("Is 666 a Smith number?", result)
