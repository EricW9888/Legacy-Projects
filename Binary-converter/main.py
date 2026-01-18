binaries = []
decimals = []
strings = []
type = input("Binary to string or string to binary?")
input = input("Input?")
ascii = [(" ", 32), ("!", 33), ('"', 34), ("#", 35), ("$", 36), ("%", 37), ("&", 38), ("'", 39), ("(", 40), (")", 41), ("*", 42), ("+", 43), (",", 44), ("-", 45), (".", 46), ("/", 47), ("0", 48), ("1", 49), ("2", 50), ("3", 51), ("4", 52), ("5", 53), ("6", 54), ("7", 55), ("8", 56), ("9", 57), (":", 58), (";", 59), ("<", 60), ("=", 61), (">", 62), ("?", 63), ("@", 64), ("A", 65), ("B", 66), ("C", 67), ("D", 68), ("E", 69), ("F", 70), ("G", 71), ("H", 72), ("I", 73), ("J", 74), ("K", 75), ("L", 76), ("M", 77), ("N", 78), ("O", 79), ("P", 80), ("Q", 81), ("R", 82), ("S", 83), ("T", 84), ("U", 85), ("V", 86), ("W", 87), ("X", 88), ("Y", 89), ("Z", 90), ("[", 91), ("\\", 92), ("]", 93), ("^", 94), ("_", 95), ("`", 96), ("a", 97), ("b", 98), ("c", 99), ("d", 100), ("e", 101), ("f", 102), ("g", 103), ("h", 104), ("i", 105), ("j", 106), ("k", 107), ("l", 108), ("m", 109), ("n", 110), ("o", 111), ("p", 112), ("q", 113), ("r", 114), ("s", 115), ("t", 116), ("u", 117), ("v", 118), ("w", 119), ("x", 120), ("y", 121), ("z", 122), ("{", 123), ("|", 124), ("}", 125), ("~", 126)]

def binary_to_string(ascii, input, binaries, decimals):  
  temp = ""
  string = ""
  
  binary = input.strip()
  for digit in binary:
    temp += digit
    if len(temp) == 8:
      binaries.append(temp)
      temp = ""
      
  for byte in binaries:
    temp = int(byte, 2)
    decimals.append(temp)
  
  for decimal in decimals:
    found = 0
    for code in ascii:
      if decimal == code[1]:
        found += 1
        string += code[0]
        
      else:
        pass

    if found == 0:
      string += "� "

  output = print("\n\nDecimal:", decimals, "\n\nString:", string)
  return output
  
def string_to_binary(ascii, input, strings, decimals):
  temp = ""
  binary = ""

  string = input
  for character in string:
    for code in ascii:
      if character == code[0]:
        decimals.append(code[1])

      else:
        pass

  for decimal in decimals:
    temp = bin(decimal)[2:]
    if len(temp) < 8:
      difference = 8 - len(temp)
      missing = ""
      for digit in range(difference):
        missing += "0"
      
      add = missing + str(temp)
      temp = add
      
    binary += temp

  output = print("\n\nDecimal:", decimals, "\n\nBinary:", binary)
  return output

if type == "binary":
  binary_to_string(ascii, input, binaries, decimals)
  
elif type == "string":
  string_to_binary(ascii, input, strings, decimals)