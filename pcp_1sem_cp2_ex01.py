print("1=Sao Paulo\n2=Rio de Janeiro\n3=Minas Gerais\n4=Bahia\n5=Acre")
estado=int(input("Digite o estado de origem do seu caminhão: "))
peso=float(input("Digite o peso da carga em toneladas do seu caminhão: "))
carga=int(input("Digite o codigo da carga{10-40}: "))
kg=peso*1000
if carga >= 10 and carga<=20:
  preco = kg*100
  print(f"Preço da carga é: R${preco}")
elif carga >= 21 and carga<=30:
  preco = kg*250
  print(f"Preço da carga é: R${preco}")
else:
  preco = kg*340
  print(f"Preço da carga é: R${preco}")

if estado == 1:
  imposto = preco * 0.35
elif estado == 2:
  imposto = preco * 0.25
elif estado == 3:
  imposto = preco * 0.15
elif estado == 4:
  imposto = preco * 0.05
elif estado == 5:
  imposto = 0
  


print(f"Valor total transportado pelo caminhão: R${preco+imposto}")


