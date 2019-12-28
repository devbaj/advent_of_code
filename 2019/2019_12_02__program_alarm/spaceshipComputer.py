def executeInstructions(instructionSet):
  for command in range(0, len(instructionSet) - 1, 4):
    if instructionSet[command] == 99:
      break
    elif instructionSet[command] == 1:
      storageIndex = instructionSet[command + 3]
      instructionSet[storageIndex] = \
        instructionSet[instructionSet[command + 1]] + \
          instructionSet[instructionSet[command + 2]]
    elif instructionSet[command] == 2:
      storageIndex = instructionSet[command + 3]
      instructionSet[storageIndex] = \
        instructionSet[instructionSet[command + 1]] * \
          instructionSet[instructionSet[command + 2]]
    else:
      print(f"Unknown command encountered at index {command}")
  return instructionSet

def replaceInitialAddresses(instructionSet, noun = 12, verb = 2):
  instructionSet[1] = noun
  instructionSet[2] = verb
  return instructionSet

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