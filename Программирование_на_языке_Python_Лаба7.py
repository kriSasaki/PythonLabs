class ParentClass:
    def display(self):
        print("Это метод display из родительского класса")

class ChildClass(ParentClass):
    def display(self):
        print("Это метод display из дочернего класса")

parent_object = ParentClass()
child_object = ChildClass()

parent_object.display()
child_object.display()

