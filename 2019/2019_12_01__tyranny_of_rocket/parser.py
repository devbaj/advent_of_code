def parseInput(contents):
  listOfMasses = contents.split("\n")
  listOfMasses.pop()
  for item in listOfMasses:
    item = int(item)
  return listOfMasses