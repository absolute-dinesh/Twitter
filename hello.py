class Greeting:
	def __init__(self,fname,lname,age,gender):
		self.fname = fname
		self.lname = lname
		self.age = age
		self.gender = gender

	def greet(self):
		#print("Hello "+self.fname +" "+self.lname)
		print("Hello Mr.{} {}".format(self.fname,self.lname))

if __name__ == '__main__':
	person1 = Greeting("Dinesh","Reddy",25,"Male")

	person1.greet()