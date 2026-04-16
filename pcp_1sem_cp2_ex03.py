cp1 = float(input("Digite a nota do CheckPoint 1: "))
cp2 = float(input("Digite a nota do CheckPoint 2: "))
cp3 = float(input("Digite a nota do CheckPoint 3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

grades = [cp1, cp2, cp3, sp1, sp2, gs]
for grade in grades:
	if grade < 0 or grade > 10:
		print("ERRO: As notas inseridas devem estar entre 0  e 10")
		exit()

lowest_cp = 10
for grade in grades[:3]:
	if grade < lowest_cp:
		lowest_cp = grade

grades.remove(lowest_cp)

mean = (sum(grades[:-1]) / 4) * 0.4 + grades[-1] * 0.6
weighted_mean = mean * 0.4

print(f"\nMédia do semestre (sem peso): {mean}\nMédia do semestre (com peso): {weighted_mean}")