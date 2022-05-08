# input
n = int(input())

def eratosthenes_sieve(n):
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime

is_prime = eratosthenes_sieve(int(pow(n, 1/3)) + 1)
cnt = 0
primes = []
for i in range(2, int(pow(n, 1/3)) + 1):
    if is_prime[i]:
        primes.append(i)

for i in range(len(primes)):
    for j in range(i):
        p, q = primes[j], primes[i]
        if n < p * (q ** 3):
            break
        cnt += 1
# TLE
# for i in range(2, int(pow(n, 1/3)) + 1):
#     for j in range(2, i):
#         if n < j * i * i * i:
#             break
#         elif is_prime[i] and is_prime[j]:
#             cnt += 1
print(cnt)