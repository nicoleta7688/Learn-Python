from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self):
        move = random.choice(self.moves)
        x = self.position[0] + move[0]
        y = self.position[1] + move[1]
        self.position = (x, y)

        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),    # up
            (0, -1),   # down
            (-1, 0),   # left
            (1, 0)     # right
        ]
    
    def level_up(self):
        self.moves.append((1,1)) # right-top
        self.moves.append((-1,1)) # left-top
        self.moves.append((1,-1)) # right-bottom
        self.moves.append((-1,-1)) # left-bottom


#test:
pawn = Pawn()

print("Initial position:", pawn.position)
print("Initial moves:", pawn.moves)

print("\nMaking 5 random moves:")
for i in range(5):
    print(f"Move {i + 1}: {pawn.make_move()}")

print("\nPath:")
print(pawn.path)

print("\nLevel up!")
pawn.level_up()

print("\nMoves after level up:")
print(pawn.moves)

print("\nMaking 5 more random moves:")
for i in range(5):
    print(f"Move {i + 1}: {pawn.make_move()}")

print("\nFinal position:")
print(pawn.position)

print("\nComplete path:")
for pos in pawn.path:
    print(pos)