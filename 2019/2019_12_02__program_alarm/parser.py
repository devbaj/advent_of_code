"""
* This module is for parsing the puzzle input provided by adventofcode.com
* It is not intended to be functional for any other specific problem or use case
"""

#* This function parses the input string of into an integer array for handling
# @param stringFormattedInput - the input read in from file
def parseInput(stringFormattedInput):
  arrayFormattedInput = stringFormattedInput.split(",")
  arrayFormattedInput[len(arrayFormattedInput) - 1] = \
    arrayFormattedInput[(len(arrayFormattedInput) - 1)].strip("\n")
  arrayIntegerInput = []
  for item in arrayFormattedInput:
    arrayIntegerInput.append(int(item))
  return arrayIntegerInput


def readInFile(filename):
  try:
    f = open(filename, "r")
    if f.mode == "r":
      contents = f.read()
      return contents
  except:
    print("That file does not exist")
    return None

def sanitizeInput(filename):
  contents = readInFile(filename)
  if not contents:
    return None
  return parseInput(contents)