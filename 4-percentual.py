# Exercício 4
# Esse exercício é mais simples, pois o objetivo é apenas converter os número em porcentagem. 

# definir os faturamentos dado em float

faturamento_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Função que soma o faturamento mensal da distribuidora em todos os estados
total = sum(faturamento_estado.values())
print ('total de faturamento:', total)


for estado, faturamento in faturamento_estado.items():
    percentual = (faturamento / total) * 100
    print('percentual do estado de 'f'{estado}: {percentual:.2f}%') # exibi os dois primeiros dígitos do float com o sinal %