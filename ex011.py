print("{:~^50}\n".format(" Pintando parede "))
enunciado = "Sabendo-se que com 1L de tinta pinta-se 2m² de parede, calcule a quantidade de litros de tinta para pintar a parede do usuário.\n"
i = 0
# Imprime "enunciado" de 50 em 50 linhas
while i < len(enunciado):
  print(enunciado[i:(i+50)])
  i += 50

l = float(input("Largura da parede (em metros): "))
h = float(input("Altura da parede (em metros): "))

a = l * h

print("\n.\n.\n.\n")
resultado = "Sua parede tem a dimensão {:.1f}m x {:.1f}m e a sua área é de {:.2f}m². Para pintar essa parede, você precisará de {:.3f}L de tinta.".format(l, h, a, (a / 2))
i = 0
# Imprime "resultado" de 50 em 50 linhas.
while i < len(resultado):
  print(resultado[i:(i+50)])
  i += 50
print("~"*50)
