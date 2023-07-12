import random

class DiceController():
    @staticmethod
    def roll(max: int) -> int:
        """Rolls a die with the specified number of sides.
        """
        return random.randint(1, max)

    @staticmethod
    def roll_sum(max: int, amt: int) -> int:
        """Rolls the specified die amt of times and sums up the values.
        """
        result = 0
        for idx in range(0, amt):
            result += DiceController.roll(max)
        return result
