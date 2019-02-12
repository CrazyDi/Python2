from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):
    def feed(self):
        print("I eat grass")

    def move(self):
        print("I walk forward")

    def make_noise(self):
        print("WOOO!")


class AbstractDecorator(Creature):
    def __init__(self, obj):
        self.obj = obj

    def feed(self):
        self.obj.feed()

    def move(self):
        self.obj.move()

    def make_noise(self):
        self.obj.make_noise()


class Swimming(AbstractDecorator):
    def move(self):
        print("I swim")

    def make_noise(self):
        print("...")


class Predator(AbstractDecorator):
    def feed(self):
        print("I eat other animals")


class Fast(AbstractDecorator):
    def move(self):
        self.obj.move()
        print("Fast!")


if __name__ == "__main__":
    print("Animal:")
    animal = Animal()
    animal.feed()
    animal.move()
    animal.make_noise()

    print("Swimming:")
    swimming = Swimming(animal)
    swimming.feed()
    swimming.move()
    swimming.make_noise()

    print("Predator:")
    predator = Predator(swimming)
    predator.feed()
    predator.move()
    predator.make_noise()

    print("Fast:")
    fast = Fast(predator)
    fast.feed()
    fast.move()
    fast.make_noise()

    print("Faster:")
    faster = Fast(fast)
    fast.feed()
    fast.move()
    fast.make_noise()

    print("Faster, not predator:")
    faster.obj.obj = faster.obj.obj.obj
    fast.feed()
    fast.move()
    fast.make_noise()
