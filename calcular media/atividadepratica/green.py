# Função para calcular a média de três notas
def calcular_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media

# Exemplo de uso da função
nota1 = 8.5
nota2 = 7.0
nota3 = 9.2
media = calcular_media(nota1, nota2, nota3)
print("A média das três notas é:", media)
