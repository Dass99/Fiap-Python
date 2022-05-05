segunda = int(input("Informe quantidade de votos para segunda "))

terca = int(input("Informe quantidade de votos para terça "))

quarta = int(input("Informe quantidade de votos para quarta "))

quinta = int(input("Informe quantidade de votos para quinta"))

sexta = int(input("Informe quantidade de votos para sexta "))


if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("\nO dia escolhido foi segunda-feira ")

elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("\nO dia escolhido foi terça-feira")

elif quarta > terca and quarta > terca and quarta > quinta and quarta > sexta:
    print("\nO dia escolhido foi quarta-feira")

elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("\nO dia escolhido foi quinta-feira")

elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("\nO dia escolhido foi sexta-feira")

else:
   print("\nHouve um empate, por favor refaçam a votação")