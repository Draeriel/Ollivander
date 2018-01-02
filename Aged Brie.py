from ollivander_logica import *
if __name__ == "__main__":

	item = AgedBrie("Aged Brie", 2, 0)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)

