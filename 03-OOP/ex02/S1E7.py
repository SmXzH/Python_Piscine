from S1E9 import Character

class Baratheon(Character):
    '''
    Class representing a Baratheon character, inheriting from Character.

    :param first_name: First name of the Baratheon character.
    :param is_alive: Boolean indicating if the Baratheon character is alive. Default is True.

    '''
    def __init__(self, first_name, is_alive=True):
        '''
        Constructor for the Baratheon class.
        
        :param first_name: First name of the Baratheon character.
        :param is_alive: Boolean indicating if the Baratheon character is alive. Default is True.
        '''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.hair_color = "brown"
        self.eye_color = "blue"
    
    def die(self):
        '''
        Method to change the health state of the Baratheon character to dead.
        '''
        self.is_alive = False

class Lannister(Character):
    '''
    Class representing a Lannister character, inheriting from Character.

    :param first_name: First name of the Lannister character.
    :param is_alive: Boolean indicating if the Lannister character is alive. Default is True.

    '''
    
    def __init__(self, first_name, is_alive=True):
        '''
        Constructor for the Lannister class.

        :param first_name: First name of the Lannister character.
        :param is_alive: Boolean indicating if the Lannister character is alive. Default is True.
        '''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.hair_color = "light"
        self.eye_color = "blue"
    
    def die(self):
        '''
        Method to change the health state of the Lannister character to dead.
        '''
        self.is_alive = False
    
    @classmethod
    def create_lannister(cls, first_name, is_alive):
        '''
        Method to create a Lannister character.

        :param first_name: First name of the Lannister character.
        :param is_alive: Boolean indicating if the Lannister character is alive.
        :return: Instance of the Lannister class.
        '''
        isinstance = cls(first_name)
        isinstance.is_alive = is_alive
        return isinstance