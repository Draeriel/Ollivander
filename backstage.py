from ollivander_logica import *
if __name__ == "__main__":

	print("Entrada 1")
	item = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)

	print("Entrada 2")
	item = Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 49)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)

	print("Entrada 3")
	item = Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)
