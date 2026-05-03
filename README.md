# 🎮 Lady, Tiger, Hunter

A command-line Python game based on the classic predator-prey decision model — a twist on Rock, Paper, Scissors with a story-driven theme. Play against the computer and test your instincts!

---

## 🧠 Game Logic

The game follows a predator-prey triangle:

| Choice | Beats | Loses To |
|--------|-------|----------|
| 👩 Lady | 🐅 Tiger (tames it) | 🏹 Hunter (captured) |
| 🐅 Tiger | 🏹 Hunter (eats it) | 👩 Lady (tamed) |
| 🏹 Hunter | 👩 Lady (captures her) | 🐅 Tiger (eaten) |

---

## 🎯 Features

- 1-player mode against the computer
- Randomized computer moves for unpredictability
- Win, loss, and draw condition handling
- Interactive command-line interface
- Round-by-round score tracking

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Interface:** Command-line / Terminal

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.x installed

### Run the Game

```bash
# Clone the repository
git clone https://github.com/DivaDivya/Game-Lady-Tiger-Hunter.git

# Navigate into the project directory
cd Game-Lady-Tiger-Hunter

# Run the game
python game.py
```

---

## 🕹️ How to Play

1. Run the game in your terminal
2. When prompted, enter your choice: `Lady`, `Tiger`, or `Hunter`
3. The computer will randomly select its move
4. The winner of the round is announced
5. Keep playing rounds — first to the target score wins!

---

## 👩‍💻 Author

**Divya Sinha**  
MS Computer Science — Washington State University  
[LinkedIn](https://www.linkedin.com/in/divyasinha28) · [GitHub](https://github.com/DivaDivya)
