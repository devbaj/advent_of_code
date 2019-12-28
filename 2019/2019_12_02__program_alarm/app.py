import parser # * bespoke parser module for this problem
import operations

GOAL_OUTPUT = 19690720

def main():
  contents = readInFile("puzzle_input")
  initialMemoryState = parser.parseInput(contents)
  print(f"INITTIAL MEMORY STATE: {initialMemoryState}")

  noun= 0
  verb = 0
  output = None
  testNumber = 0

  for i in range (0, 99):
    for j in range (0, 99):
      testArray = initialMemoryState.copy()
      operations.preparations(testArray,j,i)
      result = operations.reader(testArray)
      output= result[0]
      if output == GOAL_OUTPUT: break
    if output == GOAL_OUTPUT: break

  # while output != GOAL_OUTPUT:
  #   testArray = initialMemoryState.copy()
  #   testArray = operations.preparations(testArray, noun, verb)
  #   result = operations.reader(testArray)
  #   output = result[0]
  #   print(f"TEST NUMBER: {testNumber}, OUTPUT: {output}")
  #   if noun < 99:
  #     noun += 1
  #   elif verb < 99:
  #     verb += 1
  #   else: break

  #   testNumber += 1

  if output == GOAL_OUTPUT:
    print("success!")
    print(f"Noun: {j}, Verb: {i}")
    answer = 100 * j + i
    print(f"ANSWER: {answer}")
  else:
    print("failure")

def readInFile(filename):
  f = open(filename, "r")
  if f.mode == "r":
    contents = f.read()
  return contents

if __name__ == "__main__":
  main()