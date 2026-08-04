# False Binary Encoder (UI)

- Language: Python (Tkinter)
- Completion date: January 2023

Tkinter encoder/decoder that shifts ASCII codes by a random offset, reverses and rotates bits, and flips them to produce an encoded string. Decoding requires the two-digit key (rotation + offset) to restore the original message.

## Run
- Python 3.8–3.11 with Tkinter (install `python3-tk` on Debian/Ubuntu if needed).
- From this folder: `python3 main.py`.

## Files
- `main.py` — the Tkinter version, with message/key fields and encode/decode checkboxes.
- `main1.py` — the earlier console version driven by `input()` prompts, kept for history.

## Screenshot
- `encoder.png`
