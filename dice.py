import random
import math
import re
import numpy
from BigNumRandom import BigNumRandom

regex_rolls = re.compile("([+-]?)(\d*)(d([1-9]\d*))?")

def roll_dices_string(dices_string : str):
  result = 0
  operations = re.findall(regex_rolls, dices_string)
  for operation in operations:
    result += calc_dice_operation(operation)
  return result

def calc_dice_operation(parts : tuple):
  value = 0
  sign = 1 if parts[0] != '-' else -1
  print(parts)

  if parts[2] != '':
    times = int(parts[1]) if parts[1] != '' else 1
    sides = int(parts[3])
    value += rol_dices(times, sides)
  elif parts[1] != '':
    value = int(parts[1])

  return sign * value


def rol_dices(times: int, sides: int):
  result = 0

  if times < 1000:
    for roll in range(times):
      result += roll_dice(sides)
  else:
    result = approximate_roll(times, sides)
  return result


def roll_dice(sides: int):
  # randint includes the upperbound, heresy!
  return random.randint(1,sides)


def approximate_roll(times: int, sides: int):
  mu = times * (sides + 1) / 2
  sigma = math.sqrt(times * (sides * sides -1) / 12)
  print('mu:', mu, 'sigma:', sigma)

  result = BigNumRandom.normalvariate(mu, sigma)
  print('result numpy:', result)
  
  if result < times:
    result = times
  elif result > times * sides:
    result = times * sides
  return result

# test cases regex
# 1d1+1d2-1d3-4+5-6 advantage
# 1d1+1d2-1d3-4+5-6 adv
# 1d1+1d2-1d3-4+5-6 a
# 1d1+1d2-1d3-4+5-6 disadvantage
# 1d1+1d2-1d3-4+5-6 dis
# 1d1+1d2-1d3-4+5-6 d
# 1d1+1d2-1d3-4+5-6advantage
# 1d1+1d2-1d3-4+5-6adv
# 1d1+1d2-1d3-4+5-6a
# 1d1+1d2-1d3-4+5-6disadvantage
# 1d1+1d2-1d3-4+5-6dis
# 1d1+1d2-1d3-4+5-6d
# 1d3
# 9999d20
# -5d20+5
# 1d1+d2-1d3-4+5-6
# d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999