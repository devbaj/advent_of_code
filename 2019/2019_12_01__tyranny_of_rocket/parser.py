"""
* This parser is specific to this problem set and its input format
* It is not intended for generalized use
"""

# * Responsible for turning the file's contents into an array of integers
# @param contents - the raw string input from the file read in by main()
# @return listOfMasses - array of integers representing the mass of each spaceship module
def parseInput(contents):
  listOfMasses = contents.split("\n")
  listOfMasses.pop() # removes trailing character left by the file
  for item in listOfMasses:
    item = int(item)
  return listOfMasses