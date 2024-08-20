# print com mensagem de boas-vindas
print("Boas-vindas a copiadora da Gisela Oliveira")


def escolha_servio():
    while True:
        # Perguntar o serviço desejado
        servico = input(
            "Entre com o tipo de serviço desejado \n"
            "DIG - Digitalização \n"
            "ICO - Impressão colorida\n"
            "IPB - Impressão Preto e Branco\n"
            "FOT - Fotocópia \n"
            ">>").lower()
        # Retornar os valores com base na escolha do usuario
        if servico == 'dig':
            return 1.10  # Custo por página de digitalização
        elif servico == 'ico':
            return 1.00  # Custo por página de impressão colorida
        elif servico == 'ipb':
            return 0.40  # Custo por página de impressão preto e branco
        elif servico == 'fot':
            return 0.20  # Custo por página de fotocópia
        else:
            print("Escolha inválida. Por favor, entre com o tipo de serviço novamente")
            print()


def num_pagina():
    while True:
        try:
            # Perguntar o número de paginas desejado
            n_pag = int(input("Qual o número de páginas desejado? "))
            if n_pag < 20:
                return n_pag  # Menor que 20 paginas, sem desconto
            elif n_pag >= 20 and n_pag < 200:
                # 15% para maior ou igual a 20 e menor que 200 paginas
                desconto = (n_pag * (15/100))
                return int(n_pag - desconto)
                # 20% se for igual ou maior que 200 e menor que 2000
            elif n_pag >= 200 and n_pag < 2000:
                desconto = n_pag * (20/100)
                return int(n_pag - desconto)
                # 25% se for maior ou igual que 2000 e menor que 20000
            elif n_pag >= 2000 and n_pag < 20000:
                desconto = n_pag * (25/100)
                return int(n_pag - desconto)
            # Para valores maiores ou igual a 20000
            else:
                print("Não aceitamos tantas páginas de uma vez."
                      "Por favor, entre com o número de páginas novamente")
                print()

                # Para valores não numericos
        except ValueError:
            print("Entrada inválida. Por favor, entre com o número de páginas novamente")
            print()


def servico_extra():
    while True:
        try:
            # Perguntar se o usuario quer algum serviço extra
            extra = int(input(
                "Escolha o serviço adicional (1- Encadernação simples, 2- Encadernação capa dura, 0- Nada): "))
            # Encadernação simples
            if extra == 1:
                return 15.00
            # Encadernação Capa dura
            elif extra == 2:
                return 40.00
            # Nenhum adicional
            elif extra == 0:
                return 0.00
            # Caso a pessoa não digite um numero valido
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                print()

        except ValueError:
            print("Entrada inválida. Digite um número correspondente à opção desejada.")
            print()


# Declarar as variaveis e armazenar os valores para fazer o calculo final
servico = escolha_servio()
n_pag = num_pagina()
extra = servico_extra()
total = (servico * n_pag) + extra
# Mostrar o total a pagar
print(f"O total a pagar é de: R$ {total: .2f}. (Serviço: { 
      servico: .2f} * páginas: {n_pag:} + extra: {extra: .2f}.)")
