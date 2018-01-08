from ollivander_logica import *
from tester import *
if __name__ == "__main__":
	iniciador = "Aged Brie, 2, 0"
	item = AgedBrie("Aged Brie", 2, 0)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)

