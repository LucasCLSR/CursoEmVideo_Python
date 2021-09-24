print("{:~^50}\n".format(" Tabuada de um número "))
n = int(input("De qual número você quer saber a tabuada? "))
print("-"*15)
i = 1
while i < 11:
  print("{} x".format(n), "{:>2} = {}".format(i, n * i))
  i += 1
print("-" * 15)
print("~" * 50)
