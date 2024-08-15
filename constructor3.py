class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Creating instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Bella", "Labrador")

# Accessing instance attributes
print(dog1.name)  # Output: Buddy
print(dog2.breed) # Output: Labrador
