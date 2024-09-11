import json

# Carregar os dados do arquivo JSON
with open('faturamento.json') as f:
    dados = json.load(f)

# Extrair os valores de faturamento, ignorando os dias com valor 0.0 e convertendo para inteiros
faturamentos = [int(dia['valor']) for dia in dados if dia['valor'] > 0]

# Calcular o menor e o maior faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcular a média mensal de faturamento (ignorando dias com valor 0.0)
media_mensal = sum(faturamentos) / len(faturamentos)

# Contar os dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

# Exibir os resultados
print(f"Menor faturamento do mês: R${menor_faturamento}")
print(f"Maior faturamento do mês: R${maior_faturamento}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")
