"""Um vendedor ambulante vendeu os produtos indicados na tabela a
 seguir. Informe quanto ele faturou com cada produto e quanto ele
 faturou no total.
 
Produto             Quantidade   vendida Valor unitário R$
Boneco Malandrinho  17               18,50
Spinner Pequeno     36               12,00
Cubo Mágico         7                5,90

Todos os dados devem ser lidos do teclado, sendo que o nome do
produto é string, a quantidade vendida é um número inteiro e o valor
unitário é um número real.
"""

boneco = "Boneco Malandrinho"
spinner = "Spinner Pequeno"
cubo = "Cubo Mágico"

quantidade = 0
texto = """
  1 - Boneco Malandrinho  
  2 - Spinner Pequeno
  3 - Cubo Mágico
"""
print(texto)



resultado = input("Qual produto que você quer: ")
escolha = input()
