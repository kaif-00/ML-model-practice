from abc import ABC,abstractmethod
import zipfile

class veichel(ABC):
    @abstractmethod
    def start(self):
        # print('start')
        pass

class car(veichel):

    def start(self):
        print('Car start')

class bike(veichel):

    def start(self):
        print('Bike start')

carr = car()
carr.start()

bikee = bike()
bikee.start()