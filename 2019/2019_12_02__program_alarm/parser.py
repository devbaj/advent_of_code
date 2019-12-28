
# This module is for parsing the puzzle input provided by adventofcode.com
# It is not intended to be functional for any other specific problem or use case

# * parses the input string of into an integer array for handling
# @param stringFormattedInput - the input read in from file
# @return arrayIntegerInput - int array, a list of all intcode values as integers
def parseInput(stringFormattedInput):
  arrayFormattedInput = stringFormattedInput.split(",")
  arrayFormattedInput[len(arrayFormattedInput) - 1] = \
    arrayFormattedInput[(len(arrayFormattedInput) - 1)].strip("\n")
  arrayIntegerInput = []
  for item in arrayFormattedInput:
    arrayIntegerInput.append(int(item))
  return arrayIntegerInput

# * reads the input from a file into a string
# @param filename - string, the name of the file to be read
# @return contents - string, the file's contents in string form
# @return None - filename is invalid, returns for error handling
def readInFile(filename):
  try:
    f = open(filename, "r")
    if f.mode == "r":
      contents = f.read()
      return contents
  except:
    print("That file does not exist")
    return None

# * handles all parsing and cleaning logic
# @param filename- string, name of the file to be read
# @return None - invalid filename, return for error handling
def sanitizeInput(filename):
  contents = readInFile(filename)
  if not contents:
    return None
  return parseInput(contents)