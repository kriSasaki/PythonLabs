class ParentClass:
    def display(self):
        print("Это метод display из родительского класса")

class ChildClass(ParentClass):
    def display(self):
        print("Это метод display из дочернего класса")

# Создаем объекты
parent_object = ParentClass()
child_object = ChildClass()

# Вызываем методы display для каждого объекта
parent_object.display()
child_object.display()

