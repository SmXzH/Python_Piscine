from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''
    Class representing a King character, inheriting from Baratheon and Lannister.
    
    :param first_name: First name of the King character.
    :param is_alive: Boolean indicating if the King character is alive. Default is True.
    
    '''
    def __init__(self, first_name, is_alive=True):
        '''
        Constructor for the King class.

        :param first_name: First name of the King character.
        :param is_alive: Boolean indicating if the King character is alive. Default is True.
        '''
        super().__init__(first_name, is_alive)
    
    def set_eyes(self, color):
        '''
        Method to set the eye color of the King character.

        :param color: Eye color of the King character.
        '''
        self.eye_color = color

    def set_hairs(self, color):
        '''
        Method to set the hair color of the King character.
        
        :param color: Hair color of the King character.
        '''
        self.hair_color = color
    
    def get_eyes(self):
        '''
        Method to get the eye color of the King character.
        
        :return: Eye color of the King character.
        '''
        return self.eye_color
    
    def get_hairs(self):
        '''
        Method to get the hair color of the King character.
        
        :return: Hair color of the King character.
        '''
        return self.hair_color