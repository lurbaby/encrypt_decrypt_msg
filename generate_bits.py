import random
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_form_4k_plus_3(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num) and num % 4 == 3:
            primes.append(num)
    return primes

def initialize_bbs():
    p = find_primes_form_4k_plus_3(10000)[-1]
    q = find_primes_form_4k_plus_3(10000)[-2]
    n = p * q
    x = random.randint(2, n - 1)  # Вибираємо випадкове число (інакше псевдогенерація буде завжди однаковою)
    while not is_prime(x):
        x = pow(x, 2, n)  # Генеруємо квадратичний залишок, для того щоб під час кожного разу генерувалася нова псевдо послідовність бітів
    return n, x

def bbs_gamma(n, x, length):
    gamma = ''
    for _ in range(length * 8):  #length * на 8, щоб отримати достатньо бітів
        x = pow(x, 2, n)
        bit = x % 2
        gamma += str(bit)
    return gamma

