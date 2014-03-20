import string
import sys
import os
import math
import base64
import pdb
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def caesar(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
	  if stayInAlphabet < ord('a'):
	    stayInAlphabet += 26 - ord('a') - stayInAlphabet
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
    else:
      cipherText += ch
  return cipherText
def file_len(fname):
  with open(fname) as f:
    for i, l in enumerate(f):
      pass
  return i + 1
def apply_instruction(mode, lines, instruction):
  encrypt_mode = "encrypt"
  decrypt_mode = "decrypt"
  if mode != encrypt_mode and mode != decrypt_mode:
    return lines
  newLines = []
  caesar_instruction = 'shift_letters '
  encode_instruction = 'encoding = '
  if instruction.startswith(caesar_instruction):
    parameter = instruction[len(caesar_instruction):]
	instruction = caesar_instruction
  if instruction.startswith(encode_instruction):
    parameter = instruction[len(encode_instruction):]
    instruction = encode_instruction
  if mode == decrypt_mode:
      lines = reversed(lines)
  for line in lines:
	if instruction == caesar_instruction:
      if is_int(parameter):
		if mode == decrypt_mode:
		  parameter = -parameter
	    newLines.extend(caesar(line, parameter))
    elif instruction == encode_instruction:
      if parameter == "base64":
        if mode == encrypt_mode
          newLines.extend(base64.b64encode(line))
        elif mode == decrypt_mode
          newLines.extend(base64.b64decode(line)
  return newLines
if __name__ == '__main__':
  pdb.set_trace()
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  textFile = open(os.path.join(__location__, 'text.txt'), "r")
  lines = textFile.readlines()
  textFile.close()
  
  instructionFile = open(os.path.join(__location__, 'instructions.txt'), "r")
  instructions = instructionFile.readlines()
  instructionFile.close()
  mode = ""
  count = 0
  for instruction in instructions:
    if not instruction.startswith('//'):
      mode = instruction
      instructions = instructions[count:]
      break
    count += 1
  print count + ' mode'
  for instruction in instructions:
    lines = apply_instruction(mode, lines, instruction)

  resultFile = open(os.path.join(__location__, 'result.txt'), "w")
  resultFile.writelines(lines)
  resultFile.close();
