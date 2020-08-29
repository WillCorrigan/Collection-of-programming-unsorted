class PlayerCharacter:
    membership = True

    def __init__(self, name):
        self.name = name


player1 = PlayerCharacter("Herald")
print(player1.name)

print(player1.membership)  # membership is True
player1.membership = False  # set class attribute object as False
print(player1.membership)  # membership is False

player2 = PlayerCharacter("John")
print(f'player2 membership: {player2.membership}') # output is true, so membership is always set to True in each instance 
print(f'player1 membership: {player1.membership}')