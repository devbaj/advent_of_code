
def addition(x, y):
  return x + y

def multiplication(x, y):
  return x * y

def preparations(sequence, noun, verb):
  sequence[1] = noun
  sequence[2] = verb
  return sequence

def reader(sequence):
  for command in range(0, len(sequence) - 1, 4):
    if sequence[command] == 99:
      print("EXITING")
      break
    elif sequence[command] == 1:
      storageIndex = sequence[command + 3]
      sequence[storageIndex] = addition(sequence[sequence[command + 1]], sequence[sequence[command + 2]])
    elif sequence[command] == 2:
      storageIndex = sequence[command + 3]
      sequence[storageIndex] = multiplication(sequence[sequence[command + 1]], sequence[sequence[command + 2]])
    else:
      print(f"Unknown command encountered at index {command}")
  return sequence