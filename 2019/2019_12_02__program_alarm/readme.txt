Problem instructions:
https://adventofcode.com/2019/day/2

Objectives: build intcode program

OPCODES:
1: adds together two numbers and stores the result
2: multiplies together two numbers and stores the result
99: program is finished
-After an opcode has been processed, move forward four positions to find the
next one

OPCODE PARAMETERS:
-The two numbers directly following an opcode indicate the positions of the
numbers to be added or multiplied
-The third number after an opcode indicates where the sum or product should be
stored

PART 2:
In this case we will be given a number the instruction set should produce as long
as we replace the values at 1 and 2 with the correct values. We are to determine
what those values should be. The answer will be 100 * noun + verb.

PROCEDURE: (part 2 steps preceeded by *)
-Parse input into integer array
  -read file
  -split string on commas
  -cast each value to int
-change value at index 1 to 12, at index 2 to 2, according to problem
  * - nested loop over attempts to try all combinations of values between 0 and 99
-iterate over array 4 values at a time (problem indicates intcodes will always
be in groups of 4, except exit code 99)
  -if 99 encountered, exit immediately
  -if anything not 1, 2, or 99 encountered, error out
  -if 1 or 2 encountered, find where the result of the calculation needs to go
    -location instruction is at command + 3
    -get location of values to be operated on (command + 1 and command + 3)
      -order doesn't matter since we are only multiplying and dividing
    -if 1, add; if 2, multiply
-after exiting, the value at index 0 is our answer
  * - after exiting, check if answer matches desired ouput. if so, produced result
    * - if not, increment either verb or noun and try again
    * - if both verb and noun reached 99 we did not find the desired result