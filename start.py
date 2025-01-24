lungime = 4

caractereMici = ''.join(chr(ord('a')+i) for i in range(26))
caractereMari = ''.join(chr(ord('A')+i) for i in range(26))
cifre = ''.join(chr(ord('0')+i) for i in range(10))

print("The characters used!")
print("The string after construction: " + str(caractereMici))
print("The string after construction: " + str(caractereMari))
print("The string after construction: " + str(cifre))

caractereFolosite = caractereMici + caractereMari + cifre
print("The final string: " + str(caractereFolosite))

numarCaractere = len(caractereFolosite)
print("The number of characters: " + str(numarCaractere))

parolaDeInceput = ''
for indexa in range(lungime):
	parolaDeInceput = parolaDeInceput + caractereFolosite[0]

print("Parola exemplu: " + str(parolaDeInceput))

def genereazaLaIndexul(parolaSablon, caractere, index):
	a = list()

	for indexb in range(numarCaractere):
		parola = parolaSablon
		parola = parola[:index] + caractere[indexb] + parola[index+1:]
		a.append(parola)
	return a

print("Automat")

paroleActuale = list()
paroleActuale.append(parolaDeInceput)

for i in range(lungime):
	parole = list()

	for parolaCurenta in paroleActuale:
		a = genereazaLaIndexul(parolaCurenta, caractereFolosite, i)
		parole += a

	paroleActuale = parole

f = open("p.txt", "a")
for parola in paroleActuale:
	f.write(parola + "\n")
f.close()
