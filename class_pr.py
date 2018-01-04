class Point():
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def normal(self):
		print("Normal X pos : %s, Y pos : %s\n" % (self.x, self.y))

	def setx(self, x):
		self.x = x
		print("Set x pos is %s\n" % (self.x))

	def sety(self, y):
		self.y = y
		print("Set y pos is %s\n" % (self.y))

	def get(self):
		t1 = (self.x, self.y)
		return t1
		
	def move(self, dx, dy):
		self.x += dx
		self.y += dy
		print("Set x pos is plus %s, so x is %s\n" % (dx, self.x))
		print("Set y pos is plus %s, so x is %s\n" % (dy, self.y))

pos = Point(2,3)
pos.normal()
pos.setx(1)
pos.sety(2)
pos.normal()
print(pos.get())
pos.move(1,2)
pos.normal()
