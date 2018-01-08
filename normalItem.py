from ollivander_logica import *
from tester import *
if __name__ == "__main__":
	iniciador = "+5 Dexterity Vest, 10, 20"
	item = NormalItem("+5 Dexterity Vest", 10, 20)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)

	iniciador = "Elixir of the Mongoose, 5, 7"
	item = NormalItem("Elixir of the Mongoose", 5, 7)
	lista = [str(item)]
	for dia in range(1, 31):
		item.updateQuality()
		lista.append(str(item))
	comprobador(iniciador, lista)
	
