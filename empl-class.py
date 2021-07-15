# working with class
class Employees:
    """This is employees records"""

    def __init__(self,name,idn,birth,status,dept,post):
        self.name = name
        self.id = idn
        self.birth = birth
        self.merital = status
        self.department = dept
        self.title = post
        pass

    # intro
    def __str__(self):
        return f"My name is {self.name}. I have joined as {self.title} in {self.department}"
        pass
    # directors details

    def __directors(self):
        return f"{self.name},{self.id},{self.merital},{self.department},{self.title}"

# instances begins
ict1 = Employees("Robert","29782071",1999,"single","ict","ict manager")
ict2 = Employees("Jitendra","389120",1989,"married","ict","ict head")

print(ict1.name)
print(ict1)
print(ict2.name)
print(ict2)
# who is ict1
print(ict1.__str__())
pass
print(" who is ict2")
print(f"***\nwho is ict2\n{ict2.__str__()}\n***")
print("\n call a private method")
print(ict1._Employees__directors())

# private employees
pass
print("private employees\n")
pass
print(ict1._Employees__directors())
print(ict1)

class Shelys(Employees):
    def __init__(self,name,idn,birth,status,post,dept,joining):
        super().__init__(name,idn,birth,status,dept,post)
        self.joindate = joining

    def __repr__(self):
        return f"name: {self.name},id: {self.id},Date of birth: {self.birth},Status: {self.merital},Department: {self.department},Job title: {self.title},Joining Date: {self.joindate}"

ict_shelys = Shelys("Zuma","10002",1942,"single","ict","executive ict",1972)

print(isinstance(ict_shelys,Shelys))
print("__str & __repr__ display below")
print(ict_shelys.__repr__())
print(ict_shelys.__str__())
print("**call private method from main class**")
print(ict_shelys._Employees__directors())
print(issubclass(Shelys,Employees))
pass
# appending, inserting into a list
item = []

item.append(ict1.__str__())
item.insert(0,ict_shelys.__repr__())
pass
# display
print("\n****")
print(f"{item}\n***")
