print("{:~^50}".format(" Conversor de Moedas "))
cot = float(input("Qual é a cotação do dólar hoje? R$"))
r = float(input("Quantos reais você tem na sua carteira? R$"))
dol = r/cot
print("\n.\n.\n.\n")
print("Com os R${:.2f} que você tem na carteira, dá pra comprar US${:.2f}.\n".format(r, dol))
print("~" * 50)
