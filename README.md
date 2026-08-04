# Legacy Projects (archived Replit work)

Old Python projects exported from Replit, kept as-is for reference. This repository is archived and receives no further maintenance. Project code and per-project screenshots are tracked together; each project folder has its own README.

## Quick start
- Requires Python 3.8–3.11.
- Most games/visualizers use `pygame`; install with `pip install pygame`.
- Run `python3 main.py` from anywhere — each pygame script sets its own working directory so relative asset paths resolve.
- Tkinter apps ship with the standard library on Windows/macOS; Linux may need `sudo apt-get install python3-tk`.

## Project list and completion dates

Listed oldest to newest.

| Project | Completed | Description | Screenshot |
| --- | --- | --- | --- |
| `Water-drop-catcher` | Apr 2022 | Pygame catcher; standard drops are 1 point, golden drops 5, three lives. | `catcher.png` |
| `Neo-Pong` | Sep 2022 | Two-player Pygame pong with sounds; W/S and arrow keys, first to 10 wins. | `pong.png` |
| `Floppy-fish` | Dec 2022 | Pygame side-scroller; steer a fish through pipe gaps with W/S or arrows, three lives. | `fish.png` |
| `Bubble-sort-visualization` | Jan 2023 | Pygame visualization over values 1–250, highlighting the active comparison with timing and comparison count. | — |
| `False-Binary-encoder-with-user-interface` | Jan 2023 | Tkinter encoder/decoder that shifts ASCII codes, reverses/rotates bits, and uses a two-digit key. | `encoder.png` |
| `Single-Player-Neo-Pong` | Feb 2023 (approx.) | Solo pong versus an AI paddle, forked from `Neo-Pong` and sharing its assets. | — |
| `Floppy-fish-2` | Apr 2023 | Sequel with space-bar jump controls and five lives. | `fish2.png` |
| `maze-solver-dfs` | Apr 2023 | Pygame depth-first/backtracking maze solver visualizer. | `maze.png` |
| `maze-solver-bfs` | Apr 2023 | Pygame breadth-first style maze explorer. | `maze2.png` |

The original Replit export did not preserve timestamps, so dates were reconstructed from a contemporaneous portfolio listing. `Single-Player-Neo-Pong` had no recorded date; it is a fork of `Neo-Pong` (identical assets and `sprites.py`, with the Player 1 paddle replaced by ball-tracking AI), so it necessarily postdates Sep 2022, and Feb 2023 is a best estimate rather than a confirmed date.

## Notes
- `False-Binary-encoder-with-user-interface/main1.py` is the earlier console version of the encoder, kept alongside the Tkinter `main.py` it grew into.
- Files such as `trail.png`, `wall.png`, and `path.png` inside the maze solvers are sprite assets, not screenshots.
- `Bubble-sort-visualization` and `Single-Player-Neo-Pong` have no screenshot on record.
