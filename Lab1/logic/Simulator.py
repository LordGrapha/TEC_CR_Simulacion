from model.Dice import Dice

class Simulator():
    """
    
    """
    dice = None
    n = 0
    k = 0

    def __init__(self, pC, pN, pK) -> None:
        """
        """
        self.dice = Dice(pC)

    def startSimulation(self):
        """
        """
        pass

    """"
    main
        -> logic
            -> Simulator
        -> model
            -> Dice
    
    """