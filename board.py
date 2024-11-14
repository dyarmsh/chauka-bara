import random

# Define the board using your original coordinates
board_setup = [
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4),
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
    (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4)
]

class Board:
    safe_cells = [(0, 2), (2, 0), (4, 2), (2, 4)]
    winning_cell = (2, 2)

    # Updated player routes based on your clarification
    player_routes = {
        0: [
            (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), 
            (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0), 
            (0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), 
            (2, 3), (1, 3), (1, 2), (2, 2)
        ],
        1: [
            (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), 
            (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), 
            (0, 4), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), 
            (3, 2), (3, 3), (2, 3), (2, 2)
        ],
        2: [
            (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0), 
            (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), 
            (4, 4), (4, 3), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), 
            (2, 1), (3, 1), (3, 2), (2, 2)
        ],
        3: [
            (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), 
            (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), 
            (4, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), 
            (1, 2), (1, 1), (2, 1), (2, 2)
        ]
    }

    def __init__(self):
        self.players = [Player(i) for i in range(4)]

    def move_player(self, player_id, steps):
        """Move a specific player on their route."""
        player = self.players[player_id]
        new_position = player.move_piece(steps)
        if new_position is None:
            print(f"Player {player_id} did not move.")
        else:
            print(f"Player {player_id} moved to {new_position}")
            return new_position

    def get_player_position(self, player_id):
        """Get the current position of a specific player."""
        player = self.players[player_id]
        return player.get_current_position()


class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.position_index = 0  # Track player's current position on their route
        self.route = Board.player_routes[player_id]

    def move_piece(self, steps):
        """Move the player's piece according to their route."""
        if (self.position_index + steps) <= (len(self.route)-1):
            new_index = self.position_index + steps
            self.position_index = new_index
            return self.get_current_position()
        else:
            return None
        

    def get_current_position(self):
        """Get the player's current position on the board."""
        return self.route[self.position_index]


# Testing the updated setup
if __name__ == "__main__":
    game_board = Board()
    
    dice_rolls = [1, 2, 3, 4, 8]

    current_player_id = 0

    while True:
        current_dice_roll = random.choice(dice_rolls)
        print(f"Player {current_player_id} rolled {current_dice_roll}")
        game_board.move_player(current_player_id, current_dice_roll)

        if game_board.players[current_player_id].get_current_position() == Board.winning_cell:
            print(f"Player {current_player_id} wins!")
            break
        else:
            current_player_id = (current_player_id + 1) % len(game_board.players)
            print("\n")
        

    # game_board.move_player(1, 3)  # Player 1 moves by 3 steps
    # game_board.move_player(2, 5)  # Player 2 moves by 5 steps
    # game_board.move_player(3, 4)  # Player 3 moves by 4 steps
    # game_board.move_player(4, 6)  # Player 4 moves by 6 steps

    # Check current positions
    # print("\nCurrent positions:")
    # for i in range(1, 5):
    #     print(f"Player {i}: {game_board.get_player_position(i)}")
