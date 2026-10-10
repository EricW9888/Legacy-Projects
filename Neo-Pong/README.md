# Neo Pong

- Language: Python (pygame)
- Completion date: December 2022

A local two-player Pong game. Players move opposing paddles to return the ball; a missed return awards a point to the other side. The ball speeds up after paddle hits, and the first player to ten points wins.

The game includes a start countdown and sounds for paddle hits, scoring, and the end of a match. The court, paddles, and ball are supplied as game artwork.

## Controls

- Click or press a key on the welcome screen to start.
- **W / S**: move the left paddle up/down.
- **Up / Down Arrow**: move the right paddle up/down.
- Click or press a key on the game-over screen to restart.

## Run

From the repository root:

```sh
python3.11 -m pip install pygame
python3.11 Neo-Pong/main.py
```

Inside this project folder, use `python3.11 main.py` instead. Keep `images/` and `sounds/` alongside the source; the court background is illustrated game artwork, not a blank-color placeholder.

## Screenshot

![Original Neo Pong court with left and right paddles, a ball, and scores](pong.png)

[Original portfolio entry](https://ericwang-digital-portfolio.pages.dev/computer_science.html#Neo%20pong) · [Archive overview](../README.md)
