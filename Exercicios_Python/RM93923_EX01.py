tipo_assinatura = input("Informe o tipo de assinatura do cliente ").upper()
faturamento_Anual = float(input("Informe o faturamento anual do cliente"))

if tipo_assinatura == "BASIC":
    bonus = faturamento_Anual * 0.3
    print(f"O valor a ser pago pelo cliente é de R${bonus:.2f}")
elif tipo_assinatura == "SILVER":
    bonus = faturamento_Anual * 0.2
    print(f"O valor a ser pago pelo cliente é de R${bonus:.2f}")
elif tipo_assinatura == "GOLD":
    bonus = faturamento_Anual * 0.1
    print(f"O valor a ser pago pelo cliente é de R${bonus:.2f}")
elif tipo_assinatura == "PLATINUM":
    bonus = faturamento_Anual * 0.05
    print(f"O valor a ser pago pelo cliente é de R${bonus:.2f}")