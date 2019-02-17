from abc import ABC, abstractmethod


class Engine:
    pass


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, item):
        for subscriber in self.__subscribers:
            subscriber.update(item)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, item):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, item):
        if item["title"] not in self.achievements:
            self.achievements.add(item["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, item):
        if item not in self.achievements:
            self.achievements.append(item)


if __name__ == "__main__":
    engine = ObservableEngine()

    short1 = ShortNotificationPrinter()
    short2 = ShortNotificationPrinter()
    full1 = FullNotificationPrinter()
    full2 = FullNotificationPrinter()

    engine.subscribe(short1)
    engine.subscribe(short2)
    engine.subscribe(full1)
    engine.subscribe(full2)

    engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})

    print(short1.achievements)
    print(short2.achievements)
    print(full1.achievements)
    print(full2.achievements)

    engine.notify({"title": "Покоритель2", "text": "Дается при выполнении всех заданий в игре2"})

    print(short1.achievements)
    print(short2.achievements)
    print(full1.achievements)
    print(full2.achievements)


