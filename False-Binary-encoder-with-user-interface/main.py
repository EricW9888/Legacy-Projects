import random
import tkinter as tk
import sys
from tkinter import *
import tkinter.scrolledtext as tksc

sys.set_int_max_str_digits(0)
root = tk.Tk()
root.wm_geometry("440x450")
root.wm_title("False binary encoder")
root['background']='#18191A'
label = tk.Label(text="Encode", font=('Arial', 11), fg='white', bg='#18191A')
label.place(x=50, y=200)
var1 = IntVar()
box1 = Checkbutton(root, variable=var1, bg='#18191A', fg='black').place(x=20, y=200)
label2 = tk.Label(text="Decode", font=('Arial', 11), fg='white', bg='#18191A')
label2.place(x=50, y=230)
var2 = IntVar()
box2 = Checkbutton(root, variable=var2, bg='#18191A', fg='black').place(x=20, y=230)
label5 = tk.Label(text="Message:", font=('Arial', 11), fg='white', bg='#18191A')
label5.place(x=20, y=10)
mtb = tksc.ScrolledText(root, height=2, width=22, font=('Arial', 20), bg='#3A3B3C', fg='white')
mtb.place(x=20, y=40)
label6 = tk.Label(text="Decoding key:", font=('Arial', 11), fg='white', bg='#18191A')
label6.place(x=20, y=120)
ktb = tksc.ScrolledText(root, height=1, width=22, font=('Arial', 20), bg='#3A3B3C', fg='white')
ktb.place(x=20, y=150)
label6 = tk.Label(text="Converted:", font=('Arial', 11), fg='white', bg='#18191A')
label6.place(x=20, y=260)
ctb = tksc.ScrolledText(root, height=2, width=22, font=('Arial', 20), bg='#3A3B3C', fg='white')
ctb.place(x=20, y=290)
ascii = [(" ", 32), ("!", 33), ('"', 34), ("#", 35), ("$", 36), ("%", 37), ("&", 38), ("'", 39), ("(", 40), (")", 41), ("*", 42), ("+", 43), (",", 44), ("-", 45), (".", 46), ("/", 47), ("0", 48), ("1", 49), ("2", 50), ("3", 51), ("4", 52), ("5", 53), ("6", 54), ("7", 55), ("8", 56), ("9", 57), (":", 58), (";", 59), ("<", 60), ("=", 61), (">", 62), ("?", 63), ("@", 64), ("A", 65), ("B", 66), ("C", 67), ("D", 68), ("E", 69), ("F", 70), ("G", 71), ("H", 72), ("I", 73), ("J", 74), ("K", 75), ("L", 76), ("M", 77), ("N", 78), ("O", 79), ("P", 80), ("Q", 81), ("R", 82), ("S", 83), ("T", 84), ("U", 85), ("V", 86), ("W", 87), ("X", 88), ("Y", 89), ("Z", 90), ("[", 91), ("\\", 92), ("]", 93), ("^", 94), ("_", 95), ("`", 96), ("a", 97), ("b", 98), ("c", 99), ("d", 100), ("e", 101), ("f", 102), ("g", 103), ("h", 104), ("i", 105), ("j", 106), ("k", 107), ("l", 108), ("m", 109), ("n", 110), ("o", 111), ("p", 112), ("q", 113), ("r", 114), ("s", 115), ("t", 116), ("u", 117), ("v", 118), ("w", 119), ("x", 120), ("y", 121), ("z", 122), ("{", 123), ("|", 124), ("}", 125), ("~", 126)]

def convert():
  global var1
  global var2
  global mtb
  global ascii
  global starting
  global ktb
  global ctb
  starting = mtb.get("1.0","end-1c")
  binaries = []
  decimals = []
  strings = []
  if var1.get() == 1:
    temp = ""
    binary = ""
  
    string = starting
    for character in string:
      for code in ascii:
        if character == code[0]:
          decimals.append(code[1])
  
        else:
          pass
  
    offset = random.randint(1,9)
    for decimal in decimals:
      decimal -= offset
      temp = bin(decimal)[2:]
      
      if len(temp) < 8:
        difference = 8 - len(temp)
        missing = ""
        
        for digit in range(difference):
          missing += "0"
        
        add = missing + str(temp)
        temp = add
        
      binary += temp
  
    temp = ""
    encoded = ""
    reverse = ""
    key = random.randint(1,7)
    for digit in binary:
      temp += digit
      if len(temp) == 8:
        reversed = temp [::-1]
        encode = reversed[key:] + reversed [:key]
        reverse += encode 
        temp = ""
        
    for character in reverse:
      if character == "0":
        encoded += "1"
        
      elif character == "1":
        encoded += "0"
  
    combined = str(key) + str(offset)
    output = ("Encoded: " + encoded + " Key: " + combined)
    ctb.delete("1.0","end")
    ctb.insert(tk.END, str(output))
    
  elif var2.get() == 1:
    key = int(ktb.get("1.0","end-1c"))
    temp = ""
    string = ""
  
    encoded = starting
    reverse = ""
    for digit in encoded:
      temp += digit
      if len(temp) == 8:
        displacement = int(str(key)[0])
        reversed = temp [::-1]
        reverse += reversed[displacement:] + reversed[:displacement]
        temp = ""
  
    binary = ""
    for digit in reverse:
      if digit == "0":
        binary += "1"
        
      elif digit == "1":
        binary += "0"
  
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
      decimal += int(str(key)[1])
      for code in ascii:
        if decimal == code[1]:
          found += 1
          string += code[0]
          
        else:
          pass
  
      if found == 0:
        string += "� "
          
    output = ("Decoded: " + string)
    ctb.delete("1.0","end")
    ctb.insert(tk.END, str(output))
    
buttonconvert=tk.Button(root, width=7, height=1, text="Convert", font=('Arial', 20), bg='black', fg='white', command=convert)
buttonconvert.place(x=130, y=375)
root.mainloop()