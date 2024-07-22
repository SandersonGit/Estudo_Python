# lista = [1, 2, 3, 4, 5]

# print(lista)

# for n in lista:
#     print(n)
    

carros = ["Monza", "Pagero", "Fusca", "Vectra"]

inputCarro = input("Escolha o seu carro")

for carro in carros:
    if carro == inputCarro:
        print(f"Seu carro foi encontrado. {carro}")
        

    if carro != inputCarro:
        print("Carro não encontrado")
    