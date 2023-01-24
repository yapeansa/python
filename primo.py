#!/bin/python3

def isPrime(n):
    test = True
    if n == 1:
        test = False
        
    for i in range(2, n):
        if n % i == 0:
            test = False
    
    return test

while True:
    n = input('Por favor, digite um número inteiro positivo: ')
    n = int(n)
    if n > 0: break

if isPrime(n):
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
