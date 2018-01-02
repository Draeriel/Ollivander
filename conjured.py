from ollivander_logica import *
if __name__ == "__main__":

	item = Conjured("Conjured Mana Cake", 0, 3)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)
