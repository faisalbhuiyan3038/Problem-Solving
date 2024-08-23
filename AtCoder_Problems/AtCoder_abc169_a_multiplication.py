# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Plan
# Take 2 integer input from user in 2 different variables
# Constraint values of both so that it's not less than 1 or more than 100
#  print the multiplied value


valA, valB = map(int, input().split());
if (1 > valA <100):
  print('Both values should be between 1 and 100.')
  exit()

if (1 > valB <100):
  print('Both values should be between 1 and 100.')
  exit()

result = valA * valB
print(str(result))
