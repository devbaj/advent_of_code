import parser # bespoke parser module for this problem
import spaceshipComputer as comp # logic module

def main():
  menu()

def menu():
  userChoice = True
  while userChoice:
    print("**********MENU**********\n"
        "1) Obtain results from a specific instruction set\n"
        "2) Find the requested product of the required inputs to reach a specific output\n"
        "3) Exit")
    userChoice = input("Please select an option: ")

    if userChoice == "1":
      filename = input("Filename: ")
      answer = calculateIntcodeResult(filename)
      if not answer:
        print("ERROR")
      else:
        print(f"ANSWER: {answer}")

    elif userChoice == "2":
      filename = input("Filename: ")
      desiredResult= input("Desired result: ")
      result = determineNecessaryInputs(filename, desiredResult)
      if not result:
        print("ERROR")
      else:
        noun = result["noun"]
        verb = result["verb"]
        answer = 100 * noun + verb
        print(f"Answer: {answer}")

    elif userChoice == "3":
      print("exiting...")
      return 0

    elif userChoice != "":
      print("Invalid choice. Please try again.")

def calculateIntcodeResult(filename):
  initialMemoryState = parser.sanitizeInput(filename)
  if not initialMemoryState:
    return None
  comp.replaceInitialAddresses(initialMemoryState)
  finalMemoryState = comp.executeInstructions(initialMemoryState)
  return finalMemoryState[0]

def determineNecessaryInputs(filename, desiredResult):
  initialMemoryState = parser.sanitizeInput(filename)
  if not initialMemoryState:
    return None
  answer = comp.testInputs(initialMemoryState, int(desiredResult))
  if not answer:
    print("No combination of inputs will produce that ouput")
  return answer

if __name__ == "__main__":
  main()