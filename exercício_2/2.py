def is_fibonacci(n):
    if n < 0:
        return False

    # Iniciar variáveis para os dois primeiros números da sequência
    a, b = 0, 1

    while a < n:
        a, b = b, a + b

    return a == n

# Número de entrada (pode ser alterado conforme necessário)
num = int(input("Informe um número: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")