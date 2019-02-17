class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, type):
        self.type = type
        self.kind = "get"


class EventSet:
    def __init__(self, value):
        self.value = value
        self.kind = "set"


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, val, event):
        if self.__successor is not None:
            return self.__successor.handle(val, event)


class IntHandler(NullHandler):
    def handle(self, val, event):
        if event.kind == "get":
            if event.type == int:
                return val.integer_field
            else:
                return super().handle(val, event)
        elif event.kind == "set":
            if type(event.value) == int:
                val.integer_field = event.value
            else:
                super().handle(val, event)


class FloatHandler(NullHandler):
    def handle(self, val, event):
        if event.kind == "get":
            if event.type == float:
                return val.float_field
            else:
                return super().handle(val, event)
        elif event.kind == "set":
            if type(event.value) == float:
                val.float_field = event.value
            else:
                super().handle(val, event)


class StrHandler(NullHandler):
    def handle(self, val, event):
        if event.kind == "get":
            if event.type == str:
                return str(val.string_field)
            else:
                return super().handle(val, event)
        elif event.kind == "set":
            if type(event.value) == str:
                val.string_field = event.value
            else:
                super().handle(val, event)


if __name__ == "__main__":
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))

    obj = SomeObject()

    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(str)))
    print(chain.handle(obj, EventGet(float)))
    chain.handle(obj, EventSet(1))
    chain.handle(obj, EventSet(1.1))
    chain.handle(obj, EventSet("str"))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(str)))
    print(chain.handle(obj, EventGet(float)))
    chain.handle(obj, EventSet(2))
    chain.handle(obj, EventSet(22.22))
    chain.handle(obj, EventSet("ertgergye"))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(str)))
    print(chain.handle(obj, EventGet(float)))