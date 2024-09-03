def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Exemplo de uso
string_teste = input('Digite uma palavra: ')
string_invertida = inverter_string(string_teste)
print(string_invertida)