def analise_vendas(vendas):
    # Calcule o total de vendas e a média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    
    return f"Total de vendas: {total_vendas}, Média de vendas: {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha separada por vírgula
    entrada = input("Digite as vendas separadas por vírgula: ")
    # Converte a entrada em uma lista de inteiros usando split(',') e map(int, ...)
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))