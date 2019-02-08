numero = int(input())
if numero == 0:
	print(1)
else:
	fat = fatorial = 1
	termos = 0
	while True:
		if numero == 0:
			print(termos)
			break
		while fatorial <= numero:
			fatorial *= fat
			fat += 1
		if fat!=1:
			fatorial /= (fat-1)
		numero -= fatorial
		termos += 1
		fatorial = fat = 1