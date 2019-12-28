import parser
import fuelCalc

def main():
  f=open("puzzle_input", "r")
  if f.mode == "r":
    contents = f.read()
    parsedInput = parser.parseInput(contents)
    answer = fuelCalc.getTotalFuelRequired(parsedInput)
    print(f"Total fuel required: {answer}")

if __name__ == "__main__":
  main()