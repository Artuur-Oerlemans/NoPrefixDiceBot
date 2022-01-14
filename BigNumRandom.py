import math
import random

class BigNumRandom:
  def normalvariate(mu: int, sigma: int) -> int:
    """Normal distribution.
    mu is the mean, and sigma is the standard deviation.
    """
    # Uses Kinderman and Monahan method. Reference: Kinderman,
    # A.J. and Monahan, J.F., "Computer generation of random
    # variables using the ratio of uniform deviates", ACM Trans
    # Math Software, 3, (1977), pp257-260.

    NV_MAGICCONST = 4 * math.exp(-0.5) / math.sqrt(2.0)
    u1 = 0
    u1 = 0

    while True:
        u1 = random.random()
        u2 = 1.0 - random.random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -math.log(u2):
            break
    precision = 10000000000000000
    return int(mu) + int(NV_MAGICCONST * (u1 - 0.5) * sigma * precision) // int(u2 * precision)