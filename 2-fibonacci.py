# Exercício número 2:

def fibonacci(n):

    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a


def verifica_pertence(n):

    i = 1
    while fibonacci(i) <= n:
        if fibonacci(i) == n:
            return True
        i += 1
    return False


num = int(input("Digite o número inteiro que deseja: "))

# Calcula a sequência de Fibonacci até o número informado
fib = fibonacci(num)

# Verifica se o número pertence à sequência de Fibonacci
if verifica_pertence(num):
    print(
        f"O número {num} pertence à sequência de Fibonacci e é o {fib}-ésimo número da sequência.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
