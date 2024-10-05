from abc import ABC, abstractmethod

class Character(ABC):
    """
    Abstract base class representing a character.
    """

    def __init__(self, first_name,family_name, is_alive=True):
        """
        Constructor for the Character class.

        :param first_name: First name of the character.
        :param is_alive: Boolean indicating if the character is alive. Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name

    @abstractmethod
    def die(self):
        """
        Abstract method to change the health state of the character to dead.
        """
        pass

    def __str__(self):
        """
        Method to return the string representation of the character.

        :return: String representation of the character.
        """
        return f"Vector: ({self.family_name}, {self.eye_color}, {self.hair_color})"

    def __repr__(self):
        """
        Method to return the string representation of the character.

        :return: String representation of the character.
        """
        return self.__str__()

class Stark(Character):
    """
    Class representing a Stark character, inheriting from Character.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor for the Stark class.

        :param first_name: First name of the Stark character.
        :param is_alive: Boolean indicating if the Stark character is alive. Default is True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Method to change the health state of the Stark character to dead.
        """
        self.is_alive = False
