# lib/dog.py

class Dog:
    # Instance method to make the dog bark
    def bark(self):
        print("Woof!")

    # Instance method to make the dog sit
    def sit(self):
        print("The dog is sitting.")


# Example usage
if __name__ == "__main__":
    fido = Dog()
    fido.bark()  # Woof!
    fido.sit()   # The dog is sitting.

    snoopy = Dog()
    snoopy.bark()  # Woof!
    snoopy.sit()   # The dog is sitting.
