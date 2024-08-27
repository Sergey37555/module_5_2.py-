class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return title

h = House('ЖК Славянка', 9)
h2 = House('ЖК Лазурный', 25)

print(h)
print(h2)

print(len(h))
print(len(h2))