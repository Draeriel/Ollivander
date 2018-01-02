from ollivander_logica import *
if __name__ == "__main__":

	item = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)

	item = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)