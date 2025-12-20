# 🌍 GeoWordle

GeoWordle is a terminal-based Wordle-style game where you have to **guess a country of the world** in a limited number of attempts.

Inspired by Wordle, but focused on **geography**, this game challenges you to identify the correct country using letter-based feedback (green, yellow, and gray).

---

## How to Play

- The game randomly selects a **country** from a predefined list.
- You have **7 attempts** to guess it.
- After each valid guess, the game shows colored feedback:
  - **Green** → correct letter in the correct position
  - **Yellow** → correct letter in the wrong position
  - **Gray** → letter not in the word
- Invalid guesses (wrong length or not in the country list) **do NOT consume an attempt**.

---

## Controls

- Type the name of a country and press **Enter**.
- Input is **case-insensitive**.
- Only countries included in the list are accepted.

---

## Project Structure

.
├── geowordle.py # Main game script
├── countries.txt # List of valid countries (one per line)
└── README.md

---

## Country List

- Countries are stored in `countries.txt`
- One country per line
- All names are normalized (lowercase)
- Only **sovereign countries** are included
- Territories and dependencies are excluded for fairness

You can easily replace `countries.txt` to create your own themed Wordle!

---

## Features

- Wordle-style letter evaluation
- Color-coded terminal output
- Input validation without wasting attempts
- Fast lookup using Python `set`
- Clean ASCII-art title screen
- Easy to extend and customize

---

## Running the Game

Make sure you have **Python 3** installed.

```bash
python geowordle.py
The game runs directly in the terminal.

Customization Ideas
Add difficulty levels

Ignore spaces automatically (e.g. unitedstates)

Add categories (Europe, Africa, Asia…)

Track win statistics

Add a hard mode

Change theme (animals, food, movies, etc.)

What I Learned
This project helped me practice:

File handling in Python

Loops and conditionals

Functions and clean code structure

Sets vs lists for performance

Game logic and validation

Terminal UI and ASCII art

📜 License
This project is for learning and personal use.
Feel free to fork, modify, and experiment with it!

Have fun playing GeoWordle 🌍
