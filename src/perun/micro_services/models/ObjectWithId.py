from abc import ABC, abstractmethod


class ObjectWithId(ABC):

    @abstractmethod
    def getId(self):
        pass