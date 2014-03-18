import string
import sys
import os
import math
def caesar(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
    else:
      cipherText += ch
  return cipherText
if __name__ == '__main__':
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  fo = open(os.path.join(__location__, 'text.txt'), "r")
  text = fo.readline()
  fo.close()
	
  fo = open(os.path.join(__location__, 'instructions.txt'), "r")
  shift = fo.readline()
  fo.close()
	
  fo = open(os.path.join(__location__, 'result.txt'), "w")
  fo.write(caesar(text, 2))
  fo.close();