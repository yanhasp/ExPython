# Yan Hasperoy Rita (código 8289735)
# Projeto M1 – Sistema de Caixa de Supermercado


produtos = {
    "arroz": 25.50,
    "feijao": 8.90,
    "oleo de soja": 7.00,
    "cafe": 50.00,
    "leite": 4.50
}

carrinho = {}  # guarda produto: [quantidade, subtotal]

while True:
    print("\n**** Supermercado Python ****")
    print("1. Adicionar item ao carrinho")
    print("2. Ver total da compra")
    print("3. Finalizar compra")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome do produto: ").strip().lower()
        # strip() → retira espaços extras; lower() → ignora maiúsc./minúsc.
        if nome in produtos:
            try:
                qtd = int(input("Quantidade: "))
            except:
                print("Quantidade inválida!")
                continue
            if qtd <= 0:
                print("Quantidade precisa ser positiva.")
                continue

            preco = produtos[nome]
            subtotal = preco * qtd
            desconto_item = 0.0

            # Desconto por volume (>3 unidades)
            if qtd > 3:
                desconto_item = subtotal * 0.03
                subtotal -= desconto_item
                print("-> Desconto de 3% por volume aplicado.") 

            # Atualiza o carrinho
            if nome in carrinho:
                carrinho[nome][0] += qtd
                carrinho[nome][1] += subtotal
            else:
                carrinho[nome] = [qtd, subtotal]

            print(f"{qtd} x {nome.title()} adicionado(s).")
        else:
            print("Produto não encontrado.")

    elif opcao == "2":
        total_parcial = 0
        for item in carrinho:
            total_parcial += carrinho[item][1]  # soma subtotais
        print(f"Total parcial: R$ {total_parcial:.2f}")

    elif opcao == "3":
        print("\n==================== RECIBO ===================")
        print("--------------- ITENS COMPRADOS ---------------")
        print("Qtd. Produto (Preço Un.) Subtotal")
        print("-----------------------------------------------")

        total_bruto = 0
        for nome, dados in carrinho.items():
            qtd, subtotal = dados
            preco_unit = produtos[nome]
            print(f"{qtd} x {nome.title()} (R$ {preco_unit:.2f}/un) R$ {subtotal:.2f}")
            total_bruto += subtotal

        # Desconto geral 
        if total_bruto > 200:
            desc_compra = total_bruto * 0.15
        elif total_bruto >= 100:
            desc_compra = total_bruto * 0.10
        else:
            desc_compra = 0.0

        print("-----------------------------------------------")
        print(f"Total Bruto: R$ {total_bruto:.2f}")
        print(f"Desconto da Compra: R$ {desc_compra:.2f}")
        print("-----------------------------------------------")
        print(f"Valor Final a Pagar: R$ {total_bruto - desc_compra:.2f}")
        print("===============================================")
        print("Obrigado pela sua compra!")
        break

    else:
        print("Opção inválida! Tente novamente.")
