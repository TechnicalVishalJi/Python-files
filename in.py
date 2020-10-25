class  Electronic_device:
	Speed = 8
	
class Pocket_gadget(Electronic_device):
	def __init__(self, n):
		self.name = n
		
	def details(self):
		return f"{self.name} is a pocket gadget that has a small size"
		
	
class Phone(Pocket_gadget):
	pass
	
	
Laptop = Electronic_device()
Mobile = Phone("Mobile")
Scanner = Pocket_gadget("Scanner" )

print(Mobile.Speed)
print(Mobile.details())