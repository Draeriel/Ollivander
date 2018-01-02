from ollivander_logica import *
if __name__ == "__main__":

	item = NormalItem("+5 Dexterity Vest", 10, 20)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)

	item = NormalItem("Elixir of the Mongoose", 5, 7)
	for dia in range(1, 31):
		print(item)
		item.updateQuality()
	print(item)
