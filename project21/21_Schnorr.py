import math
import random
from sympy import *
from sympy.ntheory import discrete_log
import time
def discreteLogarithm(a, b, m):
    return discrete_log(m, b, a)

def prime_generator(a, b):
    check = true
    while check:
        i = random.randrange(a, b)
        if isprime(i):
            check = false
    return i

def divisor_number(p):
    for q in range(pow(2, 10), (p - 1) // 2):
        if (p - 1) % q == 0 & isprime(q):
            return q

def findPrimefactors(s, n):
    # Print the number of 2s that divide n
    while n % 2 == 0:
        s.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while n % i == 0:
            s.add(i)
            n = n // i
    if n > 2:
        s.add(n)

def findPrimitive(n):
    s = set()
    if not isprime(n):
        return -1
    phi = n - 1
    findPrimefactors(s, phi)

    for r in range(2, phi + 1):
        flag = False
        for it in s:
            if pow(r, phi // it, n) == 1:
                flag = True
                break
        if not flag:
            return r
    return -1


def number_generator(p, q):
    while True:
        k = (p - 1) // q
        x = primitive_root(p)
        alpha = pow(x, k, p)
        return alpha


def TA_generator():
    p = prime_generator(pow(2, 30), pow(2, 35))
    q = divisor_number(p)
    params = {
        "p": p,
        "q": q,
        "alpha": number_generator(p, q),
        "t": random.randrange(1, 20)
    }
    return params


def key_generator(params: dict):
    private_key = {
        "a": random.randrange(0, params["q"] - 1),
    }
    public_key = {
        # "n": params["n"],
        "alpha": params["alpha"],
    }
    output = {
        "sk": private_key,
        "pk": public_key
    }
    return output


def identification(params: dict, keys: dict):
    alpha: int = keys["pk"]["alpha"]
    a: int = keys["sk"]["a"]
    p: int = params["p"]
    q: int = params["q"]
    t: int = params["t"]
    # A sends v to TA
    v = pow(alpha, -a, p) % p
    # A chooses  random k1 and k2  and compute gamma then sends gamma to B
    k = random.randrange(1, params["q"])
    gamma = pow(alpha, k, p)
    # B choose a random number r
    r = random.randrange(0, 2 ** t - 1)
    y = k + r * a % q
    gamma1 = pow(alpha, y, p) * pow(v, r, p) % p

    if gamma1 == gamma:
        print(f"p: {p} \nq: {q} \nalpha: {alpha}  \na: {a} \n"
              f" \nt: {t} \nv: {v} \nk: {k} \n"
              f"gamma: {gamma} \nr: {r} \ny: {y}  \ngamma1: {gamma1}")
        print("验证通过:Accepted")
    else:
        print("验证失败:Rejected")


if __name__ == "__main__":
    start = time.time()
    parameters = TA_generator()
    keys = key_generator(parameters)
    identification(parameters, keys)
    end = time.time()
    print("所用时间为:", (end - start) * 1000, "ms")