from ollivander_logica import *
from tester import *
if __name__ == "__main__":

	iniciador = "Conjured Mana Cake, 0, 3"
	item = Conjured("Conjured Mana Cake", 0, 3)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)
'''Salta el assert porque en el fichero stdout.txt el elemento "Conjured Mana Cake" funciona como un Normalitem'''