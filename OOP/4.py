class Person:
    name = "Undefined"

    def print_name(self):
        print(self.name)


tom = Person()
bob = Person()
tom.print_name()  # Undefined
bob.print_name()  # Undefined

bob.name = "Bob"
bob.print_name()  # Bob
tom.print_name()  # Undefined