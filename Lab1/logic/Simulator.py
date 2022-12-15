from random import randrange
from model.Dice import Dice

class Simulator():
    """
    
    """
    dice = None     #Dice is the one that will gives us the numbers for each roll
    n = 0           #n is how many times we are gonna play the dice roll in one experiment (in each k experiment)
    k = 0           #k is how many experiments we are going to simulate
    resultSimulation = {}

    def __init__(self, pC, pN, pK) -> None:
        """
        Constructs the Simulator to get dice rolls with specified parameters
        In: pC is the number of sides for the dice
            pN is the number of rolls
            pK is the number of experiments for the simulation
        Out: Instance
        Restrictions: None
        """
        self.dice = Dice(pC)
        self.n = pN
        self.k = pK
        self.resultSimulation = dict()

    def startSimulation(self):
        """
        This method applies all the cycles and random dice roll, getting the sum of all the 
        rolls in one experiment and hashing it in resultSimulation attribute
        In: None
        Out: Hashmap with (key = sum) : (value = number of appearances)
        Restrictions: None
        """
        #Iterate for each experiment
        for experiment in range(self.k):
            #Sum will accumulate the roll values in all the n dice rolls
            sum = 0
            #Iterate for each n dice roll for one experiment
            for roll in range(self.n):
                sum += self.__rollDice()
            #Once all the n dice rolls are done and sum is done, we hashed it to count the appearances of that number
            #if the number has already appeared before, the sum 1 appearance to it
            if self.resultSimulation.get(sum, False):
                self.resultSimulation[sum] += 1
            #if its the first time we get the sum number, then add it to the hash and set 1 appearance
            else:
                self.resultSimulation[sum] = 1

        #May the force be with u
        return self.resultSimulation

    def __rollDice(self):
        #Random from 1 to dice sides
        return randrange(self.dice.sides) + 1
