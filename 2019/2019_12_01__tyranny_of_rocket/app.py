import parser # * bespoke parser for this problem
import fuelCalc # * module containing all of the logic for this problem

# * executes functions in order and prints our answer
def main():
  contents = readInFile("puzzle_input")
  if not contents:
    print("input not found")
    return False
  parsedInput = parser.parseInput(contents)
  answer = fuelCalc.getTotalFuelRequired(parsedInput)
  print(f"Total fuel required: {answer}")

# * reads in the contents of the file and returns the string
# @param filename - the name of the file where the puzzle input is found
# @return contents - the entirety of the file's contents in string format
# @return None - in case of error reading file
def readInFile(filename):
  f = open(filename, "r")
  if f.mode == "r":
    contents = f.read()
    return contents
  else:
    return None

if __name__ == "__main__":
  main()