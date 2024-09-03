import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, 'dados.json')

# Carregar os dados do arquivo JSON
with open(json_path, 'r') as file:
    faturamento_data = json.load(file)

# Filtrar dias com faturamento
faturamento = [dia['valor'] for dia in faturamento_data if dia['valor'] > 0]

# Calcular menor e maior faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcular média mensal
media_mensal = sum(faturamento) / len(faturamento)

# Contar dias acima da média
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

# Exibir resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")