import parser # bespoke parser module for this problem
import spaceshipComputer as comp # logic module

# * opens program and sends user directly to the menu
def main():
  menu()

# * menu lets user choose between either part of the question presented
# ! input validation is incomplete but sufficient for our purposes so far
def menu():
  userChoice = True
  while userChoice:
    print("**********MENU**********\n"
        "1) Obtain results from a specific instruction set\n"
        "2) Find the requested product of the required inputs to reach a specific output\n"
        "3) Exit")
    userChoice = input("Please select an option: ")
# * OPTION 1: handles part 1 of question prompt
    if userChoice == "1":
      filename = input("Filename: ")
      answer = calculateIntcodeResult(filename)
      if not answer:
        print("ERROR")
      else:
        print(f"ANSWER: {answer}")
# * OPTION 2: handles part 2 of question prompt
    elif userChoice == "2":
      filename = input("Filename: ")
      desiredResult= input("Desired result: ")
      result = determineNecessaryInputs(filename, desiredResult)
      if not result:
        print("ERROR")
      else:
        noun = result["noun"]
        verb = result["verb"]
        answer = 100 * noun + verb # this is the processing requested by the prompt
        print(f"Answer: {answer}")
# * OPTION 3: exits the program
    elif userChoice == "3":
      print("exiting...")
      return 0
# * invalid choice returns user to menu
    elif userChoice != "":
      print("Invalid choice. Please try again.")

# * handles the instructions for part 1, only calcluating the answer (0th position) based on a given input
# @param filename - string, name of the file containing the input
# @return None - invalid filename, returns for error processing
# @return finalMemoryState[0] - int, the 0th value of our array after processing; the answer we are seeking
def calculateIntcodeResult(filename):
  initialMemoryState = parser.sanitizeInput(filename)
  if not initialMemoryState:
    return None
  comp.replaceInitialAddresses(initialMemoryState)
  finalMemoryState = comp.executeInstructions(initialMemoryState)
  return finalMemoryState[0]

# * handles the instructions for part 2, determining what two inputs will give us a specific result
# @param filename - string, name of the file containing the input
# @param desiredResult - string, the end calculation for which we want to find inputs
# @return None - invalid filename, return for error processing
# @return answer - dict{"noun", "verb"}, a dictionary containing the two inputs that get us the desired result
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