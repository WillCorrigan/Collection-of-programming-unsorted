from operator import attrgetter

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_oldest_cat(listName):
    return max(listName, key=attrgetter('age'))


yoshi = Cat('Yoshi', 6)
tali = Cat('Tali', 4)
rufus = Cat('Rufus', 8)
dog = Cat('Dog', 22)

cats = [yoshi, tali, rufus, dog]

print(f"The oldest cat is {get_oldest_cat(cats).name}, they are {get_oldest_cat(cats).age} years old.")