# Define a caixa-S como uma lista de listas
s_box = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def caixa_s(sub_word, s_box):
    # Converte a sub_palavra binária em decimal
    decimal_value = int(sub_word, 2)
    
    # Divide a sub_palavra em linha e coluna
    row = (decimal_value & 0b1000) >> 3  # Pega o primeiro bit
    col = decimal_value & 0b0111          # Pega os últimos 3 bits
    
    # Encontra o valor na caixa-S correspondente à linha e coluna
    return s_box[row][col]

# Palavra de entrada
entrada = "011010"

# Divide a palavra de entrada em blocos de 4 bits
blocos = [entrada[i:i+4] for i in range(0, len(entrada), 4)]

# Substitui cada bloco usando a caixa-S
resultado = [caixa_s(bloco, s_box) for bloco in blocos]

print("Substituição de caixa-S para a palavra de entrada", entrada)
print("Resultado:", resultado)
