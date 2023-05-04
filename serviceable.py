from abc import ABC, abstractmethod

class serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass