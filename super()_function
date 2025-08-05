    # Super() funtion
    class Parent:
        def __init__(self, name):
            self.name = name
            print(f"Parent __init__ called for {self.name}")

    class Child(Parent):
        def __init__(self, name, age):
            super().__init__(name)  # Calls Parent's __init__
            self.age = age
            print(f"Child __init__ called for {self.name}, age {self.age}")

    child_obj = Child("Alice", 10)
