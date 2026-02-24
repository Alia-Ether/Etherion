from .main import User
import random


class EtherionUser(
    User
):
    pass


class EtherionStateClass:
    def __init__(self):
        self.ads = ''
    
    def emj(self):
        win = ['🙂', '😋', '😄', '🤑', '😃', '😇']
        loser = ['😔', '😕', '😣', '😞', '😢']
        return random.choice(win), random.choice(loser)
        
        
EtherionConst = EtherionStateClass()
