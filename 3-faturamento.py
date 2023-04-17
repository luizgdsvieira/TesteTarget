# Exercício 3:

# A princípio tentei usar o arquivo .xml. Não só retirei as tags de fechamento entre os dias no arquivo
# como a função de leitura exigia converter o arquivo ElementTree para string e depois para float, e mesmo
# assim o a função não realizava a média. De qualquer forma, o json é o mais indicado para tipo de problema.

import json

# Leitura do arquivo dados.json
with open('dados.json', 'r') as f:
    dados = json.load(f)

# Função para varrer os dados
valores = [dado['valor'] for dado in dados]

menor_valor = min(valores)
maior_valor = max(valores)

# Média da soma do faturamento
valores_com_faturamento = [v for v in valores if v > 0]
media = sum(valores_com_faturamento) / len(valores_com_faturamento)

# Cálculo dos valores acima da média
dias_com_faturamento = sum(1 for v in valores if v > media)

# Prints
print('Menor valor diário:', menor_valor)
print('Maior valor diário:', maior_valor)
print('Número de dias com faturamento acima da média:', dias_com_faturamento)
