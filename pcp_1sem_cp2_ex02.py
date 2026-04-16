from os import remove
import math

lista=[]
for c in range (1,4):
  num = int(input("Digite um número: "))
  lista.append(num)
print(lista)

a=(max(lista))
lista.remove(a)
b = lista.pop()
c = lista.pop()

print(a)
print(b)
print(c)

if a>=b+c:
  print("Não forma triangulo")
elif a**2==b**2+c**2:
  print("Triangulo retangulo")
elif a**2>b**2+c**2:
  print("Triangulo obtusangulo")
elif a**2<b**2+c**2:
  print("Triangulo acutangulo")
elif a==b==c:
  print("Triangulo equilatero")
elif a==b or a==c or b==c:
  print("Triangulo isosceles")

