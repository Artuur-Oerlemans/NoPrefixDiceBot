import random
import math

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

  result = int(round(random.normalvariate(mu, sigma)))
  print('result:', result)
  
  if result < times:
    result = times
  elif result > times * sides:
    result = times * sides
  return result