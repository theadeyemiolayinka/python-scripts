def is_emirp_prime(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    reverse_num = int(str(num)[::-1])
    return is_prime(num) and is_prime(reverse_num) and num != reverse_num

result = is_emirp_prime(13)
print("Is 13 an emirp prime number?", result)
