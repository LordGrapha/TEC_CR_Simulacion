class Dice():
    """
    
    """
    sides = 0


    def __init__(self, pSides) -> None:
        """
        """
        self.sides = pSides

    def roll(self):
        """
        """
        if self.sides == 0:
            return 0
        #Logic with all the sides and probabilities