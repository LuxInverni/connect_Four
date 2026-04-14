🎮 Connect 4 (Python + Pygame)

A fully playable Connect 4 game built in Python using Pygame, featuring:

🎮 Local 2-player mode
🤖 AI opponent (heuristic-based)
📐 Responsive, resizable board rendering
🧠 Clean game-state architecture
🎯 Hover previews + win detection
🧩 Modular codebase (UI / game logic / AI separated)
🚀 Features
🎮 Game Modes
Player vs Player (local hot-seat)
Player vs AI
🤖 AI Opponent
Evaluates board states using a scoring heuristic
Prioritises:
Winning moves
Blocking opponent wins
Center column control

(Can be extended to minimax / alpha-beta pruning)

🖥️ Responsive UI
Fully resizable window
Dynamic scaling board
Centered grid layout
Smooth hover indicator for active column
Clean menu + game-over screens
🧠 Game Logic
Robust win detection:
Horizontal
Vertical
Diagonal (both directions)
Column validation
Gravity-based piece placement
Turn management system supporting both PvP and AI modes
🧱 Project Structure
connect-four/
│
├── game.py          # Main game loop + state machine
├── board.py         # Game logic (board, moves, win detection)
├── ui.py            # Rendering (menu, board, game over)
├── ai.py            # AI move selection logic
├── constants.py     # Shared constants (colors, dimensions)
🔁 Game Flow

The game is structured using a state machine:

MENU
PLAYING
GAME_OVER

Each frame:

Handle input events
Update game state
Render correct screen based on state

This avoids deeply nested logic and keeps rendering separate from gameplay.

🧠 AI Logic Overview

The AI evaluates all possible moves and assigns a score based on:

Immediate win detection
Blocking opponent wins
Center column preference
Simple positional heuristics

This creates a reactive but competitive opponent without needing heavy computation.

📦 Requirements
pip install pygame numpy
▶️ Run the Game
python game.py
🎯 Controls
Menu
P → Player vs Player
A → Player vs AI
Q → Quit
Gameplay
Move mouse → preview column
Click → drop piece
R (Game Over) → restart
🛠️ What I Learned

This project was focused on:

Refactoring a monolithic Pygame script into modules
Handling real-time game state management
Fixing coordinate system mismatches in grid-based rendering
Designing a basic AI opponent
Building responsive UI scaling logic in Pygame
🔮 Future Improvements
Minimax AI with depth control
Animation system for falling pieces
Sound effects + polish
Online multiplayer (socket-based)
Undo / replay system
Difficulty levels for AI

License

MIT License © 2026 Lucy Winters
