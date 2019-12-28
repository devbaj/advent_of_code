import math

def calculateFuelForModule(mass):
  rounded = math.floor( int(mass) / 3)
  final = rounded - 2
  if final <= 0:
    return 0
  else:
    return final + calculateFuelForModule(final)

def sumFuelTotals(listOfFuelRequirements):
  totalFuelRequired = 0
  for item in listOfFuelRequirements:
    totalFuelRequired += item
  return totalFuelRequired

def getTotalFuelRequired(listOfMasses):
  listOfFuelRequirements = []
  for entry in listOfMasses:
    listOfFuelRequirements.append(calculateFuelForModule(entry))
  return sumFuelTotals(listOfFuelRequirements)