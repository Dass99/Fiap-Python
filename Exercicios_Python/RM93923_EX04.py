numero = int(input("Informe os minutos atuais do computador: "))
fatorial = 1

for n in range(1,numero+1):
    fatorial *= n

senha = "LIBERDADE" + str(fatorial)
print("Utilize a  senha " + senha + " para o desbloqueio")
