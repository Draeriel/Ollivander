class Item:
	def __init__(self, name, sell_in, quality):
		self.name = name
		self.sell_in = sell_in
		self.quality = quality

	def __repr__(self):
		return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Interfaz():
	def updateQuality(self):
		pass

class NormalItem(Item, Interfaz):
	def __init__(self, name, sell_in, quality):
		Item.__init__(self, name, sell_in, quality)

	def setSellIn(self): 
		self.sell_in -= 1

	def getSellIn(self):
		return self.sell_in	

	def setQuality(self, valor):
		if self.quality	+ valor > 50:
			self.quality = 50
		elif self.quality + valor >= 0:
			self.quality += valor
		else:
			self.quality = 0	

	def getQuality(self):
		return self.quality

	def updateQuality(self):
		if self.sell_in > 0:	
			self.setQuality(-1)
		else:
			self.setQuality(-2)	
		self.setSellIn()

class AgedBrie(NormalItem):
	def __init__(self, name, sell_in, quality):
		Item.__init__(self, name, sell_in, quality)

	def updateQuality(self):
		if self.sell_in > 0:	
			self.setQuality(1)
		else:
			self.setQuality(2)	
		self.setSellIn()

class Conjured(NormalItem):
	def __init__(self, name, sell_in, quality):
		Item.__init__(self, name, sell_in, quality)	

	def updateQuality(self):
		if self.sell_in > 0:	
			self.setQuality(-2)
		else:
			self.setQuality(-4)	
		self.setSellIn()

class Backstage(NormalItem):
	def __init__(self, name, sell_in, quality):
		Item.__init__(self, name, sell_in, quality)	

	def updateQuality(self):
		self.setSellIn()
		if self.sell_in >= 0:
			if self.sell_in < 5:
				self.setQuality(3)
			elif self.sell_in < 10:
				self.setQuality(2)
			else: 		
				self.setQuality(1)
		else:
			self.quality = 0			