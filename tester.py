def comprobador(nombre, lista):
	recolector = []
	colector = ""
	fichero = open("./stdout.txt", "r")
	for linea in fichero:
		for letra in linea:
			if letra != "\n":
				colector += letra
			else:
				recolector.append(colector)
				colector = ""
	tester = []
	comienzo = recolector.index(nombre)				
	for elemento in range(comienzo, len(recolector), 10):
		tester.append(recolector[elemento])							
	fichero.close()
	assert(lista == tester)
	print("Todo ha ido bien.")	

