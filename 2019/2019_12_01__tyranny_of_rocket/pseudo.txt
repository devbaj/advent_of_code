problem instructions:
https://adventofcode.com/2019/day/1

Objective: determine the sum of fuel requirements for all modules on my
spacecraft.

Specifics:
- fuel rq'd is bassed on module mass determined by:
      [ floored (mass / 3) ] - 2
- total fuel requirement is the sum of all fuel rq'd by modules
- fuel itself has mass and requires fuel to launch it, determined by same formula

Input:
- text file, list of integers separated by newlines

Basic plan:
- parse input to int array
- for each entry in array calculate fuel according to formula
      -part 2- calculate fuel required for that amount, then that amount, until
      the value is less than 2
- add module fuel requirements together
- print total