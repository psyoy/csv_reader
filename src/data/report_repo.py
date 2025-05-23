from abc import ABC, abstractmethod

class ReportRepo(ABC):
    @abstractmethod
    def save(self):
        pass
