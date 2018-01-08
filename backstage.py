from ollivander_logica import *
from tester import * 
if __name__ == "__main__":

	iniciador = "Backstage passes to a TAFKAL80ETC concert, 15, 20"
	item = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)

	iniciador = "Backstage passes to a TAFKAL80ETC concert, 10, 49"
	item = Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 49)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)

	iniciador = "Backstage passes to a TAFKAL80ETC concert, 5, 49"
	item = Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)