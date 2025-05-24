from abc import ABC, abstractmethod

class ReportCreator(ABC):
    @abstractmethod
    def create(self):
        pass
