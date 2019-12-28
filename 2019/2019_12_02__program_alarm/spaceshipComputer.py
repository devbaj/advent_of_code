# handles majority of problem's logic

# * executes the commands in the intcode array, according to rules set by problem
# @param instructionSet - int array, the intcode containing instructions on the operations to perform
# @return instructionSet - in array, our original array, but modified according to the instructions found within it
def executeInstructions(instructionSet):
  for command in range(0, len(instructionSet) - 1, 4):
    if instructionSet[command] == 99:
      break
    elif instructionSet[command] == 1: # 1 indicates the values should be added per problem
      storageIndex = instructionSet[command + 3]
      instructionSet[storageIndex] = \
        instructionSet[instructionSet[command + 1]] + \
          instructionSet[instructionSet[command + 2]]
    elif instructionSet[command] == 2: # 2 indicates the values should be multiplied per problem
      storageIndex = instructionSet[command + 3]
      instructionSet[storageIndex] = \
        instructionSet[instructionSet[command + 1]] * \
          instructionSet[instructionSet[command + 2]]
    else:
      print(f"Unknown command encountered at index {command}")
  return instructionSet

# * replaces the values at addresses 1 and 2 with either set values (part 1) or variable values (part 2)
# @param instructionSet - int array, the intcodes containting our instructions
# @param noun - int, the value to put at address 1 (default 12 per part 2)
# @param verb - int, the value to put at address 2 (default 2 per part 2)
# @return instructionSet - int array, our intcodes with addresses 1 and 2 modified
def replaceInitialAddresses(instructionSet, noun = 12, verb = 2):
  instructionSet[1] = noun
  instructionSet[2] = verb
  return instructionSet

# * tests all possible combinations of inputs for noun and verb according to the conditions established in part 2
# @param initialMemoryState - int array, the original intcode set with no modifications
# @param desiredResult - int, the result for we want to find the inputs
# @return anonymous dictionary - each value it an int, the inputs which produce our desired result
# @return None - no combination found to produce desired result, return for error handling
def testInputs(initialMemoryState, desiredResult):
  for noun in range(0, 99):
    for verb in range(0, 99):
      testArray = initialMemoryState.copy()
      replaceInitialAddresses(testArray, noun, verb)
      result = executeInstructions(testArray)
      output = result[0]
      if output == desiredResult: break
    if output == desiredResult: break
  if output == desiredResult:
    return {"noun": noun, "verb": verb}
  else:
    return None