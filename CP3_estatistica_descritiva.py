"""
Estatística Descritiva — FIAP

Neste trabalho da FIAP, desenvolvi funções em Python para calcular média,
mediana, moda, variância e desvio padrão. Apliquei esses cálculos à análise
de tempos de atendimento e à comparação de notas de duas turmas, utilizando
a biblioteca collections para contar a frequência dos valores.
"""

from collections import Counter

tempos_atendimento = [12, 15, 12, 18, 20, 12, 22, 15, 18, 16]
Turma_A = [7.0, 7.5, 8.0, 7.0, 8.5, 9.0, 7.0, 8.0]
Turma_B = [5.0, 9.5, 6.0, 10.0, 5.5, 9.0, 6.5, 10.5]

def media(lista):
    total = 0
    for x in lista:
        total += x
    return total/len(lista)

def mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista)
    centro = n // 2
    if n % 2 == 0:
        return (lista_ordenada[centro] + lista_ordenada[centro - 1]) / 2
    return lista_ordenada[centro]

def moda(lista):
    aparicao = Counter(lista)
    max_aparicao = max(aparicao.values())
    return [item_max for item_max, ocorrencia in aparicao.items() if ocorrencia == max_aparicao]

def variancia(lista):
    Media = media(lista)
    total = 0
    for num in lista:
        total += (num - Media)**2
    return total/(len(lista) - 1)

def desvio_padrao(lista):
    Variancia = variancia(lista)
    return Variancia** 0.5

# exercicio 1
# 1:
print(f"A média é: {media(tempos_atendimento)}")
# 2:
print(f"A mediana é: {mediana(tempos_atendimento)}")
# 3:
print(f"A moda é: {moda(tempos_atendimento)}")

# exercicio 2
# 1:
print(f"A variancia é: {variancia(tempos_atendimento)}")
# 2:
print(f"O Desvio padráo é: {desvio_padrao(tempos_atendimento)}")

# exercicio 3
# 1:
print(f"A média da turma A é: {media(Turma_A)}")
print(f"A média da turma B é: {media(Turma_B)}")
# 2:
print(f"O Desvio padráo da turma A é: {desvio_padrao(Turma_A)}")
print(f"O Desvio padráo da turma B é: {desvio_padrao(Turma_B)}")
# 3:
print("O desvio padrão nos mostra que apesar das duas turmas exibirem a mesma média, a Turma A apresenta em um contexto geral valores muito mais próximos da média do que quando comparados com a Turma B, pois o desvio padrão da turma A é menor que o da Turma B.")
