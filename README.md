  # Peg Solitaire Game

Welcome to the "Peg Solitaire Game," a classic single-player puzzle game implemented in Python. The goal is to clear the board by jumping over pegs, with the aim of leaving only one peg remaining.

## Game Instructions
**Objective:** The aim is to eliminate all pegs by jumping over them, leaving just one peg on the board.
**How to Play:**
   - The game begins with a standard English peg solitaire board setup.
   - Players can move pegs by entering the position of the peg and the direction of the move (L for left, R for right, U for up, D for down).
   - A valid move involves jumping over an adjacent peg into an empty space, thereby removing the jumped peg.
   - The game continues until no more valid moves can be made.
**Game End:** The game ends when no more valid moves are possible. Try to leave just one peg for the best possible result.

## Implementation Details
- The game is implemented using Python and runs in a command-line interface.
- The board is represented as a 2D list, with '1' representing a peg and '0' representing an empty space.
- Key functions manage user input, validate moves, update the game board, and check for game completion.

## How to Run
**Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/peg-solitaire.git
   cd peg-solitaire
   ```
**Ensure you have Python installed:** The game requires Python 3. Ensure it is installed on your system.
**Run the Game:**
   ```bash
   python PegSolitaire-Maria.py
   ```

## Additional Information
Feel free to modify the board configuration or rules within the Python file to create custom versions of the game. Enjoy playing!
