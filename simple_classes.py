# type hinting
colors: list = list()   #   list colors = new list();
colors.append("red")
colors.append("pink")
colors.append("purple")
print(f"{colors = }")

x = 5   #  x = int(5)

class Dog:
    def bark(self):
        print("Woof! woof!")


d1 = Dog()
d2 = Dog()
d3 = Dog()
d1.bark()  # self is d1
d3.bark()  # self is d3