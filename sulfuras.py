from ollivander_logica import *
from tester import *
if __name__ == "__main__":

	iniciador = "Sulfuras, Hand of Ragnaros, 0, 80"
	item = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)

	iniciador = "Sulfuras, Hand of Ragnaros, -1, 80"
	item = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)