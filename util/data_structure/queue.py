from queue import SimpleQueue as PyQueue

from models.token import Token


class Queue:
    def __init__(self, from_list: list[Token]|tuple[Token]):
        self.__queue = PyQueue()
        for element in from_list:
            self.__queue.put(element)
        self.__last_item: Token = None

    def peek(self) -> Token:
        if self.__last_item is None:
            if self.__queue.empty():
                return None
            self.__last_item = self.__queue.get()
        return self.__last_item

    def remove(self) -> Token:
        to_return = self.__last_item
        self.__last_item = None
        return to_return
