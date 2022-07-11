class Planet:
	def __init__ (self,name,radius,gravity):
		self.name=name
		self.radius=radius
		self.gravity=gravity
hoth= Planet('hot', 200000, 5.5)
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'The gravity is: {hoth.gravity}')
def gun_dec(func):
	def func_wrapper():
		print('*gun*')
		func()
		print('*gun*')
	return func_wrapper
@gun_dec
def question():
	print('how old are you')
@gun_dec
def answer():
	print("I'm 20 years old")
question()
answer()






class Planet:
	def __init__(self,name,radius,gravity,system):
		self.__name=name
		self.__radius=radius
		self.__gravity=gravity
		self.system=system
	def set_name(self,name):
		self.__name=name
	def set_radius(self,radius):
		self.__radius=radius
	def set__gravity(self,gravity):
		self.__gravity=gravity
	def set_system(self,system):
		self.__system = system
	def get_name(self):
		return self.__name
	def get_radius(self):
		return self.__radius
	def get_gravity(self):
		return self.__gravity
	def get_system(self):
		return self.__system
import planet
def main():
	name=input()
	radius=int(input())
	gravity=float(input())
	system=input()
	print('Here is the data you enter')
	print('name is:', planet.get_name())
	print('radius:', planet.get_radius())
	print('gravity is:', format(planet.get_gravity, ',.2f'), sep= ' ')
	print('system is:', planet.get_system())
main()