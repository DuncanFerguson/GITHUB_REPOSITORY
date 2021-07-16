from abc import ABCMeta, abstractmethod


class Task(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        """Starts a task instance"""
        raise NotImplemented()

    @abstractmethod
    def stop(self):
        """Stops a task instance"""
        raise NotImplemented()

    @abstractmethod
    def status(self):
        """Fetch current status of a task instance"""
        raise NotImplemented()

    @abstractmethod
    def metrics(self):
        """Fetch current status of a task instance"""
        raise NotImplemented()

    @abstractmethod
    def delete(self):
        """Delete a task instance"""
        raise NotImplemented()
