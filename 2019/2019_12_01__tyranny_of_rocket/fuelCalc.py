import math # standard python lib

# * runs logic for fuel calculation
# @param listOfMasses - int array, mass of each spaceshipt module
# @return - returns other function result
def getTotalFuelRequired(listOfMasses):
  listOfFuelRequirements = []
  for entry in listOfMasses:
    listOfFuelRequirements.append(recursiveCalculateFuelForModule(entry))
  return sumFuelTotals(listOfFuelRequirements)

# * calculates the fuel required to launch an individual spaceship module
# * formula provided by problem prompt (view psuedo for more detail)
# ! This function recurses because fuel also has weight; the fuel required to lift the module itself requires fuel, and so forth
# @param mass - int, mass of a given spaceship module
# @return final (recursive) - int, amount of fuel required to launch module
def recursiveCalculateFuelForModule(mass):
  rounded = math.floor( int(mass) / 3)
  final = rounded - 2
  if final <= 0: # * base case; negatives and zero amounts are ignored per problem instructions
    return 0
  else:
    return final + recursiveCalculateFuelForModule(final) # * Recursive call
    # returns the fuel required to lift this amount of mass, then calls itself
    # to calculate the amount of fuel required to lift that amount of fuel, and so on

# * sums the amounts of fuel required by all modules to arrive at a final fuel requirement
# @param listOfFuelRequirements - int array, fuel total required by each module
# @return totalFuelRequired - int, total fuel required to launch all modules
def sumFuelTotals(listOfFuelRequirements):
  totalFuelRequired = 0
  for item in listOfFuelRequirements:
    totalFuelRequired += item
  return totalFuelRequired