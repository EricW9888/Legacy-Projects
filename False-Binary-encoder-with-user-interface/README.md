# False Binary Encoder (UI)

- Language: Python (Tkinter)
- Completion date: September 2022

A Tkinter utility for encoding printable ASCII messages into a transformed binary string and decoding them with a two-digit key. Encoding subtracts a random offset from each character code, converts it to an eight-bit value, reverses and rotates the bits, then flips zeroes and ones. The key records the rotation and offset so decoding can reverse those steps.

This is an educational encoding experiment, not secure encryption. `main.py` provides the graphical interface; `main1.py` preserves an earlier command-line version.

## Usage

- To encode, enter a message, select only **Encode**, and click **Convert**. The output includes the encoded bits and decoding key.
- To decode, paste only the encoded bits into the message field, enter the two-digit key, select only **Decode**, and click **Convert**.
- The character table covers printable ASCII; this is not a general Unicode encoder.

## Run

Requires Python 3.11 or newer with Tkinter support. No Pygame dependency. From the repository root:

```sh
python3.11 False-Binary-encoder-with-user-interface/main.py
```

Inside this project folder, use `python3.11 main.py` instead. Check Tkinter availability with `python3.11 -m tkinter`.

## Files

- `main.py` — the Tkinter version, with message/key fields and encode/decode checkboxes.
- `main1.py` — the earlier console version driven by `input()` prompts, kept for history.

## Screenshot

![Original False Binary Encoder interface showing an encoded example message](encoder.png)

[Original portfolio entry](https://ericwang-digital-portfolio.pages.dev/computer_science.html#False%20binary%20encoder%20with%20user%20interface) · [Archive overview](../README.md)
