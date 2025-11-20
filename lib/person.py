# lib/person.py

class Person:
    # Instance method to make the person talk
    def talk(self):
        print("Hello World!")

    # Instance method to make the person walk
    def walk(self):
        print("The person is walking.")


# Example usage
if __name__ == "__main__":
    alice = Person()
    alice.talk()  # Hello World!
    alice.walk()  # The person is walking.
