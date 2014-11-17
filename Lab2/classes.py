class Animal():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def sleep(self):
		print self.name, "of age", self.age, "is sleeping"
class Bird(Animal):
	def __init__(self, name, age, wings_color):
		Animal.__init__(self,name, age)
		self.wings_color = wings_color

class Human(Animal):
	def __init__(self, name, age, skill):
		Animal.__init__(self,name,age)
		self.skill = skill
		
	def sayskill(self):
		print "My skill is", self.skill


rami = Human("Rami", 35, "CS")
rami.sayskill()		
a = Animal("Rami", 35)
a.sleep()
